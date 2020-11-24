# How to set selenium in Linux system?
1. 크롬 설치

```bash
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
```

```bash
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
```

```bash
sudo apt-get update 
```

```bash
sudo apt-get install google-chrome-stable
```



2. 크롬 버전 확인

```bash
google-chrome --version
```

상단의 명령어로 크롬 버전 확인 후, 버전에 맞는 [chromedriver 다운로드](https://sites.google.com/a/chromium.org/chromedriver/) 후 압축 해제



3. 필요한 라이브러리 설치

```bash
sudo pip3 install xlrd
```

```bash
sudo apt install xvfb
```



4. chromedriver에 실행권한 설정 및 환경을 위한 세팅

```bash
chmod +x chromedriver
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```



5. selenium 설치

```bash
pip3 install selenium
```

------

해야할 일

> corona web crawl data를 ELK 스택에 적재하기