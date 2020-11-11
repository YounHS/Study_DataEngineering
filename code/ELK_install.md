# How to install ELK?
### Elasticsearch install

> Ubuntu 18.04 를 기준

1. Elasticsearch 다운로드

```bash
dpkg -i elasticsearch-7.6.2-amd64.deb
```

​		[다운로드 링크](https://www.elastic.co/kr/downloads/elasticsearch)에서 DEB을 다운로드 후, 상단 명령어로 설치 진행



2. 방화벽 설정

```bash
firewall-cmd --permanent --zone=public --add-port=9200/tcp
firewall-cmd --reload
firewall-cmd --list-ports
```

​		elasticsearch의 경우, 9200 port를 허용해야하므로 상단 명령어로 방화벽 설정



> Elasticsearch 실행 전, 하단의 생성 경로 확인
>
> - /usr/share/elasticsearch
> - /etc/elasticsearch
> - /etc/init.d/elasticsearh



3. Elasticsearch service start

```bash
service elasticsearch start
```



> ```bash
> curl -XGET 127.0.0.1:9200
> ```
>
> 상단의 명령어를 통해 설치가 정상적으로 진행되었는지 확인



4. 외부 접속 허용

```bash
sudo -i
vi /etc/elasticsearch/elasticsearch.yml
```

- 상단의 파일에서 `network.host:192.168.0.1` 을 `network.host:0.0.0.0` 으로 변경
- `cluster.initial_master_nodes` 의 주석 제거



5. Elasticsearch service 재가동

```bash
service elasticsearch restart
```

​		상단의 명령어로 Elasticsearch service를 재가동한 후, 
​		웹 주소창에 http://<ip address>:9200 을 입력하여 정상작동 확인

------

### Kibana install

> Ubuntu 18.04 를 기준

1. Kibana 다운로드

```bash
dpkg -i kibana-7.6.2-amd64.deb
```

​		[다운로드 링크](https://www.elastic.co/kr/downloads/kibana)에서 DEB을 다운로드 후, 상단 명령어로 설치 진행



2. 방화벽 설정

```bash
firewall-cmd --permanent --zone=public --add-port=5601/tcp
firewall-cmd --reload
firewall-cmd --list-ports
```

​		kibana의 경우, 5601 port를 허용해야하므로 상단 명령어로 방화벽 설정



3. 외부 접속 허용

```bash
sudo -i
vi /etc/kibana/kibana.yml
```

- 상단의 파일에서 `server.host:'localhost'` 을 `server.host:0.0.0.0` 으로 변경
- `elasticsearch.hosts` 의 주석 제거



4. Kibana service start

```bash
service kibana start
```



> ```bash
> service kibana status
> ```
>
> 정상적으로 kibana가 구동중인지 확인



​		이후, 웹 주소창에 http://localhost:5601 을 입력하여 정상작동 확인

------

### Logstash install

> Ubuntu 18.04 를 기준

1. Logstash 다운로드

```bash
dpkg -i logstash-7.6.2.deb
```

​		[다운로드 링크](https://www.elastic.co/kr/downloads/logstash)에서 DEB을 다운로드 후, 상단 명령어로 설치 진행



2. Logstash test를 위한 .conf 파일 생성

```bash
vi test.conf
```

​		하단의 내용으로 세팅

```json
input {
    stdin {}
}
output {
    stdout {}
}
```



3. Logstash start

```bash
sudo /usr/share/logstash/bin/logstash -f ./test.conf
```

​		원하는 경로에 있는 .conf 파일과 상단의 명령어를 통해 Logstash 실행

------

해야할 일

> Logstash .conf를 수정하여 실시간 데이터 subscribe 해보기