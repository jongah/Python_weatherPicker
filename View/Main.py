# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from data.weather import Weather
from data.date import Date

# from typing import TYPE_CHECKING
# if TYPE_CHECKING:

from View.Closet import ClosetDialog

mainUi = '../_uiFile/viewMain.ui'

class MainDialog(QDialog):
    def __init__(self):
        super(MainDialog, self).__init__()
        QDialog.__init__(self, None)
        uic.loadUi(mainUi, self)

        #창
        self.setWindowIcon(QIcon("../image/hang_1.png"))
        self.setWindowTitle("weather's Picker")
        #날씨
        self.weather = Weather()
        self.weather.getWeather()
        #날짜
        self.date = Date()
        #클릭
        self.m_btn_closet.clicked.connect(self.click_closet)
        self.m_btn_reco.clicked.connect(self.click_recommend)
        self.m_btn_seoul.clicked.connect(lambda state,button = self.m_btn_seoul: self.click_area(state,button))
        self.m_btn_busan.clicked.connect(lambda state,button = self.m_btn_busan: self.click_area(state,button))
        self.m_btn_dejun.clicked.connect(lambda state,button = self.m_btn_dejun: self.click_area(state,button))
        self.m_btn_jeju.clicked.connect(lambda state,button = self.m_btn_jeju: self.click_area(state,button))
        self.m_btn_ham.clicked.connect(lambda state,button = self.m_btn_ham: self.click_area(state,button))

        self.draw_ui()


    def draw_ui(self):
        # 년도
        self.m_la_year.setText(str(self.date.getYear()))
        self.m_la_day.setText(self.date.__str__())
        # 온도
        self.m_la_tem.setText(self.weather.getTemperature() + '°C')
        # 상태
        self.m_la_state.setText(self.weather.getComment())
        #지역
        self.m_la_area.setText(self.weather.getLocaion())

    def get_weather(self):
        return self.weather

    def click_area(self,state ,button):
        self.weather.setLocation(button.text())
        self.weather.getWeather()
        self.m_la_tem.setText(self.weather.getTemperature()+'°C')
        self.m_la_state.setText(self.weather.getComment())
        self.m_la_area.setText(self.weather.getLocaion())

    def click_closet(self):
        self.accept()
        r = ClosetDialog()
        r.show()
        r.exec_()

    def click_recommend(self):
        from View.Recommend import RecommendDialog
        self.accept()
        r = RecommendDialog(self.weather)
        r.show()
        r.exec_()



if __name__ == "__main__" :
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    main_dialog = MainDialog()
    # 프로그램 화면을 보여주는 코드
    main_dialog.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()