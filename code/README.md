# How to run Kafka publish-server?
1. zookeeper 서버 실행

```bash
./bin/zookeeper-server-start.sh config/zookeeper.properties
```

- kafka가 설치된 디렉터리에서 위 명령어 실행



2. kafka 서버 실행 (최소 3대 실행 권장)

```bash
./bin/kafka-server-start.sh config/server.properties
```



3. kafka consumer 실행

```bash
./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test
```

- 마지막 인자에 '--from-beginning' 입력 시, 여기서부터 메시지를 가져온다는 것을 의미



4. ./python/pub_example.py 실행

```bash
python3 ./python/pub_example.py
```

------

해야할 일

> 코로나 데이터 파이프라인 프로젝트 기획