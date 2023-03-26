# check-seeder

torrent 파일의 seeders, leechers를 체크하는 스크립트

## Requirement

- docker
- docker-compose

## How to Run

1. 프로젝트 root 경로에 `torrents` 폴더를 생성한 뒤 그 안에 체크할 torrent 파일을 전부 넣는다.
2. docker로 스크립트를 실행한다.
    - windows os: `run.bat`을 실행
    - 그 외 os: 터미널에서 `$ docker-compose up`을 실행
3. 실행이 완료되면 `output/result.json`을 확인한다.
