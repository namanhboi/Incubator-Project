import os
from PyQt6 import QtCore, QtGui, QtWidgets

ImageDirectory = os.path.dirname(__file__).removesuffix('blocker') + "resources\images"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(960, 540))
        MainWindow.setMaximumSize(QtCore.QSize(12800, 6090))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:#70333E")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.OptionButton = QtWidgets.QPushButton(self.centralwidget)
        self.OptionButton.setGeometry(QtCore.QRect(60, 50, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OptionButton.sizePolicy().hasHeightForWidth())
        self.OptionButton.setSizePolicy(sizePolicy)
        self.OptionButton.setMinimumSize(QtCore.QSize(40, 40))
        self.OptionButton.setMaximumSize(QtCore.QSize(40, 40))
        self.OptionButton.setStyleSheet(
            "QPushButton {\n"
            "    border-radius: 20px;\n"
            "    background: #CB909B;\n"
            "    }\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(166, 118, 127);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background: rgb(103, 73, 79);\n"
            "}")
        self.OptionButton.setText("")
        OptionButtonIcon = QtGui.QIcon()
        OptionButtonIcon.addPixmap(QtGui.QPixmap(ImageDirectory+"\settingsbutton.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.OptionButton.setIcon(OptionButtonIcon)
        self.OptionButton.setIconSize(QtCore.QSize(35, 35))
        self.OptionButton.setCheckable(True)
        self.OptionButton.setObjectName("OptionButton")


        self.PlayButton = QtWidgets.QPushButton(self.centralwidget)
        self.PlayButton.setGeometry(QtCore.QRect(315, 430, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlayButton.sizePolicy().hasHeightForWidth())
        self.PlayButton.setSizePolicy(sizePolicy)
        self.PlayButton.setMinimumSize(QtCore.QSize(40, 40))
        self.PlayButton.setMaximumSize(QtCore.QSize(40, 40))
        self.PlayButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.PlayButton.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #CB909B;\n"
            "    border-radius: 20px;\n"
            "    background: #CB909B;\n"
            "    }\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(166, 118, 127);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background: rgb(103, 73, 79);\n"
            "}")
        self.PlayButton.setText("")
        PlayButtonIcon = QtGui.QIcon()
        PlayButtonIcon.addPixmap(QtGui.QPixmap(ImageDirectory+"\playbutton.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.PlayButton.setIcon(PlayButtonIcon)
        self.PlayButton.setIconSize(QtCore.QSize(50, 50))
        self.PlayButton.setCheckable(True)
        self.PlayButton.setObjectName("PlayButton")


        self.MuteButton = QtWidgets.QPushButton(self.centralwidget)
        self.MuteButton.setGeometry(QtCore.QRect(375, 430, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MuteButton.sizePolicy().hasHeightForWidth())
        self.MuteButton.setSizePolicy(sizePolicy)
        self.MuteButton.setMinimumSize(QtCore.QSize(40, 40))
        self.MuteButton.setMaximumSize(QtCore.QSize(40, 40))
        self.MuteButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.MuteButton.setStyleSheet(
            "QPushButton {\n"
            "    border: 2px solid #CB909B;\n"
            "    border-radius: 20px;\n"
            "    background: #CB909B;\n"
            "    }\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgb(166, 118, 127);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background: rgb(103, 73, 79);\n"
            "}")
        self.MuteButton.setText("")
        MuteButtonIcon = QtGui.QIcon()
        MuteButtonIcon.addPixmap(QtGui.QPixmap(ImageDirectory+"\mutebutton.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.MuteButton.setIcon(MuteButtonIcon)
        self.MuteButton.setIconSize(QtCore.QSize(45, 45))
        self.MuteButton.setCheckable(True)
        self.MuteButton.setObjectName("MuteButton")


        self.VolumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.VolumeSlider.setGeometry(QtCore.QRect(435, 430, 150, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VolumeSlider.sizePolicy().hasHeightForWidth())
        self.VolumeSlider.setSizePolicy(sizePolicy)
        self.VolumeSlider.setMinimumSize(QtCore.QSize(150, 40))
        self.VolumeSlider.setMaximumSize(QtCore.QSize(150, 40))
        self.VolumeSlider.setStyleSheet(
            ".QSlider {\n"
            "    min-height: 40px;\n"
            "    max-height: 40px;\n"
            "}\n"
            "\n"
            ".QSlider::groove:horizontal {\n"
            "    height: 6px;\n"
            "    background: #000000;\n"
            "    margin: 0 12px;\n"
            "}\n"
            "\n"
            ".QSlider::handle:horizontal {\n"
            "    background: #CB909B;\n"
            "    width: 10px;\n"
            "    height: 50px;\n"
            "    margin: -10px -5px;\n"
            "}")
        self.VolumeSlider.setMaximum(100)
        self.VolumeSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.VolumeSlider.setObjectName("VolumeSlider")


        self.ForwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.ForwardButton.setGeometry(QtCore.QRect(605, 430, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ForwardButton.sizePolicy().hasHeightForWidth())
        self.ForwardButton.setSizePolicy(sizePolicy)
        self.ForwardButton.setMinimumSize(QtCore.QSize(40, 40))
        self.ForwardButton.setMaximumSize(QtCore.QSize(40, 40))
        self.ForwardButton.setStyleSheet("\n"
            "\n"
            "QPushButton {\n"
            "    border:0px;\n"
            "    background:#70333E;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background:rgb(164, 75, 91);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {"
            "    background:rgb(221, 101, 123);"
            "}")
        self.ForwardButton.setText("")
        ForwardButtonIcon = QtGui.QIcon()
        ForwardButtonIcon.addPixmap(QtGui.QPixmap(ImageDirectory+"\Forwardbutton.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ForwardButton.setIcon(ForwardButtonIcon)
        self.ForwardButton.setIconSize(QtCore.QSize(40, 40))
        self.ForwardButton.setCheckable(True)
        self.ForwardButton.setObjectName("ForwardButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
