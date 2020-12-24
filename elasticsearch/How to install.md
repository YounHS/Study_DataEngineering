# How to install Elasticsearch?
> The way about install Elasticsearch

#### Install process

1. java 8 install

   - Elasticsearch는 jvm 위에서 구동

     ```bash
     sudo add-apt-repository -y ppa:webupd8team/java
     sudo apt-get update
     sudo apt-get -y install oracle-java8-installer
     ```

   - add-apt-repository가 동작하지 않는다면 하단의 명령어를 실행하여 관련 패키지 설치

     ```bash
     sudo apt-get install python-software-properties
     sudo apt-get install software-properties-common
     ```

     

2. ElasticSearch install

   - first, wget!

     ```bash
     wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.3.1.deb
     dpkg -i elasticsearch-5.1.1.deb
     ```

   - 설치 경로: /usr/share/elasticsearch

   - 설정파일 경로: /etc/elasticsearch

   - 스크립트 파일: /etc/init.d/elasticsearch

   - 자동 재시작

     ```bash
     sudo systemctl enable elasticsearch.service
     ```

   - elasticsearch 작동여부 확인

     ```bash
     service elasticsearch start
     service elasticsearch
     curl -XGET 'localhost:9200'
     ```


