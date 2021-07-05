# dData Engineer Study
1. Kafka Download

   ```bash
   $ wget http://apache.mirror.cdnetworks.com/kafka/2.4.1/kafka_2.12-2.4.1.tgz
   kafka_2.12-2.4.1.tgz         100%[==============================================>]  59.47M  7.80MB/s    in 7.7s
   # apache kafka 링크 변경(하단)
   # https://archive.apache.org/dist/kafka/2.4.1/kafka_2.12-2.4.1.tgz
   # 현재 kafka 최신 버전 링크 : https://www.apache.org/dyn/closer.cgi?path=/kafka/2.8.0/kafka_2.12-2.8.0.tgz

   $ tar -xzf kafka_2.12-2.4.1.tgz
   $ cd kafka_2.12-2.4.1
   ```




2. Zookeeper 실행

   ```bash
   $ ./bin/zookeeper-server-start.sh ./config/zookeeper.properties

   # ./config/zookeeper.properties 데이터 경로 수정 (놔둬도 됨)
   ```



3. Kafka 서버 실행

   ```bash
   $ ./bin/kafka-server-start.sh ./config/server.properties

   # ./config/server.properties 로그 경로 수정 (놔둬도 됨)
   ```



4. python-kafka Download

   ```bash
   $ pip install kafka-python
   ```

   만약 python에서 kafka를 사용해야한다면 상단처럼 pip를 통해 패키지를 받자.



5. chromedriver Download

   먼저, 'chrome' 을 실행한 후, '도움말' -> 'Chrome 정보'를 클릭하여, 사용중인 크롬 버전을 확인한다. 

   그리고, [링크](https://sites.google.com/a/chromium.org/chromedriver/downloads)를 클릭하여 자신에게 맞는 버전의 chromedriver를 다운로드 받는다.

   물론 windows이니, 'chromedriver_win32.zip' 을 받아야한다.

   그리고 압축을 풀어주고 사용하면 된다. 하단은 python에서 chromedriver를 사용할 때의 예이다.

   ```bash
   driver = webdriver.Chrome('C:\chromedriver.exe')
   ```

------

해야할 일

> - [x] 아래꺼 하기 전에 kafka부터 다시 제대로 공부하자...제에에에발
> - [ ] 가상환경 잡는 것 보다 CDP 프로젝트 진행하면서, 개인용 PC를 사용하여 서버를 지속적으로 운영하기 어려운 것을 인지했다... AWS EC2를 사용하면 좋을거 같은데.... 가격 부분을 좀 보고 괜찮다 싶으면 AWS EC2를 사용하기로... ㅠ
> - [ ] virtualenv 및 conda 활용법 정리 (아 굉장히 좋더라)