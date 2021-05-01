# -*- coding: utf-8 -*-
#pip install bs4
#pip install html5lib

from urllib.request import urlopen, Request
import urllib
import bs4

class Weather:

    def __init__(self):
        self.location ='서울'
        self.temperature =''
        self.url=''
        self.comment = ''


    def __str__(self):
        print('현재 ' + self.location + ' 날씨는 ' + self.temperature + '도 입니다.')
        print(self.url)
        #return self.location

    def setLocation(self,area):
        self.location = area

    def getLocaion(self):
        return self.location

    def getTemperature(self):
        self.getWeather()
        return self.temperature

    def getComment(self):
        return self.comment

    def getWeather(self):
        enc_location = urllib.parse.quote(self.location + '+날씨')
        self.url = 'https://search.naver.com/search.naver?ie=utf8&query=' + enc_location
        req = Request(self.url)
        page = urlopen(req)
        html = page.read()
        soup = bs4.BeautifulSoup(html, 'html5lib')
        self.temperature = soup.find('p', class_='info_temperature').find('span',class_='todaytemp').text
        self.comment = soup.find('p',{"class":'cast_txt'}).text
        #print(self.temperature)





if __name__ == '__main__':
    weather = Weather()

    weather.getWeather()
    weather.__str__()

