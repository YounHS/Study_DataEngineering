__author__ = 'Hyeonsoo Youn'

from bs4 import BeautifulSoup
from selenium import webdriver
from kafka import KafkaProducer

import psycopg2
import time
import json
import datetime

conn_string = "host='localhost' dbname ='collectData' user='postgres' password='secy'"


def kafka_pub(saveUpdated, worldConfirmedCase, worldDeathNum, worldQuarantineRelease, worldFatalityRate,
              occurCountry, domesticConfirmedCase, domesticDeathNum, domesticQuarantineRelease,
              domesticFatalityRate, totalInspector, duringInspect, navigateResult):
    now = datetime.datetime.now()
    nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
    producer = KafkaProducer(bootstrap_servers=["localhost:9092"])
    topicName = "corona"
    msg = {"saveUpdated": saveUpdated, "worldConfirmedCase": worldConfirmedCase, "worldDeathNum": worldDeathNum,
           "worldQuarantineRelease": worldQuarantineRelease, "worldFatalityRate": worldFatalityRate,
           "occurCountry": occurCountry, "domesticConfirmedCase": domesticConfirmedCase,
           "domesticDeathNum": domesticDeathNum, "domesticQuarantineRelease": domesticQuarantineRelease,
           "domesticFatalityRate": domesticFatalityRate, "totalInspector": totalInspector,
           "duringInspect": duringInspect, "navigateResult": navigateResult, "insertTime": nowDateTime}

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

    driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

    count = True
    saveUpdated = ''

    while 1:
        # driver.implicitly_wait(5)
        # headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
        driver.get('https://coronaboard.kr/')
        time.sleep(10)

        nowUpdated = driver.find_element_by_xpath("//span[@id='last-updated']").text

        worldConfirmedCase = driver.find_element_by_xpath(
            "//div[normalize-space(@class)='row dashboard world']//div[1]/p[1]").text.replace(',', '')
        worldDeathNum = driver.find_element_by_xpath(
            "//div[normalize-space(@class)='row dashboard world']//div[2]/p[1]").text.replace(',', '')
        worldQuarantineRelease = driver.find_element_by_xpath(
            "//div[normalize-space(@class)='row dashboard world']//div[3]/p[1]").text.replace(',', '')
        worldFatalityRate = driver.find_element_by_xpath(
            "//div[normalize-space(@class)='row dashboard world']//div[4]/p[1]").text.replace('%', '')
        occurCountry = driver.find_element_by_xpath(
            "//div[normalize-space(@class)='row dashboard world']//div[5]/p[1]").text.replace(',', '')

        domesticConfirmedCase = driver.find_element_by_xpath(
            "//div[normalize-space(@class)='row dashboard domestic']//div[1]/p[1]").text.replace(',', '')
        domesticDeathNum = driver.find_element_by_xpath(
            "//div[normalize-space(@class)='row dashboard domestic']//div[2]/p[1]").text.replace(',', '')
        domesticQuarantineRelease = driver.find_element_by_xpath(
            "//div[normalize-space(@class)='row dashboard domestic']//div[3]/p[1]").text.replace(',', '')
        domesticFatalityRate = driver.find_element_by_xpath(
            "//div[normalize-space(@class)='row dashboard domestic']//div[4]/p[1]").text.replace('%', '')
        totalInspector = driver.find_element_by_xpath(
            "//div[normalize-space(@class)='row dashboard domestic']//div[5]/p[1]").text.replace(',', '')
        duringInspect = driver.find_element_by_xpath(
            "//div[normalize-space(@class)='row dashboard domestic']//div[6]/p[1]").text.replace(',', '')
        navigateResult = driver.find_element_by_xpath(
            "//div[normalize-space(@class)='row dashboard domestic']//div[7]/p[1]").text.replace(',', '')

        if count or len(saveUpdated) == 0:
            saveUpdated = nowUpdated
            print(saveUpdated)
            print('\n\nWhole world statistics')
            print(worldConfirmedCase)
            print(worldDeathNum)
            print(worldQuarantineRelease)
            print(worldFatalityRate)
            print(occurCountry)
            print('\n\nKorea statistics')
            print(domesticConfirmedCase)
            print(domesticDeathNum)
            print(domesticQuarantineRelease)
            print(domesticFatalityRate)
            print(totalInspector)
            print(duringInspect)
            print(navigateResult)
            kafka_pub(saveUpdated, worldConfirmedCase, worldDeathNum, worldQuarantineRelease, worldFatalityRate,
                      occurCountry, domesticConfirmedCase, domesticDeathNum, domesticQuarantineRelease,
                      domesticFatalityRate, totalInspector, duringInspect, navigateResult)
            count = False
        else:
            # new updated data record
            if (nowUpdated != '-') and (saveUpdated != nowUpdated):
                saveUpdated = nowUpdated
                print(saveUpdated)
                print('\n\nWhole world statistics')
                print(worldConfirmedCase)
                print(worldDeathNum)
                print(worldQuarantineRelease)
                print(worldFatalityRate)
                print(occurCountry)
                print('\n\nKorea statistics')
                print(domesticConfirmedCase)
                print(domesticDeathNum)
                print(domesticQuarantineRelease)
                print(domesticFatalityRate)
                print(totalInspector)
                print(duringInspect)
                print(navigateResult)
                kafka_pub(saveUpdated, worldConfirmedCase, worldDeathNum, worldQuarantineRelease, worldFatalityRate,
                          occurCountry, domesticConfirmedCase, domesticDeathNum, domesticQuarantineRelease,
                          domesticFatalityRate, totalInspector, duringInspect, navigateResult)


if __name__ == "__main__":
    main()
