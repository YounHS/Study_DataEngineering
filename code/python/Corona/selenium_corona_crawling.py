__author__ = 'Hyeonsoo Youn'

from bs4 import BeautifulSoup
from selenium import webdriver
from kafka import KafkaProducer

import psycopg2
import time
import json
import datetime

conn_string = "host='localhost' dbname ='collectData' user='postgres' password='secy'"


def kafka_pub(wo_saveUpdated, wo_CoronavirusCase, wo_DeathNum, wo_RecoveredNum, wo_ActiveCase,
              wo_ActiveMildCondition, wo_ActiveSeriousCritical, wo_ClosedCase, wo_ClosedRecoverdDischarged,
              wo_ClosedDeath):
    now = datetime.datetime.now()
    nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
    producer = KafkaProducer(bootstrap_servers=["211.194.13.200:9092"])
    topicName = "corona"
    msg = {"wo_saveUpdated": wo_saveUpdated, "wo_CoronavirusCase": int(wo_CoronavirusCase), "wo_DeathNum": int(wo_DeathNum),
           "wo_RecoveredNum": int(wo_RecoveredNum), "wo_ActiveCase": int(wo_ActiveCase),
           "wo_ActiveMildCondition": int(wo_ActiveMildCondition), "wo_ActiveSeriousCritical": int(wo_ActiveSeriousCritical),
           "wo_ClosedCase": int(wo_ClosedCase), "wo_ClosedRecoverdDischarged": int(wo_ClosedRecoverdDischarged),
           "wo_ClosedDeath": int(wo_ClosedDeath), "insertTime": nowDateTime}

    def on_send_success(record_metadata):
        print(record_metadata.topic)
        print(record_metadata.partition)
        print(record_metadata.offset)

    # def on_send_error(excp):
    #     log.error("error!!!", exc_info=excp)

    producer = KafkaProducer(value_serializer=lambda m: json.dumps(msg).encode("ascii"))
    producer.send(topicName, {'key': 'value'}).add_callback(on_send_success)

    producer.flush()

    producer = KafkaProducer(retries=5)


def createDB():
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()

    cur.execute("CREATE TABLE realtime_env_naver ("
                "seq SERIAL PRIMARY KEY, "
                "current_temperature TEXT, "
                "high_temperature TEXT, "
                "low_temperature TEXT, "
                "feel_temperature TEXT, "
                "time_rain_fall TEXT, "
                "fine_dust TEXT, "
                "ultra_fine_dust TEXT, "
                "ozone TEXT, "
                "server_update_time TEXT, "
                "creation_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
    conn.commit()
    cur.close()
    conn.close()


def insertDB():
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()

    cur.execute("INSERT INTO realtime_env_naver(seq,"
                "current_temperature, "
                "high_temperature, "
                "low_temperature, "
                "feel_temperature, "
                "time_rain_fall, "
                "fine_dust, "
                "ultra_fine_dust, "
                "ozone, "
                "server_update_time) "
                "VALUES (nextval('realtime_env_naver_seq_seq'), %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    currentTemperature, highTemperature, lowTemperature, feelTemperature,
                    timeRainFall, fineDust, ultraFineDust, ozone, update))
    conn.commit()
    cur.close()
    conn.close()


def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('C:\chromedriver.exe', chrome_options=chrome_options)

    count = True
    wo_saveUpdated = ''

    while 1:
        # driver.implicitly_wait(5)
        # headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
        driver.get('https://www.worldometers.info/coronavirus/')
        time.sleep(5)

        nowUpdated = driver.find_element_by_xpath("//div[normalize-space(@class)='content-inner']//div[2]").text

        if count or len(saveUpdated) == 0:
            wo_CoronavirusCase = driver.find_element_by_xpath(
                "//div[normalize-space(@class)='content-inner']//div[4]/div[1]/span[1]").text.replace(',', '')
            wo_DeathNum = driver.find_element_by_xpath(
                "//div[normalize-space(@class)='content-inner']//div[6]/div[1]/span[1]").text.replace(',', '')
            wo_RecoveredNum = driver.find_element_by_xpath(
                "//div[normalize-space(@class)='content-inner']//div[7]/div[1]/span[1]").text.replace(',', '')
            wo_ActiveCase = driver.find_element_by_xpath(
                "//div[normalize-space(@class)='content-inner']//div[9]/div[1]/div[2]/div[1]/div[1]/div[1]").text.replace(
                ',', '')
            wo_ActiveMildCondition = driver.find_element_by_xpath(
                "//div[normalize-space(@class)='content-inner']//div[9]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[1]").text.replace(
                ',', '')
            wo_ActiveSeriousCritical = driver.find_element_by_xpath(
                "//div[normalize-space(@class)='content-inner']//div[9]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/span[1]").text.replace(
                ',', '')
            wo_ClosedCase = driver.find_element_by_xpath(
                "//div[normalize-space(@class)='content-inner']//div[10]/div[1]/div[2]/div[1]/div[1]/div[1]").text.replace(
                ',', '')
            wo_ClosedRecoverdDischarged = driver.find_element_by_xpath(
                "//div[normalize-space(@class)='content-inner']//div[10]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[1]").text.replace(
                ',', '')
            wo_ClosedDeath = driver.find_element_by_xpath(
                "//div[normalize-space(@class)='content-inner']//div[10]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/span[1]").text.replace(
                ',', '')

            wo_saveUpdated = nowUpdated
            print(wo_saveUpdated)
            print('\n\n전세계 상황')
            print(wo_CoronavirusCase)
            print(wo_DeathNum)
            print(wo_RecoveredNum)
            print(wo_ActiveCase)
            print(wo_ActiveMildCondition)
            print(wo_ActiveSeriousCritical)
            print(wo_ClosedCase)
            print(wo_ClosedRecoverdDischarged)
            print(wo_ClosedDeath)
            kafka_pub(wo_saveUpdated, wo_CoronavirusCase, wo_DeathNum, wo_RecoveredNum, wo_ActiveCase,
                      wo_ActiveMildCondition, wo_ActiveSeriousCritical, wo_ClosedCase, wo_ClosedRecoverdDischarged,
                      wo_ClosedDeath)
            count = False
        else:
            # 여기서부터 새롭게 업데이트된 데이터 받아오기
            if (nowUpdated != '-') and (wo_saveUpdated != nowUpdated):
                wo_CoronavirusCase = driver.find_element_by_xpath(
                    "//div[normalize-space(@class)='content-inner']//div[4]/div[1]/span[1]").text.replace(',', '')
                wo_DeathNum = driver.find_element_by_xpath(
                    "//div[normalize-space(@class)='content-inner']//div[6]/div[1]/span[1]").text.replace(',', '')
                wo_RecoveredNum = driver.find_element_by_xpath(
                    "//div[normalize-space(@class)='content-inner']//div[7]/div[1]/span[1]").text.replace(',', '')
                wo_ActiveCase = driver.find_element_by_xpath(
                    "//div[normalize-space(@class)='content-inner']//div[9]/div[1]/div[2]/div[1]/div[1]/div[1]").text.replace(
                    ',', '')
                wo_ActiveMildCondition = driver.find_element_by_xpath(
                    "//div[normalize-space(@class)='content-inner']//div[9]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[1]").text.replace(
                    ',', '')
                wo_ActiveSeriousCritical = driver.find_element_by_xpath(
                    "//div[normalize-space(@class)='content-inner']//div[9]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/span[1]").text.replace(
                    ',', '')
                wo_ClosedCase = driver.find_element_by_xpath(
                    "//div[normalize-space(@class)='content-inner']//div[10]/div[1]/div[2]/div[1]/div[1]/div[1]").text.replace(
                    ',', '')
                wo_ClosedRecoverdDischarged = driver.find_element_by_xpath(
                    "//div[normalize-space(@class)='content-inner']//div[10]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/span[1]").text.replace(
                    ',', '')
                wo_ClosedDeath = driver.find_element_by_xpath(
                    "//div[normalize-space(@class)='content-inner']//div[10]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/span[1]").text.replace(
                    ',', '')

                wo_saveUpdated = nowUpdated
                print(wo_saveUpdated)
                print('\n\n전세계 상황')
                print(wo_CoronavirusCase)
                print(wo_DeathNum)
                print(wo_RecoveredNum)
                print(wo_ActiveCase)
                print(wo_ActiveMildCondition)
                print(wo_ActiveSeriousCritical)
                print(wo_ClosedCase)
                print(wo_ClosedRecoverdDischarged)
                print(wo_ClosedDeath)
                kafka_pub(wo_saveUpdated, wo_CoronavirusCase, wo_DeathNum, wo_RecoveredNum, wo_ActiveCase,
                          wo_ActiveMildCondition, wo_ActiveSeriousCritical, wo_ClosedCase, wo_ClosedRecoverdDischarged,
                          wo_ClosedDeath)


if __name__ == "__main__":
    main()
