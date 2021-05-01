# -*- coding: utf-8 -*-

import sys
import os.path

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

from typing import TYPE_CHECKING



closetUi = '../_uiFile/viewCloset.ui'

class ClosetDialog(QDialog):



    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(closetUi, self)
        # 창
        self.setWindowIcon(QIcon("../image/hang_1.png"))
        self.setWindowTitle("closet")

        self.img = ['','image:url(../image/cardigan.png);','image:url(../image/coat.png);','image:url(../image/fleece.png);','image:url(../image/hoodzip_up.png);'
           ,'image:url(../image/jacket.png);','image:url(../image/padding.png);','image:url(../image/tem.png);']
        self.clothes_labeles = []
        self.name_labeles = []
        self.season_labeles = []
        self.temperature_labeles =[]
        self.c_btn_main.clicked.connect(self.click_main)
        self.c_btn_add.clicked.connect(self.click_add)

        self.file_read()


    def file_read(self):

        file = '../File/userClothesInfo.txt'
        if os.path.isfile(file)==False: #만약 파일이 없다면(앱을 처음 실행)
            f  = open("../File/userClothesInfo.txt", 'a', encoding='UTF-8')
            f.close()
        else:
            f  = open(file,'r', encoding='UTF-8')
            lines = f .readlines()
            f.close()
            self.draw_ui(lines)


    def delete(self,state,i,lines):
        reply = QMessageBox.question(self, "삭제", "선택하신 항목을 삭제하시겠습니까?",QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            f_write = open("../File/userClothesInfo.txt", 'w', encoding='UTF-8')

            for j in range(0,len(lines)):
                if j != i:
                    f_write.write(lines[j])
            f_write.close()

            self.file_read()


    def draw_ui(self,lines):
        j = 0

        for i in range(0,len(self.clothes_labeles)):
            self.clothes_labeles[i].hide()
            self.name_labeles[i].hide()
            self.season_labeles[i].hide()
            self.temperature_labeles[i].hide()
        for i in range(0,len(lines)):
            line = lines[i].split('/')
            name = line[0]
            season = line[1]
            temperature = line[2]
            clothes = line[3]


            if i>3:j=1

            #옷
            img_clothes = QPushButton('',self)
            img_clothes.show()
            img_clothes.setStyleSheet(self.img[int(clothes)]+" border:0px")
            img_clothes.clicked.connect(lambda state, i1 = i : self.delete(state,i1,lines))
            i = i % 4
            img_clothes.setGeometry(20+i*320,170+300*j,171,211)
            self.clothes_labeles.append(img_clothes)

            #이름
            label_name = QLabel(name, self)
            label_name.show()
            label_name.setAlignment(Qt.AlignCenter)
            label_name.setGeometry(20 + i * 320, 370+300*j, 171, 51)
            label_name.setStyleSheet('font: 25 15pt "나눔바른고딕 Light";')
            self.name_labeles.append(label_name)

            #계절
            label_season = QLabel(season, self)
            label_season.show()
            label_season.setGeometry(200 + i * 320, 170+300*j, 121, 61)
            label_season.setStyleSheet('font: 25 10pt "나눔바른고딕 Light";')
            self.season_labeles.append(label_season)

            #온도
            label_temperature = QLabel(temperature, self)
            label_temperature.show()
            label_temperature.setGeometry(200 + i * 320, 240+300*j, 121, 61)
            label_temperature.setStyleSheet(' font: 25 10pt "나눔바른고딕 Light";')
            self.temperature_labeles.append(label_temperature)


    def click_main(self):
        from View.Main import MainDialog
        self.accept()
        r = MainDialog()
        r.show()
        r.exec_()

    def click_add(self):
        f = open("../File/userClothesInfo.txt",'r',encoding='UTF-8')
        lines = f.readlines()
        if len(lines)>=8:
            QMessageBox.about(self,"message","최대 8개까지 저장이가능합니다")
        else:
            from View.Add import AddDialog
            self.accept()
            r = AddDialog()
            r.show()
            r.exec_()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main_dialog = ClosetDialog()
    main_dialog.show()
    sys.exit(app.exec_())