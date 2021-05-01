# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

addUi = '../_uiFile/viewAdd.ui'

class AddDialog(QDialog):

    #전역변수 사용시 self.season 처럼 사용
    # name = ''
    # season = ''
    # tem = ''
    # clothes = ''

    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(addUi, self)

        # 창
        self.setWindowIcon(QIcon("../image/hang_1.png"))
        self.setWindowTitle("add")

        self.name = '-'
        self.season = '-'
        self.tem = '-'
        self.clothes = '-'

        # 이미지 셋팅
        self.a_img_clothes1.setStyleSheet('image:url(../image/cardigan.png);')
        self.a_img_clothes2.setStyleSheet('image:url(../image/coat.png);')
        self.a_img_clothes3.setStyleSheet('image:url(../image/fleece.png);')
        self.a_img_clothes4.setStyleSheet('image:url(../image/hoodzip_up.png);')
        self.a_img_clothes5.setStyleSheet('image:url(../image/jacket.png);')
        self.a_img_clothes6.setStyleSheet('image:url(../image/padding.png);')
        self.a_img_tem.setStyleSheet('image:url(../image/tem.png);')

        #btn_리스너
        self.a_btn_add.clicked.connect(self.btn_add)
        self.a_btn_cancle.clicked.connect(self.btn_cancle)

        #btn_radio season
        self.a_rb_s_spring_fall.clicked.connect(self.groupBox_season)
        self.a_rb_s_winter.clicked.connect(self.groupBox_season)

        # btn_radio tem
        self.a_rb_t1.clicked.connect(self.groupBox_tem)
        self.a_rb_t2.clicked.connect(self.groupBox_tem)
        self.a_rb_t3.clicked.connect(self.groupBox_tem)
        self.a_rb_t4.clicked.connect(self.groupBox_tem)
        self.a_rb_t5.clicked.connect(self.groupBox_tem)
        #self.a_rb_t20.clicked.connect(self.groupBox_tem)

        # btn_radio clothes
        self.a_rb_clothes1.clicked.connect(self.groupBox_clothes)
        self.a_rb_clothes2.clicked.connect(self.groupBox_clothes)
        self.a_rb_clothes3.clicked.connect(self.groupBox_clothes)
        self.a_rb_clothes4.clicked.connect(self.groupBox_clothes)
        self.a_rb_clothes5.clicked.connect(self.groupBox_clothes)
        self.a_rb_clothes6.clicked.connect(self.groupBox_clothes)

    def setSeason(self, s):
        self.season = s

    def setTem(self, t):
        self.tem = t

    def setClothes(self,c):
        self.clothes = c


    def groupBox_season(self):
        if self.a_rb_s_spring_fall.isChecked():
            self.setSeason('spring,fall')
        elif self.a_rb_s_winter.isChecked():
            self.setSeason('winter')

    def groupBox_tem(self):
        if self.a_rb_t1.isChecked():
            self.setTem('17℃~19℃')
        elif self.a_rb_t2.isChecked():
            self.setTem('12℃~16℃')
        elif self.a_rb_t3.isChecked():
            self.setTem('9℃~11℃')
        elif self.a_rb_t4.isChecked():
            self.setTem('5℃~8℃')
        elif self.a_rb_t5.isChecked():
            self.setTem('~4℃')
        # elif self.a_rb_t20.isChecked():
        #     self.setTem('20')

    def groupBox_clothes(self):
        if self.a_rb_clothes1.isChecked():
            self.setClothes('1')
        elif self.a_rb_clothes2.isChecked():
            self.setClothes('2')
        elif self.a_rb_clothes3.isChecked():
            self.setClothes('3')
        elif self.a_rb_clothes4.isChecked():
            self.setClothes('4')
        elif self.a_rb_clothes5.isChecked():
            self.setClothes('5')
        elif self.a_rb_clothes6.isChecked():
            self.setClothes('6')

    def fileWrite(self,name,season,temperature, clothes):
        #'a' : 쓰기를 위해 열려 있고, 파일의 끝에 추가하는 경우 추가합니다
        #상대주소
        f = open("../File/userClothesInfo.txt", 'a', encoding='UTF-8')
        try:
            f.write(name + '/' + season + '/' + temperature +'/'+ clothes +'\n')
        except FileNotFoundError as e:
            print(e)
        finally:
            f.close()
            self.btn_cancle()

    def btn_add(self):
        #이름 입력 and 모두다 선택되어있을 떄
        self.name = self.a_te_name.toPlainText()
        if(self.name != '' and self.clothes != '-'and self.tem != '-'and self.season != '-'):
            self.fileWrite(self.name, self.season, self.tem, self.clothes)

        else:
            QMessageBox.about(self,"message","모든항목을 다 입력해주세요")
        

    def btn_cancle(self):
        from View.Closet import ClosetDialog
        self.accept()
        r = ClosetDialog()
        r.show()
        r.exec_()



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main_dialog = AddDialog()
    main_dialog.show()
    main_dialog.exec_()
