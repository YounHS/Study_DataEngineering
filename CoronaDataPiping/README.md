# CoronaDataPiping (CDP)
1. 개요

   코로나로 인해 팬데믹이 선언된 이후, 도무지 현 상황이 나아질 기미가 보이지 않아, 국내의 코로나 관련 다양한 관측값, 더 나아가 전세계의 코로나 관련 다양한 관측값을 추출하여 데이터를 시각화해보기 위해 시작한다. 향후, 동시간대의 타 데이터와 머징하여 다양한 변수들 간의 상관관계를 도출하여 유의미한 분석까지 하는 것을 본 프로젝트의 목표로 한다.
   
   **(picture에서 EcoSys를 EcoSys2로 교체. 기왕 kafka 사용하니까 windows에서는 wordometer를 통한 코로나 데이터, Ubuntu에서는 CoronaBoard를 통한 코로나 데이터를 실시간 수집해보기로 함.)**
   
   **([2020.12.08] EcoSystem 그림을 또다시 교체함... EcoSys2처럼 진행하려면 windows에서도 zookeeper와 kafka broker를 따로 구축한 후, 진행할 수 있는 것으로 확인했기 때문에... 하... 이 부분은 좀 더 공부가 필요할 거 같으며, 우선은 EcoSys3 그림처럼 진행키로 한다.)**



![CDP_EcoSystem](https://github.com/YounHS/Study_DataEngineering/blob/main/CoronaDataPiping/Picture/EcoSys3.png)



2. 관련 스터디

   2.1 ELK 환경 구축

   (자세한 내용은 지속적으로 추가할 예정)

   이전에, Naver 날씨 페이지에서 웹 크롤링하여 데이터 파이핑을 한 적이 있었다. 그리고 현재, 새로운 페이지를 크롤링하는 김에 logstash의 input, filter, output 관련 conf 파일을 새롭게 세팅하여 kibana index pattern 또한 새롭게 시작하려 했다. 음... 그런데 무슨 짓을 해도 kibana에 새롭게 세팅한 index pattern이 뜨지 않는 문제가 발생했다. 처음엔 단순히 zookeeper도 재시작해야하는 줄 알았지만... 그걸로 해결되지 않았다. 몇 십분 구글링하다가 문득 하단 링크의 ELK_install.md에 적어놨던 내용이 떠올랐다. kafka-console-consumer를 구동할 때 맨 마지막 인자로 '--from-beginning' 인자를 적어주면 offset를 리셋하여 새롭게 메시지를 가져온다는 내용이었다. 후.... 역시... 그렇게 진행하니까 바로 kibana에 제대로 index-pattern이 뜨는 것을 확인할 수 있었다. 
   
   
   
   ![corona_index_pattern](https://github.com/YounHS/Study_DataEngineering/blob/main/CoronaDataPiping/Picture/corona_index_pattern_show.png)
   
   
   
   어... 근데... 이게 업데이트가 초 단위로 되는게 아니라 관측값의 변동이 있을 때만 업데이트 하는 것으로 확인되었다... 그래서 시각화를 해보니까 음.... 하단의 캡쳐화면처럼 비쥬얼적으로 좀... 가오가 없다... 뭔가 가오가 필요한 듯 싶다.
   
   **(Windows10(로컬)으로 worldometer를 크롤링하는데, 이건 자주 업데이트되서 뭔가 이쁜 그래프가 나올 것으로 예상됨. 설렘. 기쁨.)**
   
   
   
   ![corona_index_pattern](https://github.com/YounHS/Study_DataEngineering/blob/main/CoronaDataPiping/Picture/less_data_input.png)
   
   
   
   [링크 클릭 후, ELK_install.md 파일 참고](https://github.com/YounHS/Study_DataEngineering/tree/main/code)



​		2.2 Kafka 환경 구축

​		(자세한 내용은 지속적으로 추가할 예정)

```python
import json
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=["localhost:9092"])
topicName = "test"
# msg = {"id":"test", "tel":"010-1234-5678", "regDate":"20201109"}

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

producer = KafkaProducer(value_serializer=lambda m: json.dumps(msg).encode("ascii"))
producer.send(topicName, {'key':'value'}).add_callback(on_send_success)

producer.flush()

producer = KafkaProducer(retries=5)
```

​		상단처럼 Kafka가 돌아가는 서버의 IP, 포트를 설정하고, topic 이름을 kafka에서 설정한 topic 이름과 같게 세팅해준다. 이렇게 세팅을 해줌으로써, CoronaBoard 웹에서 크롤링한 데이터를 실시간으로 분산처리하여 ELK (Logstash)와 연동할 수 있게 된다. kakfa 서버 및 토픽 세팅에 관련한 설정은 하단의 링크를 참고하면 된다.

​		[링크 클릭 후, README.md 파일 참고](https://github.com/YounHS/Study_DataEngineering/tree/main/code)



3. 실험에 사용한 자료

   3.1 CoronaBoard (유용히 잘 사용하겠습니다.)

   [실시간 코로나 상황](https://coronaboard.kr/)

   수집하는 데이터는 하단과 같다.

   - 전세계

     - 확진자
     - 사망자
     - 격리해제
     - 치명률
     - 발생국

     

   - 대한민국

     - 확진자
     - 사망자
     - 격리해제
     - 치명률
     - 총검사자
     - 검사중
     - 결과음성



​		3.2 Worldometer

​		전세계적인 코로나 데이터를 보여주는 사이트이다. 3.1의 coronaboard보다 조금 더 업데이트가 많이 이루어져 시각화 시, 아름다운 그래프를 볼 수 있을 것으로 보인다. 우선 worldometer로 전세계적인 코로나 데이터를 수집하였다[2020.12.08]. 이제 이 수집한 데이터를 VirtualBox의 Ubuntu 상의 kafka 서버로 publish할 것이다. 후.... 일단 coronaboard랑 같은 토픽을 사용할 것이라서..... 키 값 중복이 이루어지지 않도록 확인해야한다.



​		3.3 Selenium

​		웹 크롤링이 필요한데, 지금까지 썼던 bs4의 경우, 어떠한 방법을 써도 동적으로 변화하는 데이터를 랜더링하는 웹 데이터를 크롤링할 수 없어서 애를 먹고 있었다. Selunium의 경우 Chrome driver를 통해 time.sleep() 같은 함수나 명시적/암묵적 함수를 설정할 수 있어, 이러한 동적 데이터를 랜더링하는 웹의 경우에도 데이터를 수집할 수 있다는 장점이 있어서 Selenium을 사용해보았다.

```python
def linux_selenium():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

    count = True
    saveUpdated = ''

    while 1:
        driver.get('https://coronaboard.kr/')
        time.sleep(10)

        nowUpdated = driver.find_element_by_xpath("//span[@id='last-updated']").text

        worldConfirmedCase = driver.find_element_by_xpath(
            "//div[normalize-space(@class)='row dashboard world']//div[1]/p[1]").text.replace(',', '')
```

​		[리눅스에서 selenium 사용 환경 만들기](https://github.com/YounHS/Study_DataEngineering/tree/main/code/python/Corona)	

​		리눅스 환경의 경우 상단의 링크에서 README.md 파일을 참고하여 selenium을 사용할 수 있는 환경을 만들어야한다. 그 후, 상단 코드를 참고하여 웹 크롤링을 할 수 있도록 한다.

```python
def windows_selenium():
    driver = webdriver.Chrome('C:\chromedriver.exe')

    count = True
    saveUpdated = ''

    while 1:
        driver.get('https://coronaboard.kr/')
        time.sleep(10)

        nowUpdated = driver.find_element_by_xpath("//span[@id='last-updated']").text

        worldConfirmedCase = driver.find_element_by_xpath(
            "//div[normalize-space(@class)='row dashboard world']//div[1]/p[1]").text.replace(',', '')
```

​		상단의 코드는 windows 환경에서 selenium을 사용할 때 웹 크롤링을 할 수 있도록 하는 코드이다. windows의 경우, 하단 링크의 README.md를 참고하여 chromedriver를 다운로드 받아 웹 크롤링이 가능한 환경을 만들어준다.

​		[windows에서 웹 크롤링 환경 만들기](https://github.com/YounHS/Study_DataEngineering)