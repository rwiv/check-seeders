# check-seeder

torrent 파일의 seeders, leechers를 체크하는 스크립트

## Requirement

- docker
- docker-compose

## 실행 방법

1. `torrents` 폴더를 만든 뒤 그 안에 체크할 torrent 파일을 전부 넣는다.
2. 스크립트를 실행한다.
    - windows os: `run.bat`을 실행
    - 그 외 os: 터미널에서 `$ docker-compose up`을 실행
3. 실행 이후 `output/result.json`을 확인한다.
