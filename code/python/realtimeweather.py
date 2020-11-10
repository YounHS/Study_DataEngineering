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
    print('현재온도: ', currentTemperature)

    temperature = soup.find('strong', {'class': 'temperature'}).text.replace("최저기온", '')
    temperature = temperature.replace("최고기온", '')
    temperature = temperature.replace("/", '')
    highTemperature = temperature.split('°')[0]
    lowTemperature = temperature.split('°')[1]
    # highTemperature = highTemperature.replace('°', '')
    print('최저기온: ', highTemperature)

    # lowTemperature = soup.find('strong', {'class': 'temperature'}).find('span', {'class': 'blind'})[1].text.replace("최고기온", '')
    # lowTemperature = temperature.findAll('span')[2].text.replace("최고기온", '')
    # lowTemperature = lowTemperature.replace('°', '')
    print('최고기온: ', lowTemperature)

    feelTemperature = soup.find('dd', {'class': 'desc_feeling'}).text.replace('°', '')
    print('체감기온: ', feelTemperature)

    rainFall = soup.find('dd', {'class': 'desc_rainfall'}).text.replace("%", '')
    print('강수확률: ', rainFall)

    wind = soup.find('dd', {'class': 'desc_wind'}).text
    print('바람: ', wind)

    humidity = soup.find('dd', {'class': 'desc_humidity'}).text.replace('%','')
    print('습도: ', humidity)

    liFineDust = soup.find('ul', {'class': 'today_chart_list'})
    fineDust = liFineDust.findAll('li')[0]
    fineDust = fineDust.find('strong', {'class': 'value'}).text
    print('미세먼지: ', fineDust)

    liUltraFineDust = soup.find('ul', {'class': 'today_chart_list'})
    ultraFineDust = liUltraFineDust.findAll('li')[1]
    ultraFineDust = ultraFineDust.find('strong', {'class': 'value'}).text
    print('초미세먼지: ', ultraFineDust)

    liOzone = soup.find('ul', {'class': 'today_chart_list'})
    ozone = liOzone.findAll('li')[2]
    ozone = ozone.find('strong', {'class': 'value'}).text
    print('자외선', ozone)

    update = soup.find('span', {'class': 'title_dsc'}).text.replace(" 업데이트", '')
    print('최근 업데이트 시각: ', update)


# conn = psycopg2.connect(conn_string)
# cur = conn.cursor()
#
# cur.execute("CREATE TABLE realtime_env_naver ("
#             "seq SERIAL PRIMARY KEY, "
#             "current_temperature TEXT, "
#             "high_temperature TEXT, "
#             "low_temperature TEXT, "
#             "feel_temperature TEXT, "
#             "rain_fall TEXT, "
#             "windms TEXT, "
#             "humidities TEXT, "
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

