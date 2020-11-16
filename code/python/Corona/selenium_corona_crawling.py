__author__ = 'Hyeonsoo Youn'

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
import psycopg2
import time

conn_string = "host='localhost' dbname ='collectData' user='postgres' password='secy'"

driver = webdriver.Chrome('C:\chromedriver.exe')

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "last-updated"))
#     )
#
# finally:

while 1:
    # driver.implicitly_wait(5)
    # driver = webdriver.Chrome('C:\chromedriver.exe')
    # driver.implicitly_wait(3)
    # headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    driver.get('https://coronaboard.kr/')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # html = requests.get(driver.page_source, headers=headers)

    # soup = BeautifulSoup(html.text, 'html.parser')
    # time.sleep(60)
    extractworldpopulation = driver.find_element_by_xpath("//span[@id='last-updated']")
    # extractworldpopulation = soup.find('span', {'id': 'last-updated'}).text.replace("마지막 업데이트: ", '')
    # extractworldpopulation = driver.find_element_by_name('id').send_keys('last-updated')
    # extractworldpopulation = driver.find_element('id', "last-updated")
    print(extractworldpopulation.text)
    # time.sleep(5)
    # worldpopulation = extractworldpopulation.findAll('span')[1].text
    # worldpopulation += extractworldpopulation.findAll('span')[3].text
    # worldpopulation += extractworldpopulation.findAll('span')[5].text
    # worldpopulation += extractworldpopulation.findAll('span')[7].text
    # print(worldpopulation)

    # highTemperature = soup.find('strong', {'class': 'degree_height'}).text.replace("최고온도", '')
    # highTemperature = highTemperature.replace('°', '')
    # print(highTemperature)
    #
    # lowTemperature = soup.find('strong', {'class': 'degree_low'}).text.replace("최저온도", '')
    # lowTemperature = lowTemperature.replace('°', '')
    # print(lowTemperature)
    #
    # feelTemperature = soup.find('strong', {'class': 'degree_feel'}).text.replace('°', '')
    # print(feelTemperature)
    #
    # timeRainFall = soup.find('a', {'class': 'link_rainfall'}).text.replace("시간당 강수량 ", '')
    # timeRainFall = timeRainFall.replace("mm", '')
    # print(timeRainFall)
    #
    # liFineDust = soup.find('ul', {'class': 'today_chart_list'})
    # fineDust = liFineDust.findAll('li')[0]
    # fineDust = fineDust.find('strong', {'class': 'value'}).text
    # print(fineDust)
    #
    # liUltraFineDust = soup.find('ul', {'class': 'today_chart_list'})
    # ultraFineDust = liUltraFineDust.findAll('li')[1]
    # ultraFineDust = ultraFineDust.find('strong', {'class': 'value'}).text
    # print(ultraFineDust)
    # # ultraFineDust = liUltraFineDust[1].find('strong', {'class': 'value'}).text
    # # print(ultraFineDust)
    #
    # liOzone = soup.find('ul', {'class': 'today_chart_list'})
    # ozone = liOzone.findAll('li')[2]
    # ozone = ozone.find('strong', {'class': 'value'}).text
    # print(ozone)
    #
    # update = soup.find('span', {'class': 'title_dsc'}).text.replace(" 업데이트", '')
    # print(update)


# conn = psycopg2.connect(conn_string)
# cur = conn.cursor()
#
# cur.execute("CREATE TABLE realtime_env_naver ("
#             "seq SERIAL PRIMARY KEY, "
#             "current_temperature TEXT, "
#             "high_temperature TEXT, "
#             "low_temperature TEXT, "
#             "feel_temperature TEXT, "
#             "time_rain_fall TEXT, "
#             "fine_dust TEXT, "
#             "ultra_fine_dust TEXT, "
#             "ozone TEXT, "
#             "server_update_time TEXT, "
#             "creation_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
# conn.commit()

    # conn = psycopg2.connect(conn_string)
    # cur = conn.cursor()
    # cur.execute("INSERT INTO realtime_env_naver(seq,"
    #             "current_temperature, "
    #             "high_temperature, "
    #             "low_temperature, "
    #             "feel_temperature, "
    #             "time_rain_fall, "
    #             "fine_dust, "
    #             "ultra_fine_dust, "
    #             "ozone, "
    #             "server_update_time) "
    #             "VALUES (nextval('realtime_env_naver_seq_seq'), %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
    #                 currentTemperature, highTemperature, lowTemperature, feelTemperature,
    #                 timeRainFall, fineDust, ultraFineDust, ozone, update))
    # conn.commit()
    # cur.close()
    # conn.close()
    # time.sleep(60)