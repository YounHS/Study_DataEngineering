# How to Manufacture search result??
> The way about Manufacture search result

#### Manufacture search result

1. from, size

   - example

     ```json
     {
         "from" : 0,
         "size" : 5,
         "query":{
             "match_all":{}
         }
     }
     ```
     
     - pagination 과 관련됨
     
       - ex) 게시판 페이징 시, 쪽 수는 from, size는 한 번에 보여줄 게시글의 수
     - from, size query는 index setting인 index.max_result_window에 설정된 값 초과 불가능
       - 해당 설정의 default 값은 10000이기에 최대 10000개의 document 호출 가능하고, 그 이상을 호출하려면 scroll API 사용 필요
     - 상단의 경우, 5개의 document만 반환하도록 조회하는 예제




2. sort

   - example

     ```json
     {
         "sort" : [
             { 
                 "age" : "desc" 
             },
             { 
                 "balance" : "desc" 
             },
             "_score"
         ],
         "query":{
             "match_all":{}
         }
     }
     ```
     
     - 특정 필드마다 하나 이상의 정렬 추가 가능
     - 사용하지 않을 경우, default는 _score 내림차순이며, 다른 항목으로 정렬할 경우, 오름차순이 default 값으로 설정됨
     - 상단의 경우, age 필드에 대해 내림차순으로 정렬한 후, balance 필드에 대해 내림차순으로 정렬하고 _score를 내림차순으로 정렬하는 예제
     



3. source filtering

   - no response example

     ```json
     {
         "_source": false,
         "query":{
             "match_all":{}
         }
     }
     ```

   - response only name, age example

     ```json
     {
         "_source": [
             "name","age"
         ],
         "query":{
             "match_all":{}
         }
     }
     ```

     - 검색된 데이터에서 특정 필드들만 반환 가능
     - SQL의 select query 시, 특정 컬럼들을 명시하는 것과 유사
     - 검색된 document의 총 갯수를 알고 싶은 경우, _source를 노출시키지 않음으로써 성능 향상 가능
     - *를 사용하여 필드명 명시, includes/excludes를 통해 필드를 포함 및 제외 가능



4. aggregations

   - name에 kim이 포함된 document들의 balance 필드 값들을 평균 내는 예제

     ```json
     {
         "query": {
             "term": {
                 "name" : "kim"
             }
         },
         "aggs" : {
             "avg_balance_test" : {
                 "avg" : {
                     "field" : "balance"
                 }
             }
         }
     }
     ```

     - 집계를 의미하며 aggs 필드를 통해 document 갯수 통계내기 가능
     - SQL의 group by 와 유사
     - **avg_balance_test**: response 데이터에 명시될 통계 결과 필드명을 의미. 원하는 명칭으로 작성
     - **avg**: 집계 타입을 의미. sum, cardinality 등 여러가지 존재
     - **field**: 어떤 필드에 대해 통계 낼 것인지 명시. 상기 예제에서는 balance 필드에 대해 집계