# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)


class UI_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(946, 546)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"  border:none;\n"
"}\n"
"QLabel{\n"
"  color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_conteiner = QFrame(self.centralwidget)
        self.left_conteiner.setObjectName(u"left_conteiner")
        self.left_conteiner.setMaximumSize(QSize(200, 16777215))
        self.left_conteiner.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.left_conteiner)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.left_conteiner)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_conteiner)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(200, 16777215))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QToolbox{\n"
"text-align: left;\n"
"background-color: rgb(228, 254, 255);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"border-radius: 5px;\n"
"background-color: rgb (194, 232, 255);\n"
"text-align: left;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMaximumSize(QSize(200, 16777215))
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(65. 65. 65);\n"
"border-top-left-radius:15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 164, 406))
        self.page.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(11)
        self.btn_home.setFont(font)
        self.btn_home.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(65. 65. 65);\n"
"border-top-left-radius:15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font)

        self.verticalLayout_6.addWidget(self.btn_cadastrar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 164, 406))
        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_conteiner)

        self.main_conteiner = QFrame(self.centralwidget)
        self.main_conteiner.setObjectName(u"main_conteiner")
        self.main_conteiner.setFrameShape(QFrame.NoFrame)
        self.verticalLayout = QVBoxLayout(self.main_conteiner)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_conteiner)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        icon = QIcon()
        icon.addFile(u":/icons/menu2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_toggle.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignHCenter)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame, 0, Qt.AlignLeft)

        self.main_frame = QFrame(self.main_conteiner)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Page = QStackedWidget(self.main_frame)
        self.Page.setObjectName(u"Page")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.label_3 = QLabel(self.pg_home)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 110, 441, 181))
        self.Page.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_7 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 37);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 671, 281))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: rgba(0, 0, 0, 236);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(120, 30))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")

        self.gridLayout.addWidget(self.lineEdit_3, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(120, 30))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")

        self.gridLayout.addWidget(self.lineEdit_2, 2, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(120, 30))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")

        self.gridLayout.addWidget(self.lineEdit_5, 3, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(120, 30))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")
        self.lineEdit_4.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEdit_4, 4, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(290, 280, 92, 33))
        self.pushButton_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(11, 157, 255);\n"
"border-radius: 15px;")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(6, 10, 651, 61))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 87 18pt \"Arial Black\";")
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 80, 401, 261))
        self.tableWidget.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(227, 227, 227);")
        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(460, 110, 138, 166))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_excel = QPushButton(self.frame_3)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(120, 30))
        self.btn_excel.setStyleSheet(u"background-color: rgb(40, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 15px;")

        self.verticalLayout_8.addWidget(self.btn_excel)

        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(120, 30))
        self.pushButton_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 166, 12);\n"
"border-radius: 15px;")

        self.verticalLayout_8.addWidget(self.pushButton_6)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(120, 30))
        self.btn_excluir.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius: 15px;")

        self.verticalLayout_8.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.Page.addWidget(self.pg_cadastrar)

        self.horizontalLayout_3.addWidget(self.Page)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_conteiner)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.footer_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_conteiner)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Page.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sistema de Cadastro de Clientes", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Bem-vindo ao Sistema</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Cadastro</p></body></html>", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Clientes</p><p align=\"center\"><br/></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"SENHA", None));
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.label_2.setText("")
    # retranslateUi

