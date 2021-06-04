#!/bin/bash
FFMPEG="`which ffmpeg`"

chars=(
    'amber'     'barbara'   'beidou'    'bennett'
    'chongyun'  'diluc'     'fischl'    'qin'
    'kaeya'     'keqing'    'klee'      'lisa'
    'mona'      'ningguang' 'noel'      'qiqi'
    'razor'     'sucrose'   'venti'     'xiangling'
    'xiao'      'xingqiu'   'tartaglia' 'zhongli'
    'diona'     'xinyan'    'ganyu'     'albedo'
    'rosaria'   'hutao'     'yanfei'    'eula'
)
nums=(
    '1000' '1101' '1102' '1103'
    '1201' '1202' '1203' '1204'
    '1205' '1001' '1002' '1003'
    '1004' '2001' '2002' '2003'
    '2004' '2005' '2006' '3001'
    '3002' '3003' '4001' '4002'
    '4003' '4004' '4005' '4006'
    '4007' '4008' '4009' '4010'
    '5001' '5002' '5003' '5004'
    '5005' '6001' '6002' '6003'
    '6004' '7001' '8001' '8002'
    '8003' '8004'
)
VOICES_DIR='./voices'
CUT_VOICES_DIR='./cut-voices'


# download
mkdir $VOICES_DIR
for char in "${chars[@]}"; do
    mkdir "$VOICES_DIR/$char"
    for num in "${nums[@]}"; do
        wget -nv -P "$VOICES_DIR/$char" \
            https://genshin.honeyhunterworld.com/audio/quotes/$char/${num}_jp.wav
        sleep 1
    done
done

# get all voice duration
durations=()
for char in "${chars[@]}"; do
    for wav in `find "$VOICES_DIR/$char" -name "*.wav"`; do
        durations+=(`"$FFMPEG" -i $wav 2>&1 | grep Duration | awk '{print $2}' | tr -d ,`)
    done
done

# get minimum duration
orig_ifs=$IFS
IFS=$'\n'
min_duration=`echo "${durations[*]}" | sort -n | head -n 1`
IFS=$orig_ifs

# cut voice
mkdir $CUT_VOICES_DIR
for char in "${chars[@]}"; do
    mkdir "$CUT_VOICES_DIR/$char"
    for wav in `find "$VOICES_DIR/$char" -name "*.wav"`; do
        echo -ne "\rCutting $wav..."
        filename=`basename $wav`
        $FFMPEG -i $wav -t $min_duration -c copy "$CUT_VOICES_DIR/$char/$filename" > /dev/null 2>&1
    done
done
echo ''
