from tkinter.tix import IMAGETEXT
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout, QFileDialog,
    QWidget)
import os
import matplotlib
matplotlib.use("TkAgg")
from tkinter import Button, Image, Label, Tk, filedialog
from tkinter import messagebox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1039, 848)
        self.actionreset = QAction(MainWindow)
        self.actionreset.setObjectName(u"actionreset")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 1011, 771))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ip_groupBox = QGroupBox(self.verticalLayoutWidget)
        self.ip_groupBox.setObjectName(u"ip_groupBox")
        font = QFont()
        font.setPointSize(13)
        self.ip_groupBox.setFont(font)
        self.verticalLayoutWidget_3 = QWidget(self.ip_groupBox)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 20, 1011, 371))
        self.ip_VLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.ip_VLayout.setObjectName(u"ip_VLayout")
        self.ip_VLayout.setContentsMargins(0, 0, 0, 0)
        self.ip_Layout1 = QHBoxLayout()
        self.ip_Layout1.setObjectName(u"ip_Layout1")
        self.upload_Layout = QVBoxLayout()
        self.upload_Layout.setObjectName(u"upload_Layout")
        self.upload_Label = QLabel(self.verticalLayoutWidget_3)
        self.upload_Label.setObjectName(u"upload_Label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.upload_Label.sizePolicy().hasHeightForWidth())
        self.upload_Label.setSizePolicy(sizePolicy)
        self.upload_Label.setMaximumSize(QSize(16777215, 16777215))
        self.upload_Layout.addWidget(self.upload_Label)

        self.upload_Button_Layout = QHBoxLayout()
        self.upload_Button_Layout.setObjectName(u"upload_Button_Layout")
        self.upload_Button_Layout.setSizeConstraint(QLayout.SetFixedSize)
        self.upload_Button = QPushButton(self.verticalLayoutWidget_3)
        self.upload_Button.setObjectName(u"upload_Button")
        self.upload_Button_Layout.addWidget(self.upload_Button)
        self.upload_func()
        

        self.upload_Label.setPixmap(QPixmap(r""))


        self.camera_Button = QPushButton(self.verticalLayoutWidget_3)
        self.camera_Button.setObjectName(u"camera_Button")

        self.upload_Button_Layout.addWidget(self.camera_Button)


        self.upload_Layout.addLayout(self.upload_Button_Layout)


        self.ip_Layout1.addLayout(self.upload_Layout)

        self.grayscale_Layout = QVBoxLayout()
        self.grayscale_Layout.setObjectName(u"grayscale_Layout")
        self.grayscale_Label = QLabel(self.verticalLayoutWidget_3)
        self.grayscale_Label.setObjectName(u"grayscale_Label")

        self.grayscale_Layout.addWidget(self.grayscale_Label)

        self.grayscale_Button = QPushButton(self.verticalLayoutWidget_3)
        self.grayscale_Button.setObjectName(u"grayscale_Button")

        self.grayscale_Layout.addWidget(self.grayscale_Button)


        self.ip_Layout1.addLayout(self.grayscale_Layout)

        self.blur_Layout = QVBoxLayout()
        self.blur_Layout.setObjectName(u"blur_Layout")
        self.blur_Label = QLabel(self.verticalLayoutWidget_3)
        self.blur_Label.setObjectName(u"blur_Label")

        self.blur_Layout.addWidget(self.blur_Label)

        self.blur_Button = QPushButton(self.verticalLayoutWidget_3)
        self.blur_Button.setObjectName(u"blur_Button")

        self.blur_Layout.addWidget(self.blur_Button)


        self.ip_Layout1.addLayout(self.blur_Layout)


        self.ip_VLayout.addLayout(self.ip_Layout1)

        self.ip_Layout2 = QHBoxLayout()
        self.ip_Layout2.setObjectName(u"ip_Layout2")
        self.edged_Layout = QVBoxLayout()
        self.edged_Layout.setObjectName(u"edged_Layout")
        self.edged_Label = QLabel(self.verticalLayoutWidget_3)
        self.edged_Label.setObjectName(u"edged_Label")

        self.edged_Layout.addWidget(self.edged_Label)

        self.edged_Button = QPushButton(self.verticalLayoutWidget_3)
        self.edged_Button.setObjectName(u"edged_Button")

        self.edged_Layout.addWidget(self.edged_Button)


        self.ip_Layout2.addLayout(self.edged_Layout)

        self.outline_Layout = QVBoxLayout()
        self.outline_Layout.setObjectName(u"outline_Layout")
        self.outline_Label = QLabel(self.verticalLayoutWidget_3)
        self.outline_Label.setObjectName(u"outline_Label")

        self.outline_Layout.addWidget(self.outline_Label)

        self.outline_Button = QPushButton(self.verticalLayoutWidget_3)
        self.outline_Button.setObjectName(u"outline_Button")

        self.outline_Layout.addWidget(self.outline_Button)


        self.ip_Layout2.addLayout(self.outline_Layout)

        self.tilt_Layout = QVBoxLayout()
        self.tilt_Layout.setObjectName(u"tilt_Layout")
        self.tilt_Label = QLabel(self.verticalLayoutWidget_3)
        self.tilt_Label.setObjectName(u"tilt_Label")

        self.tilt_Layout.addWidget(self.tilt_Label)

        self.tilt_Button = QPushButton(self.verticalLayoutWidget_3)
        self.tilt_Button.setObjectName(u"tilt_Button")

        self.tilt_Layout.addWidget(self.tilt_Button)


        self.ip_Layout2.addLayout(self.tilt_Layout)


        self.ip_VLayout.addLayout(self.ip_Layout2)


        self.verticalLayout.addWidget(self.ip_groupBox)

        self.ir_groupBox = QGroupBox(self.verticalLayoutWidget)
        self.ir_groupBox.setObjectName(u"ir_groupBox")
        self.ir_groupBox.setSizeIncrement(QSize(0, 0))
        self.ir_groupBox.setFont(font)
        self.ir_groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ir_groupBox.setCheckable(False)
        self.horizontalLayoutWidget = QWidget(self.ir_groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 20, 1011, 371))
        self.ir_Layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.ir_Layout.setObjectName(u"ir_Layout")
        self.ir_Layout.setContentsMargins(0, 0, 0, 0)
        self.dr_Layout = QVBoxLayout()
        self.dr_Layout.setObjectName(u"dr_Layout")
        self.dr_Label = QLabel(self.horizontalLayoutWidget)
        self.dr_Label.setObjectName(u"dr_Label")

        self.dr_Layout.addWidget(self.dr_Label)

        self.dr_Button = QPushButton(self.horizontalLayoutWidget)
        self.dr_Button.setObjectName(u"dr_Button")

        self.dr_Layout.addWidget(self.dr_Button)


        self.ir_Layout.addLayout(self.dr_Layout)

        self.result_Layout = QVBoxLayout()
        self.result_Layout.setObjectName(u"result_Layout")
        self.result_Label = QLabel(self.horizontalLayoutWidget)
        self.result_Label.setObjectName(u"result_Label")

        self.result_Layout.addWidget(self.result_Label)

        self.result_Button = QPushButton(self.horizontalLayoutWidget)
        self.result_Button.setObjectName(u"result_Button")

        self.result_Layout.addWidget(self.result_Button)


        self.ir_Layout.addLayout(self.result_Layout)

        self.ir_Layout.setStretch(0, 2)
        self.ir_Layout.setStretch(1, 8)

        self.verticalLayout.addWidget(self.ir_groupBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1039, 24))
        self.menureset = QMenu(self.menubar)
        self.menureset.setObjectName(u"menureset")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menureset.menuAction())
        self.menureset.addAction(self.actionreset)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def upload_func(self):
        self.upload_Button.clicked.connect(self.fileopen)

    def fileopen(self):
        print("test")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionreset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.ip_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Image Preprocessing", None))
        self.upload_Label.setText("")
        self.upload_Button.setText(QCoreApplication.translate("MainWindow", u"1-1. Upload", None))
        self.camera_Button.setText(QCoreApplication.translate("MainWindow", u"1-2. Camera", None))
        self.grayscale_Label.setText("")
        self.grayscale_Button.setText(QCoreApplication.translate("MainWindow", u"2. GrayScale", None))
        self.blur_Label.setText("")
        self.blur_Button.setText(QCoreApplication.translate("MainWindow", u"3. Blur", None))
        self.edged_Label.setText("")
        self.edged_Button.setText(QCoreApplication.translate("MainWindow", u"4. Edged", None))
        self.outline_Label.setText("")
        self.outline_Button.setText(QCoreApplication.translate("MainWindow", u"5. Outline", None))
        self.tilt_Label.setText("")
        self.tilt_Button.setText(QCoreApplication.translate("MainWindow", u"6. Tilt Correction", None))
        self.ir_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Image Recognition", None))
        self.dr_Label.setText("")
        self.dr_Button.setText(QCoreApplication.translate("MainWindow", u"Digit Recognition", None))
        self.result_Label.setText("")
        self.result_Button.setText(QCoreApplication.translate("MainWindow", u"Result Image", None))
        self.menureset.setTitle(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi
