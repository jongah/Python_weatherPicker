# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

recommendUi = '../_uiFile/viewRecommend.ui'
from View.Main import MainDialog
class RecommendDialog(QDialog):


    def __init__(self,weather):
        QDialog.__init__(self, None)
        uic.loadUi(recommendUi, self)

        # 창
        self.setWindowIcon(QIcon("../image/hang_1.png"))
        self.setWindowTitle("recommend")

        self.r_img_clothes1.setStyleSheet('image:url(../image/hang.png);')
        self.r_img_clothes2.setStyleSheet('image:url(../image/hang_1.png);')
        self.r_img_clothes3.setStyleSheet('image:url(../image/hang_1.png);')


        self.r_btn_main.clicked.connect(self.click_main)
        self.r_btn_closet.clicked.connect(self.click_closet)
        self.img = ['', 'image:url(../image/cardigan.png);', 'image:url(../image/coat.png);','image:url(../image/fleece.png);', 'image:url(../image/hoodzip_up.png);'
            , 'image:url(../image/jacket.png);', 'image:url(../image/padding.png);']
        self.tems = ['','17℃~19℃', '12℃~16℃', '9℃~11℃', '5℃~8℃', '~4℃','','옷이없습니다',""]
        self.weather = weather
        self.clothes = ['-' for i in range(3)]
        self.names = ['-' for i in range(3)]
        self.weathers = ['-' for i in range(3)]
        self.temperatures = ['-' for i in range(3)]

        self.draw_ui()

    def draw_ui(self):
        #날씨, 온도
        from data.date import Date
        date = Date()

        temperature = int(self.weather.getTemperature())
        self.r_la_year.setText(str(date.getYear()))
        self.r_la_day.setText(date.__str__())
        self.r_la_tem.setText(str(temperature)+'℃')
        self.r_la_state.setText(self.weather.getComment())

        # 옷 추천
        f = open("../File/userClothesInfo.txt",'r',encoding='UTF-8')
        tem = 0
        if temperature>=20:
            tem = 7
        elif 17<=temperature<=19:
            tem = 1
        elif 12<=temperature<=16:
            tem = 2
        elif 9<=temperature<=11:
            tem = 3
        elif 5<=temperature<=8:
            tem = 4
        elif temperature<=4:
            tem = 5

        lines = f.readlines()
        i = 0
        for line in lines:
            line = line.split('/')
            if i<3: #3번
                if line[2] == self.tems[tem]:
                    self.names[i] = line[0]
                    self.weathers[i] = line[1]
                    self.temperatures[i] = line[2]
                    self.clothes[i] = line[3]
                    i += 1


        if i<3:
            for line in lines:
                line = line.split('/')
                if i < 3:  # 3번
                    if line[2] == self.tems[tem-1]:
                        self.names[i] = line[0]
                        self.weathers[i] = line[1]
                        self.temperatures[i] = line[2]
                        self.clothes[i] = line[3]
                        i += 1

                    elif line[2] == self.tems[tem+1]:
                        self.names[i] = line[0]
                        self.weathers[i] = line[1]
                        self.temperatures[i] = line[2]
                        self.clothes[i] = line[3]
                        i += 1


        #ui
        if self.names[0]!='-':
            self.r_img_clothes1.setStyleSheet(self.img[int(self.clothes[0])])
            self.r_la_clothes1_n.setText(self.names[0])
            self.r_la_clothes1_s.setText(self.weathers[0])
            self.r_la_clothes1_t.setText(self.temperatures[0])
        else:
            pass
            #예외

        if  self.names[1]!='-':
            self.r_img_clothes2.setStyleSheet(self.img[int(self.clothes[1])])
            self.r_la_clothes2_n.setText(self.names[1])
            self.r_la_clothes2_s.setText(self.weathers[1])
            self.r_la_clothes2_t.setText(self.temperatures[1])
        else:
            # self.r_img_clothes2.hide()
            self.r_la_clothes2_n.hide()
            self.r_la_clothes2_s.hide()
            self.r_la_clothes2_t.hide()

        if self.names[2] != '-':
            self.r_img_clothes3.setStyleSheet(self.img[int(self.clothes[2])])
            self.r_la_clothes3_n.setText(self.names[2])
            self.r_la_clothes3_s.setText(self.weathers[2])
            self.r_la_clothes3_t.setText(self.temperatures[2])
        else:
            # self.r_img_clothes3.hide()
            self.r_la_clothes3_n.hide()
            self.r_la_clothes3_s.hide()
            self.r_la_clothes3_t.hide()

    def click_main(self):

        self.accept()
        r = MainDialog()
        r.show()
        r.exec_()

    def click_closet(self):
        from View.Closet import ClosetDialog
        self.accept()
        r = ClosetDialog()
        r.show()
        r.exec_()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    weather = MainDialog.get_weather
    main_dialog = RecommendDialog(weather)
    main_dialog.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

