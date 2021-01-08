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
     
