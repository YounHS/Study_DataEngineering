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

해야할 일

> Kibana 설치