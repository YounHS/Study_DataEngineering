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
       
       ```properties
       # input
       input {
       	beats {
       		port => 5044
       		host => "0.0.0.0"
       		client_inactivity_timeout => 86400
       	}
       }
       ```
       
       - filebeat로부터 데이터를 받을 때는 input을 beats로 설정
       
       - filebeat로부터 데이터를 받을 포트 지정 (default port = 5044)
       
       - 호스트 상관없이 모든 데이터를 받을 경우 호스트는 0.0.0.0으로 작성
       
         
       
     - filter
       - 형식이나 복잡성에 상관없이 설정을 통해 데이터를 동적으로 변환
       
       - grok: 구문 분석 및 임의의 텍스트로 구성
       
       - mutate: 이벤트 필드에서 일반적인 변환 수행
       
       - drop: 이벤트 삭제
       
       - clone: 이벤트의 복사본 생성
       
       - geoip: ip 주소의 지리적 위치에 대한 정보 추가
       
         ```properties
         filter {
           if "IMP" in [log][file][path] {
             mutate {
               gsub => ["message", ", ", "| "]
             }
             grok {
               match => { "message" => ["%{NUMBER:[imp][date]},%{NUMBER:[imp][h]},%{NUMBER:[imp][cu_id]},%{NUMBER:[imp][au_id]},%{NUMBER:[imp][pu_id]},%{WORD:[imp][c_key]},%{WORD:[imp][p_key]},%{GREEDYDATA:[imp][no_info]},%{NUMBER:[imp][place_id]},%{WORD:[imp][nation]},%{WORD:[imp][device]},%{NUMBER:[imp][no_info2]},%{NUMBER:[imp][user_key]},%{WORD:[imp][p_set_id]},%{GREEDYDATA:[imp][url]},\"%{TIMESTAMP_ISO8601:[imp][cre_tt]}\",%{GREEDYDATA:[imp][remote_addr]},%{NUMBER:[click][ar_id]}"]}
               remove_field => ["message"]
               }
             grok {
               match => { "message" => ["%{NUMBER:[imp][date]},%{NUMBER:[imp][h]},%{NUMBER:[imp][cu_id]},%{NUMBER:[imp][au_id]},%{NUMBER:[imp][pu_id]},%{WORD:[imp][c_key]},%{WORD:[imp][p_key]},%{GREEDYDATA:[imp][no_info]},%{NUMBER:[imp][place_id]},%{WORD:[imp][nation]},%{WORD:[imp][device]},%{NUMBER:[imp][no_info2]},%{NUMBER:[imp][user_key]},%{WORD:[imp][p_set_id]},%{GREEDYDATA:[imp][url]},\"%{TIMESTAMP_ISO8601:[imp][cre_tt]}\""]
               remove_field => ["message"]
               }
             }
             date {
               match => [ "[imp][cre_tt]", "YYYY-MM-dd H:m:s" ]
               target => "@timestamp"
               timezone => "Asia/Seoul"
             }
             mutate {
               gsub => [ '[imp][url]', '"', '']
               convert => ["[imp][au_id]","integer"]
               convert => ["[imp][cu_id]","integer"]
               convert => ["[imp][date]","integer"]
               convert => ["[imp][h]","integer"]
               convert => ["[imp][place_id]","integer"]
               convert => ["[imp][pu_id]","integer"]
             }
           }
         }
         ```
       
       - [log] [file] [path]: 로그의 위치
       
         - 노출 로그를 정제하는 과정으로 우선 log를 읽어오는 경로로 다른 로그와 구분
         - 상단의 경우, 로그 경로에 "IMP"가 포함되어 있으면 이곳에서 필터링
       
       - mutate의 gsub
       
         - 가장 상단에서 grok에 보낼 메시지를 미리 전처리할 작업이 있을 때 사용
         - 상단은 , 구분자를 |로 변경하는 작업을 진행
         - 사용법: mutate {gsub => [필드명, 원래 값, 변경할 값]
       
       - grok 플러그인
       
         - 우선 읽어들인 로그는 message 안에 포함
         - grok을 여러번 사용하면 multiple grok 적용 가능
         - 하나의 grok 패턴에서 파싱이 안되면 message가 그대로 다음 grok으로 넘어오게 되고 재시도
         - 다수의 grok에 파싱이 되는 메시지의 경우, 여러번 grok이 적용되는 문제도 발생하니 주의
         - 사용법: grok {match => {"message" => [grok 정규표현식]}, removed_field => [지우고 싶은 필드명]}
       
       - date 플러그인
       
         - elastic에 데이터가 저장될 때, elastic에 데이터를 보내는 시간이 아닌 실제 로그 파일에 적힌 시간으로 elastic에 적재하기 위해 원하는 field로 재설정 필요
         - 사용법: date {match => {변경할 필드명, 날짜 format}, target =>"@timestamp", timezone => "Asia/Seoul"}
       
       - mutate 플러그인
       
         - 상단의 gsub 외에도 다양한 기능 존재
         - elastic에 logstash에서 파싱한 데이터가 넘어갈 경우, 필드의 타입을 변경해줘야 원하는 타입으로 데이터가 돌아감
         - 데이터 타입을 변경하지 않고 적재하면 무조건 string으로 넘어감
         - 사용법: mutate {convert => [변경할 필드명, 데이터 타입]}
       
       - kv 필터 플러그인
       
         - key "구분자" value 구조의 데이터를 분류하는데 특화
         - 사용법: filter {kv {source => 필드명, field_split => 구분자로 필드 분리, value_split => 구분자로 key value 분리}}
       
         
       
     - output
       - EalsticSearch, Email, ECS, Kafka 등 원하는 저장소에 데이터 전송
       
       - elasticsearch: 이벤트 데이터를 elasticsearch에 전송
       
       - file: 디스크 파일에 기록
       
       - graphite: graphite에 전송 (메트릭을 저장하고 그래프로 작성하는 데 사용되는 오픈 소스 도구)
       
       - statsd: 카운터 및 타이머와 같은 통계를 수신하고 UDP를 통해 전송되며, 하나 이상의 플러그 가능한 백엔드 서비스에 집계를 전송하는 서비스
       
         ```properties
         # 실제로 구성한 내용
         output {
           if "IMP_PRODUCT" in [log][file][path] {
             elasticsearch {
               hosts => ["ip 주소:9200"]
               manage_template => false
               index => "2020-imp-%{[@metadata][beat]}-%{[host][name]}"
             }
           }
           else if "CLICK" in [log][file][path] {
             elasticsearch {
               hosts => ["ip 주소:9200"]
               manage_template => false
               index => "2020-click-%{[@metadata][beat]}-%{[host][name]}"
             }
           }
         }
         ```
       
       - 여러 개의 filebeat에서 하나의 logstash로 보낼 경우, 파일에 따라 다른 인덱스명으로 elastic에 적재를 해야할 경우는 상기와 같이 조건문을 사용하여 다양한 인덱스로 보내줌

​	

------

해야할 일

> corona | weather 로그 수집 시 사용한 output 예제 업로드
>
