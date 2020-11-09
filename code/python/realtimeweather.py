__author__ = 'Hyeonsoo Youn'

from bs4 import BeautifulSoup
import requests
import psycopg2
import time

conn_string = "host='localhost' dbname ='collectData' user='postgres' password='secy'"

while 1:
    html = requests.get('https://n.weather.naver.com/today/05200125')

    soup = BeautifulSoup(html.text, 'html.parser')

    currentTemperature = soup.find('strong', {'class': 'current'}).text.replace("현재 온도", '')
    currentTemperature = currentTemperature.replace('°', '')
    print(currentTemperature)

    highTemperature = soup.find('strong', {'class': 'degree_height'}).text.replace("최고온도", '')
    highTemperature = highTemperature.replace('°', '')
    print(highTemperature)

    lowTemperature = soup.find('strong', {'class': 'degree_low'}).text.replace("최저온도", '')
    lowTemperature = lowTemperature.replace('°', '')
    print(lowTemperature)

    feelTemperature = soup.find('strong', {'class': 'degree_feel'}).text.replace('°', '')
    print(feelTemperature)

    timeRainFall = soup.find('a', {'class': 'link_rainfall'}).text.replace("시간당 강수량 ", '')
    timeRainFall = timeRainFall.replace("mm", '')
    print(timeRainFall)

    liFineDust = soup.find('ul', {'class': 'today_chart_list'})
    fineDust = liFineDust.findAll('li')[0]
    fineDust = fineDust.find('strong', {'class': 'value'}).text
    print(fineDust)

    liUltraFineDust = soup.find('ul', {'class': 'today_chart_list'})
    ultraFineDust = liUltraFineDust.findAll('li')[1]
    ultraFineDust = ultraFineDust.find('strong', {'class': 'value'}).text
    print(ultraFineDust)
    # ultraFineDust = liUltraFineDust[1].find('strong', {'class': 'value'}).text
    # print(ultraFineDust)

    liOzone = soup.find('ul', {'class': 'today_chart_list'})
    ozone = liOzone.findAll('li')[2]
    ozone = ozone.find('strong', {'class': 'value'}).text
    print(ozone)

    update = soup.find('span', {'class': 'title_dsc'}).text.replace(" 업데이트", '')
    print(update)


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
    time.sleep(60)