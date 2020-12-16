# What a Logstash!?
> Logstash는 실시간 파이프라인 기능을 가진 오픈소스 데이터 수집 엔진

#### Logstash

- 서로 다른 소스의 데이터를 동적으로 통합 가능

- 원하는 대상으로 데이터 정규화 가능

- 다양한 입력과 필터 및 출력 플러그인을 통해 모든 유형의 이벤트 보강과 변환 가능

- 많은 기본 코덱이 처리 과정을 단순화

- 방대하고 다양한 데이터를 활용하여 통찰력있게 보는 것을 가능케 함




1. 기능

   ![logstash_function](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlTK54%2FbtqEcm5tdcT%2FtavhAMDyBTPM0CDBzrvIK0%2Fimg.png)

   ​	(이미지 출처: https://soyoung-new-challenge.tistory.com/99)

   - 강력한 elasticsearch와 kibana의 시너지와 함께 수평적으로 데이터 프로세스 파이프라인 스케일업 가능
   - 다른 input, filter그리고 output 플러그인들을 Mix, Match 가능
   - 200개가 넘는 플러그인 사용 가능
   - 새로운 플러그인 생성 및 기여 가능




2. 파이프라인

   ![logstash_pipeline](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FtrxsO%2FbtqEbbDydeW%2F8UjRxHMCsgPrMz1XWDY5Xk%2Fimg.png)
   
   ​	(이미지 출처: https://soyoung-new-challenge.tistory.com/99)
   
   - logstash의 전체적인 파이프라인에는 inputs, filters, outputs가 존재
   - inputs, outputs는 필수적 요소
   - 파싱 여부에 따라 filters는 선택적으로 사용 가능
   



3. Logstash 주요 파일

   - Logstash.yml

     ```yaml
  path.data : /var/lib/logstash
     path.logs : /var/log/logstash
     ```
   
     - logstash 실행을 컨트롤하는 setting 파일
     - 다른 설정을 제외한 초기 설정은 상단과 같이 2가지만 세팅되어있음
   
     
   
   - jvm.option
   
     ```properties
     # 초기 total heapsize
     -Xms1g
     
     # 최대 heap size
     -Xmx1g
     ```
   
     - 힙 사이즈 조절 가능
     - 초기 세팅은 상단과 동일
   
     
   
   - Pipeline.yml
   
     ```yaml
     - pipeline.id: main
       patch.config: "/etc/logstash/conf.d/*.conf"
     ```
   
     - 초기엔 단일 파이프라인으로 구성
     - 초기엔 /etc/logstash/conf.d 밑에 있는 .conf 파일로 연결
     - 하나의 인스턴스에서 여러 개의 파이프라인을 실행할 경우 추가
     - .conf 파일명은 원하는대로 설정
     - conf.d 하위에 ~.conf로 작성 가능
   
     
   
   - .conf 파일 구성
   
     - input
       - Beats, CloudWatch, Eventlog 등의 다양한 입력을 지원하여 데이터 수집
       - file, syslog(RFC3164 형식), beats(Filebeat)
     - filter
       - 형식이나 복잡성에 상관없이 설정을 통해 데이터를 동적으로 변환
       - grok: 구문 분석 및 임의의 텍스트로 구성
       - mutate: 이벤트 필드에서 일반적인 변환 수행
       - drop: 이벤트 삭제
       - clone: 이벤트의 복사본 생성
       - geoip: ip 주소의 지리적 위치에 대한 정보 추가
     - output
       - EalsticSearch, Email, ECS, Kafka 등 원하는 저장소에 데이터 전송
       - elasticsearch: 이벤트 데이터를 elasticsearch에 전송
       - file: 디스크 파일에 기록
       - graphite: graphite에 전송 (메트릭을 저장하고 그래프로 작성하는 데 사용되는 오픈 소스 도구)
       - statsd: 카운터 및 타이머와 같은 통계를 수신하고 UDP를 통해 전송되며, 하나 이상의 플러그 가능한 백엔드 서비스에 집계를 전송하는 서비스

​	

------

해야할 일

> .conf 파일의 input, filter, output 예제 및 상세 설명 study
>