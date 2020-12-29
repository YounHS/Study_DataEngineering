# How to Bulk?
> The way about Elasticsearch Bulk

#### Elasticsearch Bulk

> Bulk: 여러 개의 document를 한번에 Elasticsearch에 삽입하는 방법

1. bulk.json이라는 bulk 파일을 삽입

   - XPOST로 삽입

     ```bash
     curl -XPOST http://localhost:9200/_bulk?pretty --data-binary @/home/elasticSearch/test/bulk.json
     ```
     
   - XGET으로 확인

     ```bash
     curl -XGET http://localhost:9200/classes/class/1?pretty
     curl -XGET http://localhost:9200/classes/class/2?pretty
     ```
     
