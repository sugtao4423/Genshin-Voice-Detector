# Genshin Voice Detector
原神のボイスをどのキャラのものか判別させるやつ

## ここにある `model.pickle`
以下のデータを学習させたもの

* 各キャラの自己紹介などのボイス
* 編成ボイスや攻撃/ダメージボイスはなし

学習スコア: `0.9435082532643508`

<details>
<summary>キャラボイス詳細</summary>

キャラ | キャラID | ボイス数
--- | --- | ---
アンバー | amber | 43
バーバラ | barbara | 42
北斗 | beidou | 42
ベネット | bennett | 42
重雲 | chongyun | 41
ディルック | diluc | 41
フィッシュル | fischl | 39
ジン | qin | 44
ガイア | kaeya | 42
刻晴 | keqing | 45
クレー | klee | 42
リサ | lisa | 42
モナ | mona | 40
凝光 | ningguang | 44
ノエル | noel | 43
七七 | qiqi | 40
レザー | razor | 40
スクロース | sucrose | 44
ウェンティ | venti | 43
香菱 | xiangling | 42
魈 | xiao | 41
行秋 | xingqiu | 42
タルタリヤ | tartaglia | 40
鍾離 | zhongli | 42
ディオナ | diona | 45
辛炎 | xinyan | 42
甘雨 | ganyu | 44
アルベド | albedo | 40
ロサリア | rosaria | 44
胡桃 | hutao | 46
煙緋 | yanfei | 42
エウルア | eula | 44

</details>

## `make-voices.sh`
1. 原神のデータベースである `Honey Impact` からボイスデータをDL
1. DLしてきたボイスデータの再生時間を取得
1. 一番短いものに合わせてすべてのボイスデータを切り抜き

するスクリプト。

Honey Impactにあるボイスデータは原神のリソースから展開されたものをそのまま公開しているのでこれを学習して良いと思う。

## 使い方
[MeguminSama/genshin-audio-extractor](https://github.com/MeguminSama/genshin-audio-extractor) を使って展開された音声データをこのスクリプトで識別させれば良い。
