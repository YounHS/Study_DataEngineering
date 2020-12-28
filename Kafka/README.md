# What a Kafka!?
> Apache Kafka는 LinkedIn에서 개발한 분산 메시징 시스템이며 2011년 오픈소스로 공개되었다. 대용량 실시간 로그 처리에 특화된 아키텍처 설계를 통하여 기존 메시징 시스템보다 우수한 TPS를 보여주고 있다.

#### Kafka

- 분산 스트리밍 플랫폼

- 데이터 파이프 라인 구성 시, 주로 사용하는 오픈소스 솔루션

- 대용량의 실시간 로그 처리에 특화되어 있는 솔루션

- 데이터 손실없이 안전하게 전달하는 것이 주목적인 메시징 시스템

- 클러스터링이 가능하여, **Fault-Tolerant**한 안정적인 아키텍처와 빠른 퍼포먼스로 데이터 처리

- 수평적으로 서버의 **Scale-Out**이 가능

- Pub-Sub모델의 메세지 큐

  > Fault-Tolerant: 시스템 내, Fault(장애)가 발생하더라도 시스템에 지장을 주지 않도록 설계된 컴퓨터 시스템
  >
  > Scale-Out: 서버의 대수를 늘려서 성능을 향상시키는 방법



1. Pub-Sub 모델

   - Publish - Subscribe 모델은 메세지를 특정 수신자에게 직접적으로 보내주는 시스템이 아님

   - publisher는 메세지를 topic을 통해 카테고리화함

   - 분류된 메세지를 수신하길 원하는 receiver는 해당 topic을 subscribe함으로써 메세지 읽기 가능

   - publisher는 topic에 대한 정보만 알고 있고, subscriber도 topic만 바라봄

   - 데이터를 관리하는 Kafka 서버를 사이에 끼고 데이터를 넣는 publisher와 데이터를 읽는 subscriber는 각자의 업무만 Kafka 서버를 통해 수행하므로 서로 모르는 상태

   - Kafka 클러스터를 중심으로 producer가 데이터를 push하고 consumer가 데이터를 pull하는 구조




2. 디스크 순차 저장 및 처리

   - 메세지를 메모리에 저장하는 기존 메시징 시스템과 달리 메세지를 파일 시스템에 저장
   - 파일 시스템에 메세지를 저장하기 때문에 별도의 설정을 하지 않아도 데이터의 영속성 보장 가능
   - 디스크가 순차적으로 저장되어 있으므로 디스크 I/O가 줄어들어 속도가 빠름
   



3. Kafka 구조 및 구성요소

   ![Kafka_archi](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fd8cokW%2FbtqEvYj5sEi%2F3V2KFeLaAkpAoV6XFhXTK0%2Fimg.jpg)

   (이미지 출처: http://blog.mmlac.com/log-transport-with-apache-kafka/)

   - Kafka Broker는 Kafka 서버, Zookeeper는 Kafka Cluster를 구성할 수 있도록 분산 코디네이션 시스템 역할을 함


   - Kafka Broker와 Zookeeper로 구성된 것들을 각각 Kafka Cluster라고 명명


   - Kafka Broker와 Zookeeper는 다른 서버에 설치하여 운영하는 것을 추천하며, 이는 만약 Zookeeper에서 시스템 오류가 발생한 경우, Kafka Broker에 영향을 미치지 않게 하기 위해서임


   - Kafka의 topic은 partition이라는 단위로 쪼개어져 Kafka Cluster의 각 서버들에 분산되어 저장됨


   - partition에는 데이터들이 순차적으로 저장되며, Kafka 서버는 해당 데이터를 설정 시간에 따라 보관

   

   ![Anatomy_of_a_Topic](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcSpDzW%2FbtqEwJmfAK6%2FI4MGF6YN8lzvIJdIsjSQ2k%2Fimg.png)

   (이미지 출처: http://kafka.apache.org/081/documentation.html)

   - 각 partition은 0부터 1씩 증가하는 offset 값을 메세지에 부여하며, 각 partition의 메세지를 식별하는 ID로 사용
   - offset 값은 partition마다 별도로 관리되므로 topic 내에서 메세지를 식별 시, partition 번호와 offset 값을 함께 사용 -> 위 그림에서 최근 쓰여진 메세지들의 ex) (partition_no, offset_no) = (0, 12) / (1, 9) / (2, 12)
   - 이러한 구조로 쓰여진 메세지는 해당 topic을 구독한 consumer가 소비. consumer가 가져다가 사용하는 구조이기 때문에 consumer 스스로가 소비하는 속도 조절 가능
   - consumer들의 묶음을 consumer group이라고 하며, 특정 partition에는 consumer group당 오로지 하나의 consumer만 접근이 가능. 즉, 동일한 consumer group에 속하는 consumer끼리는 동일한 partition에 접근할 수 없음. 이 때, 특정 partition에 접근하는 consumer를 partition owner라고 명명
   - consumer가 message의 offset 번호를 기억하고 있다가, 다음 메세지를 읽어올 때 offset 번호를 이용해서 읽어오기 가능. 한 consumer group 내부의 consumer 끼리는 각자 접근하고 있는 partition의 메세지 offset 값을 공유하고 있기에, 어떤 consumer에서 장애 발생 시, 다른 consumer가 장애가 발생한 consumer의 offset 값을 알고 있기 때문에 해당 consumer 대신 메세지 소비
   - 한 번 정해진 partition owner는 Kafka broker나 consumer 구성의 변동이 있지 않는 한 계속 유지
   - consumer와 partition의 대칭 비율은 1:N이며, consumer가 partition의 수보다 많은 경우는 사용되지 않는 consumer가 생기고, partition의 수가 consumer의 수보다 많은 경우는 하나의 consumer가 2개 이상의 partition에 접근 가능. 따라서 partition과 consumer의 수 조절할 필요 존재



![Kafka_Cluster1](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcAj1C4%2FbtqExZWJ8g0%2F7qxa8TATVt1xD13HcAJhA1%2Fimg.png)

​	(이미지 출처: http://kafka.apache.org/081/documentation.html)

   - Consumer group에 다수의 consumer를 할당하면 각 consumer마다 별도의 partition으로부터 메시지를 받아오기 때문에 (producer가 각 partition에 메시지를 균등하게 분배한다고 가정할 경우), consumer group은 큐 모델로 동작
   - 단일 consumer로 이루어진 consumer group을 활용하면 다수의 consumer가 동일한 partition에 동시에 접근하여 동일한 메시지를 엑세스하기 때문에 pub-sub 모델 구성 가능 (ex) 하나의 채팅창에 여러명 접근)
        - 하나의 consumer에 의하여 독점적으로 partition이 엑세스되기 때문에 동일 partition 내의 메시지는 partition에 저장된 순서대로 처리, 만약 특정 키를 지닌 메시지가 발생 시간 순으로 처리되어야 한다면 partition 분배 알고리즘을 적절하게 구현하여 특정 키를 지닌 메시지는 동일한 partition에 할당되어 단일 consumer에 의해 처리되도록 해야함 (ex) 순서가 중요한 증권사 시스템 같은 경우 필요)
        - 다른 partition에 속한 메시지의 순차적 처리는 보장되지 않으므로, 특정 topic의 전체 메시지가 발생 시간 순으로 처리되어야 할 경우, 해당 topic이 하나의 partition만을 가지도록 설정해야함



​	![kafka_cluster2](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FuRhAk%2FbtqEBeTPqes%2FyYxO2zQuPCqjvhhUzsnbO0%2Fimg.png)

​	(이미지 출처: https://dbjh.tistory.com/54)

   - 각 topic의 patrition들이 분산되어 저장된 형태
   - Kafka는 각각의 Kafka Broker에서 topic들을 관리하는데, 상기와 같이 하나의 topic을 여러개의 partition으로 나누어서 각각의 Kafka Broker에 저장 가능
   - Kafka는 여러 상황을 대비하여 partition을 같은 Cluster 안에 다른 Broker에 복사하여 저장 가능한데, 이 때 필요한 것이 replication-factor 설정 값임. replication-factor는 얼마만큼 partition을 복사할 것인지 설정하는 것
   - 상기와 같은 상황에서 replication-factor가 3이면 총 6개의 partition이 각 서버에 3개씩 생기기 때문에 하단의 그림처럼 총 18개의 partition이 생김
   - replication-factor는 topic 단위의 설정 값. (ex) red는 3, blue는 2로 설정 가능)



​	![Kafka_Cluster3](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbo3ahH%2FbtqEADzZjt9%2FSNpZs9kZQMKYiE7WXRcRP0%2Fimg.png)

​	(이미지 출처: https://dbjh.tistory.com/54)

   - replication-factor의 설정 값에 맞게 partition 복사가 이루어진 상황
   - Red topic을 예로 들면, 첫번째 Broker에서 P0-1이 두번째 Broker에 P0-2로 복사되었고, 또 다시 세번째 Broker에 P0-3으로 복사된 것. 이 때, 각 partition들은 3개의 replica를 가진 것
   - 이 때, 주의깊게 볼 것은 검은 테두리로 씌워진 partition인데, 이 partition이 바로 leader이고 테두리가 씌워져 있지 않은 partition은 follower
   - 메세지를 partition에 쓰고 읽는 행위는 leader를 통해서만 수행 가능하고, follower는 leader의 복사본일 뿐임. follower는 해당 용도로만 사용되는 것은 아니며, 여기서 leader와 follower로 구성된 것을 ISR(In Sync Replica)이라고 함
   - 만약 leader에서 장애가 발생하면, 해당 partition을 복사한 follower들 중 하나가 새로운 leader가 됨



​	![Kafka_Cluster4](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmmBrp%2FbtqEBfE92iQ%2FntqsJAvwEphDrdCawXZT8k%2Fimg.png)

​	(이미지 출처: https://dbjh.tistory.com/54)

   - P0 partition의 기존 leader에서 장애가 발생하여 follower 중 새로운 leader 선출
   - 상기와 같이 새로운 leader가 선출되면 해당 leader를 통해서만 메세지 읽기, 쓰기가 가능



> **Keyword**
>
> - Kafka Broker = Kafka 서버
> - Zookeeper = 분산 코디네이션 시스템 (Kafka 서버 구성에서 필수)
> - Kafka Cluster = (Kafka Broker + Zookeeper) x N
> - Producer(Publisher) = 데이터를 Kafka Cluster에 적재하는 주체
> - Consumer(Subscriber) = Kafka Cluster로부터 데이터를 읽어오는 주체
> - Consumer Group = Consumer의 집합, Consumer x N
> - Topic = Kafka Broker에서 사용하는 데이터(메세지)의 카테고리이며, Partition의 집합, Partition x N
> - Partition = 메세지의 집합, Topic으로 묶여서 관리. Message x N
> - Offset = Partition마다 관리되는 메세지의 인덱스
> - Leader = 메세지를 읽고 쓰는 것이 가능한 Partition
> - Follower = Leader의 복제, 잠재적 Leader

------

해야할 일

> 하기 링크, 이해하며 쭉 훑어보기
>
> - [x] [아파치 카프카](https://engkimbs.tistory.com/691)
> - [x] [Kafka 이해하기](https://medium.com/@umanking/%EC%B9%B4%ED%94%84%EC%B9%B4%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-%EC%9D%B4%EC%95%BC%EA%B8%B0-%ED%95%98%EA%B8%B0%EC%A0%84%EC%97%90-%EB%A8%BC%EC%A0%80-data%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-%EC%9D%B4%EC%95%BC%EA%B8%B0%ED%95%B4%EB%B3%B4%EC%9E%90-d2e3ca2f3c2)
> - [ ] [Kafka 소개 및 아키텍처 정리](https://epicdevs.com/17)
> - [ ] [Topic Replication](https://www.popit.kr/kafka-%EC%9A%B4%EC%98%81%EC%9E%90%EA%B0%80-%EB%A7%90%ED%95%98%EB%8A%94-topic-replication/)