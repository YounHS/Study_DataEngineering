# How to Query DSL??
> The way about Query DSL

#### Query DSL

> json 형태로 Query를 생성하여 검색

- **Query Context**: 
  QC에서 사용하는 query절은 해당 document가 query절과 얼마나 잘 일치하는지 _score로 표현
- **Filter Context:** 
  FC에서 사용하는 query절은 해당 document가 query절과 일치하는지 true/false로 표현

1. document 반환 예제

   - example

     ```json
     {
       "query": { 
         "bool": { 
           "must": [
             { 
                 "match": { 
                     "title": "Search" 
                 }
             }, 
             { 
                 "match": { 
                     "content": "Elasticsearch"
                 }
             }  
           ],
           "filter": [ 
             { 
                 "term":  { 
                     "status": "published" 
                 }
             }, 
             { 
                 "range": { 
                     "publish_date": { 
                     	"gte": "2015-01-01"
                     }
                 }
             }
           ]
         }
       }
     }
     ```
     
   - query parameter: Query Context 명시

   - match: Query Context

   - filter parameter: Filter Context 명시

   - term, range: Filter Context




2. Query DSL example

   - match_all/match_none

     ```json
     {
         "query": {
             "match_all": {}
         }
     }
     ```
     
     - match_all
       - 지정된 index의 모든 document 검색
       - 특별한 검색어 없이 모든 document를 get할 때 사용
     - match_none
     
       - 모든 document를 get하고 싶지 않을 때 사용
     
   - match

     ```json
     {
         "query": {
             "match": {
                 "name": "park"
             }
         }
     }
     ```

     - match
       - 기본 필드 검색 쿼리
       - 텍스트, 숫자, 날짜 허용
     - 상단의 경우, name에 park이라는 문자열이 있는 모든 document를 조회
     
   - bool

     ```json
     {
         "query": {
             "bool": {
                 "must": [
                     { 
                         "match": { 
                             "age": "21" 
                         } 
                     }
                 ],
                 "must_not": [
                     { 
                         "match": { 
                             "state": "Seoul" 
                         } 
                     }
                 ]
             }
         }
     }
     ```

     - bool(True/False) 로직을 사용하는 query
     - bool query 종류
       - must: 지정된 모든 query가 일치하는 document 조회
       - should: 지정된 모든 query 중 하나라도 일치하는 document 조회
       - must_not: 지정된 모든 query가 모두 일치하지 않는 document 조회
       - filter: must처럼 filter 절에 지정된 모든 query가 일치하는 document 조회, Filter Context에서 실행되기 때문에 score 무시
     - 상단의 경우, 나이가 21세이고, 서울에 살지 않는 document를 조회하는 예제

   - filter

     - document가 검색 query와 일치하는지 나타내는 _score 값을 계산하지 않도록 query 실행을 최적화

   - range

     ```json
     {
         "query": {
             "bool": {
                 "must": { 
                     "match_all": {} 
                 },
                 "filter": {
                     "range": {
                         "balance": {
                             "gte": 15000,
                             "lte": 20000
                         }
                     }
                 }
             }
         }
     }
     ```

     - 범위를 지정하여 범위에 해당하는 값을 갖는 document 조회
     - range query에서 범위 지정을 위한 파라미터
       - gte: 이상
       - gt: 초과
       - lte: 이하
       - lt: 미만
       - boost: query의 boost 값을 세팅 (default: 1.0)
         - boost -> 검색에 가중치를 부여하는 것
     - 상단의 경우, 잔액이 15000~20000인 범위에 속하는 document를 조회하는 예제
