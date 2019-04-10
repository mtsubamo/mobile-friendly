# test
# mobile-friendly
search termを基に、検索結果の上から順にmobile friendlyか判定するシステムです

# HOW TO USE
## install docker
dockerを環境にinstallしてください(おそらくmac??)  
https://docs.docker.com/docker-for-mac/install/

## build image
imageをbuildしてください
```
$ docker build -t mobile-friendly .
```

## run container
コンテナを起動して、中に入ります
```
$ docker run -it mobile-friendly /bin/bash
```

## exec
好きな検索単語を引数に実行してください
```
$ python main.py 紀尾井町　焼肉
```
