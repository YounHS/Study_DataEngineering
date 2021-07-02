__author__ = 'Hyeonsoo Youn'

from bs4 import BeautifulSoup
import requests
import psycopg2
import time

import json
from kafka import KafkaProducer

conn_string = "host='localhost' dbname ='collectData' user='postgres' password='secy'"


# def kafka_pub(highTemperature, lowTemperature, feelTemperature, rainFall, wind, humidity, fineDust, ultraFineDust,
#               ozone, update):
def kafka_pub():
    # producer = KafkaProducer(bootstrap_servers=["localhost:9092"])
    topicName = "weather"
    # msg = {"highTemperature": highTemperature, "lowTemperature": lowTemperature, "feelTemperature": feelTemperature,
    #        "rainFall": rainFall, "wind": wind, "humidity": humidity, "fineDust": fineDust, "ultraFineDust": ultraFineDust,
    #        "ozone": ozone, "update": update}
    msg = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}

    # def on_send_success(record_metadata):
    #     print(record_metadata.topic)
    #     print(record_metadata.partition)
    #     print(record_metadata.offset)

    # def on_send_error(excp):
    #     log.error("error!!!", exc_info=excp)
    print("producer go")
    producer = KafkaProducer(bootstrap_servers=["localhost:9092"], value_serializer=lambda m: json.dumps(msg).encode("utf-8"), api_version=(2, 0, 2))
    print("producer created")
    # producer.send(topicName, {'key': 'value'}).add_callback(on_send_success)
    producer.send(topicName, {'key': 'value'})
    print("producer send")
    producer.flush()
    print("producer flush")
    producer = KafkaProducer(retries=5)


def createDB(conn_string):
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()

    cur.execute("CREATE TABLE realtime_env_naver ("
                "seq SERIAL PRIMARY KEY, "
                "current_temperature TEXT, "
                "high_temperature TEXT, "
                "low_temperature TEXT, "
                "feel_temperature TEXT, "
                "rain_fall TEXT, "
                "windms TEXT, "
                "humidities TEXT, "
                "fine_dust TEXT, "
                "ultra_fine_dust TEXT, "
                "ozone TEXT, "
                "server_update_time TEXT, "
                "creation_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
    conn.commit()


def insertDB(conn_string):
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("INSERT INTO realtime_env_naver(seq,"
                "current_temperature, "
                "high_temperature, "
                "low_temperature, "
                "feel_temperature, "
                "rain_fall, "
                "windms, "
                "humidities, "
                "fine_dust, "
                "ultra_fine_dust, "
                "ozone, "
                "server_update_time) "
                "VALUES (nextval('realtime_env_naver_seq_seq'), %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    currentTemperature, highTemperature, lowTemperature, feelTemperature,
                    rainFall, wind, humidity, fineDust, ultraFineDust, ozone, update))
    conn.commit()
    cur.close()
    conn.close()
    time.sleep(60)


if __name__ == "__main__":
    while 1:
        # html = requests.get('https://n.weather.naver.com/today/02450110')
        #
        # soup = BeautifulSoup(html.text, 'html.parser')
        #
        # currentTemperature = soup.find('strong', {'class': 'current'}).text.replace("현재 온도", '')
        # currentTemperature = currentTemperature.replace('°', '')
        # print('현재온도: ', currentTemperature)
        #
        # temperature = soup.find('strong', {'class': 'temperature'}).text.replace("최저기온", '')
        # temperature = temperature.replace("최고기온", '')
        # temperature = temperature.replace("/", '')
        # highTemperature = temperature.split('°')[0]
        # lowTemperature = temperature.split('°')[1]
        # # highTemperature = highTemperature.replace('°', '')
        # print('최저기온: ', highTemperature)
        #
        # # lowTemperature = soup.find('strong', {'class': 'temperature'}).find('span', {'class': 'blind'})[1].text.replace("최고기온", '')
        # # lowTemperature = temperature.findAll('span')[2].text.replace("최고기온", '')
        # # lowTemperature = lowTemperature.replace('°', '')
        # print('최고기온: ', lowTemperature)
        #
        # feelTemperature = soup.find('dd', {'class': 'desc_feeling'}).text.replace('°', '')
        # print('체감기온: ', feelTemperature)
        #
        # rainFall = soup.find('dd', {'class': 'desc_rainfall'}).text.replace("%", '')
        # print('강수확률: ', rainFall)
        #
        # wind = soup.find('dd', {'class': 'desc_wind'}).text
        # print('바람: ', wind)
        #
        # humidity = soup.find('dd', {'class': 'desc_humidity'}).text.replace('%','')
        # print('습도: ', humidity)
        #
        # liFineDust = soup.find('ul', {'class': 'today_chart_list'})
        # fineDust = liFineDust.findAll('li')[0]
        # fineDust = fineDust.find('strong', {'class': 'value'}).text
        # print('미세먼지: ', fineDust)
        #
        # liUltraFineDust = soup.find('ul', {'class': 'today_chart_list'})
        # ultraFineDust = liUltraFineDust.findAll('li')[1]
        # ultraFineDust = ultraFineDust.find('strong', {'class': 'value'}).text
        # print('초미세먼지: ', ultraFineDust)
        #
        # liOzone = soup.find('ul', {'class': 'today_chart_list'})
        # ozone = liOzone.findAll('li')[2]
        # ozone = ozone.find('strong', {'class': 'value'}).text
        # print('자외선', ozone)
        #
        # update = soup.find('span', {'class': 'title_dsc'}).text.replace(" 업데이트", '')
        # print('최근 업데이트 시각: ', update)

        # kafka_pub(highTemperature, lowTemperature, feelTemperature, rainFall, wind, humidity, fineDust, ultraFineDust, ozone, update)
        kafka_pub()

