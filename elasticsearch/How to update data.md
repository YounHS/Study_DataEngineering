# How to update Data??
> The way about update Data

#### Update Data

1. 업데이트할 document 생성

   - XPOST로 등록

     ```bash
     curl -XPOST http://localhost:9200/classes/class/1/ -d '{"title":"Algorithm", "professor":"John"}'
     ```
     
   - XGET으로 확인

     ```bash
     curl -XGET http://localhost:9200/classes/class/1?pretty
     ```
     

   

2. 생성한 document 수정

   - XPOST로 document 수정

     ```bash
     curl -XPOST http://localhost:9200/{index}/{type}/{doc_id}/_update -d '{update 명령어}'
     
     curl -XPOST http://localhost:9200/classes/class/1/_update?pretty -d '{"doc":{"unit":1}}'
     ```
     
   - XGET으로 업데이트한 document 확인

     ```bash
     curl -XGET http://localhost:9200/classes/class/1?pretty
     ```
     
   - 스크립트를 이용한 업데이트 방법

     ```bash
     curl -XPOST http://localhost:9200/classes/class/1/_update?pretty -d '{"script":"ctx._source.unit+=5"}'
     ```
     