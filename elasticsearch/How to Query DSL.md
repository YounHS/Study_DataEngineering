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
