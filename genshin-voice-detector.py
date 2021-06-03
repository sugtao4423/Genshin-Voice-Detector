#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import os
import pickle
from time import time

import librosa
import numpy
from sklearn.svm import SVC

VOICE_GLOB_PATTERN = './cut-voices/%s/*.wav'
MODEL_FILE = './model.pickle'

CHAR_LIST = [
    'amber', 'barbara', 'beidou', 'bennett',
    'chongyun', 'diluc', 'fischl', 'qin',
    'kaeya', 'keqing', 'klee', 'lisa',
    'mona', 'ningguang', 'noel', 'qiqi',
    'razor', 'sucrose', 'venti', 'xiangling',
    'xiao', 'xingqiu', 'tartaglia', 'zhongli',
    'diona', 'xinyan', 'ganyu', 'albedo',
    'rosaria', 'hutao', 'yanfei', 'eula'
]


def getMfcc(filename):
    y, sr = librosa.load(filename)
    return librosa.feature.mfcc(y=y, sr=sr)


def learn():
    voice_training = []
    char_training = []
    for index, char in enumerate(CHAR_LIST):
        for wav in glob.glob(VOICE_GLOB_PATTERN % char):
            print('\rReading data of %s...' % wav, end='')
            mfcc = getMfcc(wav)
            voice_training.append(mfcc.T)
            label = numpy.full((mfcc.shape[1], ), index, dtype=numpy.int32)
            char_training.append(label)
    voice_training = numpy.concatenate(voice_training)
    char_training = numpy.concatenate(char_training)

    print('\nStart Learn')
    start = time()
    clf = SVC(C=1, gamma=1e-3)
    clf.fit(voice_training, char_training)
    end = time()
    print('Learning Done!')
    print('Processing: %ss' % round(end - start, 2))
    with open(MODEL_FILE, mode='wb') as f:
        pickle.dump(clf, f, protocol=2)
    print('model saved!')

    print('\nCalculating score...')
    start = time()
    score = clf.score(voice_training, char_training)
    end = time()
    print('score: %s' % score)
    print('Processing: %ss' % round(end - start, 2))


def load():
    with open(MODEL_FILE, mode='rb') as f:
        clf = pickle.load(f)
    print('model loaded!')
    return clf


def test():
    clf = load()
    for wav in glob.glob('./test_voices/*.wav'):
        mfcc = getMfcc(wav)
        prediction = clf.predict(mfcc.T)
        counts = numpy.bincount(prediction)
        result = numpy.argmax(counts)
        print('%s\t%s' % (wav, CHAR_LIST[result]))


if(os.path.exists(MODEL_FILE)):
    test()
else:
    learn()
