# What the Elasticsearch??
> Apache Lucene 기반의 분산 검색 엔진으로 텍스트, 숫자, 위치 기반 정보, 정형 및 비정형 데이터 등 모든 유형의 데이터를 위한 분산형 오픈 소스 검색 및 분석 엔진

#### Elasticsearch

- 데이터 수집, 보강, 저장, 분석, 시각화를 위한 오픈 소스 도구 모임인 Elastic Stack의 중심 구성 요소

- 단독으로 사용되기 보다는 Logstash, Kibana와 함께 사용

- Elasticsearch, Logstash, Kibana를 줄여 ELK Stack이라 명명

- 많은 기본 코덱이 처리 과정을 단순화

- Elastic Stack에는 데이터를 Elasticsearch로 전송하기 위한 경량의 데이터 수집 에이전트들이 제공되는 컬렉션인 Beats가 포함되어 있으며, 이를 이용하여 빅데이터를 실시간 분석 가능




1. 사용예시

   - 어플리케이션 검색
   - 웹 사이트 검색
   - 엔터프라이즈 검색
   - 로깅과 로그 분석
   - 인프라 매트릭과 컨테이너 모니터링
   - 어플리케이션 성능 모니터링
   - 위치 기반 정보 데이터 분석 및 시각화
   - 보안 분석
   - 비즈니스 분석




2. 작동원리

   - 로그, 시스템 매트릭, 웹 어플리케이션 등 다양한 소스로부터 Raw data가 Elasticsearch로 유입
   - 데이터 수집은 Raw data가 Elasticsearch에서 indexing되기 전, 구문분석, 정규화, 강화되는 프로세스
   - Elasticsearch에서 색인이 진행되면, 사용자는 이 데이터에 대해 쿼리를 실행하고 집계를 사용해 데이터의 복잡한 요약 검색 가능
   



3. Indexing

   - Elasticsearch Index는 서로 관련된 문서들의 모음
   - 각 문서는 일련의 key와 value를 서로 연결
   - Elasticsearch는 JSON 형식으로 데이터 저장
   - Elasticsearch는 반전된 인덱스라고 하는 데이터 구조 사용, 이로 인해 텍스트 검색 시간 단축 가능
   - 반전된 인덱스는 문서에 나타나는 모든 고유한 단어의 목록을 생성하고, 각 단어가 발생하는 모든 문서를 식별
   - 색인된 프로세스 중, Elasticsearch는 문서를 저장하고 반전된 인덱스를 구축하여 거의 실시간으로 문서 검색이 가능한 데이터로 변환
   - 인덱스 API를 사용하여 색인이 진행, 이를 통해 사용자는 특정한 인덱스에서 JSON 문서를 추가하거나 업데이트 가능

   

4. 장점

   - 속도
     - Lucene 기반의 구축으로 전체 텍스트 검색에 뛰어나며 문서가 색인될 때부터 검색이 가능해질 때까지의 대기 시간이 매우 짧아 실시간 검색 플랫폼과 거의 유사
   - 분산성
     - Elasticsearch에 저장된 문서는 shard(샤드)라는 다른 컨테이너에 분산
     - 샤드는 복제되어 하드웨어 장애 시, 중복되는 데이터 사본 제공
     - Elasticsearch의 분산적인 특징은 다수의 서버까지 확장하고 petabyte의 데이터 처리가 가능하도록 서포트
   - 넓은 범위의 기능 세트 제공
     - 데이터의 roll-up, 인덱스 수명 주기 관리 등과 같이 데이터를 훨씬 효율적으로 저장하고 검색할 수 있게 해주는 강력한 기본 기능이 다수 탑재
   - 데이터 수집, 시각화, 보고의 간소화
     - Beats, Logstash의 통합을 통해 Elasticsearch로 색인하기 전, 데이터를 훨씬 더 쉽게 처리가 가능
     - Kibana를 통해 데이터의 실시간 시각화 작업 진행 가능
     - UI를 통해 어플리케이션 성능 모니터링, 로그, 인프라 매트릭 데이터에 신속한 접근 가능

   

5. 지원 프로그래밍 언어

   - JAVA
   - Node.js
   - Go
   - .NET(C#)
   - PHP
   - Perl
   - Python
   - Ruby

​	

------

해야할 일

> - [ ] read -> How to BULK
> - [ ] read -> How to Manufacture search result
> - [x] read -> How to Mapping data
> - [ ] read -> How to Query DSL
> - [x] read -> How to controll data
> - [x] read -> How to search data
> - [x] read -> How to update data

