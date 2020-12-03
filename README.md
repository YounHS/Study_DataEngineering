# Data Engineer Study
1. Kafka Download

   ```bash
   $ wget http://apache.mirror.cdnetworks.com/kafka/2.4.1/kafka_2.12-2.4.1.tgz
   kafka_2.12-2.4.1.tgz         100%[==============================================>]  59.47M  7.80MB/s    in 7.7s
   
   $ tar -xzf kafka_2.12-2.4.1.tgz
   $ cd kafka_2.12-2.4.1
   ```




2. python-kafka Download

   ```bash
   pip install kafka-python
   ```

   만약 python에서 kafka를 사용해야한다면 상단처럼 pip를 통해 패키지를 받자.



3. chromedriver Download

   먼저, 'chrome' 을 실행한 후, '도움말' -> 'Chrome 정보'를 클릭하여, 사용중인 크롬 버전을 확인한다. 

   그리고, [링크](https://sites.google.com/a/chromium.org/chromedriver/downloads)를 클릭하여 자신에게 맞는 버전의 chromedriver를 다운로드 받는다.

   물론 windows이니, 'chromedriver_win32.zip' 을 받아야한다.

   그리고 압축을 풀어주고 사용하면 된다. 하단은 python에서 chromedriver를 사용할 때의 예이다.

   ```python
   driver = webdriver.Chrome('C:\chromedriver.exe')
   ```

   

------

해야할 일

> virtualenv 및 conda 활용법 정리 (아 굉장히 좋더라)