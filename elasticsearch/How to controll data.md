# How to control Data??
> The way about control Data

#### Control Data

1. 입력(Post) 전, 데이터가 존재하는지 확인

   - 존재여부 확인

     ```bash
     curl -XGET http://localhost:9200/classes
     ```
     
   - 결과를 아름답게 확인가능

     ```bash
     curl -XGET http://localhost:9200/classes?pretty
     ```
     

   

2. 1의 결과 404 출력 시, 해당 인덱스가 없으므로 인덱스 새로 생성

   - 인덱스 생성

     ```bash
     curl -XPUT http://localhost:9200/classes
     ```
     
   - 인덱스 생성 확인

     ```bash
     curl -XGET http://localhost:9200/classes
     ```
     



3. 인덱스 제거 절차

   - 인덱스 제거

     ```bash
     curl -XDELETE http://localhost:9200/classes
     ```

   - 인덱스 제거 확인

     ```bash
     curl -XGET http://localhost:9200/classes
     ```

     

4. document 생성 방법

   - document는 index가 있을 때 만들어도 되고, 없을 때도 index명과 type명을 명시해주면 바로 document 생성 가능

     ```bash
     curl -XPOST http://localhost:9200/classes/class/1/ -d '{"title":"Algorithm", "professor":"John"}'
     ```

   - document가 파일에 저장되어 있을 경우 (항상 커맨드에 입력 불가능)

     ```bash
     curl -XPOST http://localhost:9200/classes/class/1/ -d @<파일명.json>
     ```

     