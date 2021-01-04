# How to search Data??
> The way about search Data

#### Search Data

1. 검색 API

   - _search

     ```bash
     curl -XGET http://localhost:9200/classes/class/_all/_search?pretty
     ```
     
   - _search: 검색 작업을 수행하는 액션

   - 검색 방법에 대한 조건(Query)들을 명시하여 원하는 정보 필터링 가능

   - 조건 전달 방법

     - URI search: URL에 파라미터 넘기기
     - Query DSL: query를 작성한 json 파일을 POST로 넘기기 (이 방법이 깔끔하다고 함!)

   

2. URI search

   - age 조건이 20살인 document만 조회

     ```bash
     curl -XGET http://localhost:9200/classes/class/_search?q=age:20&pretty
     ```
     
   - 파라미터 q: query string

   - sort, from, size 옵션 등이 존재 ([파라미터 정보 확인](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html))

   - response 결과 분석

     - took: 검색 소요 시간 (ms)
     - timed_out: 검색 시, 초과된 시간 여부
     - _shards: 검색한 shard 갯수 및 검색에 성공/실패한 shard 갯수
     - hits: 검색 결과에 해당하는 데이터들 (default: 10, size로 조절 가능)
       - _score: 해당 document가 지정된 검색 query와 얼마나 일치하는지 상대적으로 나타내는 숫자 값 (높을수록 고관련성)
     - sort: 결과 정렬 방식 (default: desc, 다른 항목일 경우: asc, _score 기준일 경우 노출되지 않음)