# How to mapping data?
> The way about mapping Elasticsearch Data

#### Mapping Data

> 매핑은 RDB에서 스키마 개념과 동일
>
> 매핑없이 Elasticsearch에 데이터 삽입은 매우 위험
>
> 데이터 관리 시, 매핑을 먼저 추가하고, 데이터가 이미 존재할 시, 매핑을 추후에 추가하여 분석이나 시각화할 때 사용 가능

1. 매핑 지정하는 방법

   - 매핑 지정방법 (geo_point의 경우, 해당 타입을 시각화툴을 이용하면 지도 상에 바로 위치 표시 가능)

     ```json
     {
     	"class": {
     		"properties": {
     			"title": {"type": "string"},
     			"professor": {"type": "string"},
     			"student_count": {"type": "integer"},
     			...,
     			"submit_data": {"type": "date", "format": "yyyy-MM-dd"},
     			"school_location": {"type": "geo_point"}
     		}
     	}
     }
     ```
     

   

2. 매핑을 지정할 인덱스 1개 생성

   - XPUT을 사용하여 생성

     ```bash
     curl -XPUT http://localhost:9200/mapping
     ```
     
   - XGET을 사용하여 확인 (mapping 영역이 비어있는 것을 확인)

     ```bash
     curl -XGET http://localhost:9200/mapping?pretty
     ```
     



3. 매핑 지정

   - XPUT을 사용하여 매핑 지정

     ```bash
     curl -XPUT http://localhost:9200/mapping/class/_mapping -d @/home/elasticsSearch/test/mappingTest.json
     ```

   - XGET을 사용하여 확인 (이런식으로 mapping 영역 지정 시, aggregation이나 시각화 시, 적절한 결과 도출 가능)

     ```bash
     curl -XGET http://localhost:9200/mapping?pretty
     ```

     

4. bulk 기능을 사용하여 데이터 입력

   - XPOST를  사용하여 해당 인덱스에 데이터 입력

     ```bash
     curl -XPOST http://localhost:9200/_bulk?pretty --data-binary @/home/elasticSearch/test/bulk.json
     ```

   - XGET을 사용하여 확인

     ```bash
     curl -XGET http://localhost:9200/classes/class/1/?pretty
     ```

     