# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '360RAT_windows_dark_expanding.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Anottation(object):
    def setupUi(self, Anottation):
        Anottation.setObjectName("Anottation")
        Anottation.resize(1319, 920)
        Anottation.setLayoutDirection(QtCore.Qt.LeftToRight)
        Anottation.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.315789 rgba(28, 29, 73, 255));\n"
"color:rgb(255,255,255);\n"
"border-color: rgb(44, 0, 66);")
        self.window = QtWidgets.QWidget(Anottation)
        self.window.setObjectName("window")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.window)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.button_go_to_first = QtWidgets.QPushButton(self.window)
        self.button_go_to_first.setMinimumSize(QtCore.QSize(80, 30))
        self.button_go_to_first.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_go_to_first.setFont(font)
        self.button_go_to_first.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_go_to_first.setObjectName("button_go_to_first")
        self.horizontalLayout_7.addWidget(self.button_go_to_first)
        self.button_go_to_last = QtWidgets.QPushButton(self.window)
        self.button_go_to_last.setMinimumSize(QtCore.QSize(80, 30))
        self.button_go_to_last.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_go_to_last.setFont(font)
        self.button_go_to_last.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_go_to_last.setObjectName("button_go_to_last")
        self.horizontalLayout_7.addWidget(self.button_go_to_last)
        self.label = QtWidgets.QLabel(self.window)
        self.label.setMinimumSize(QtCore.QSize(600, 60))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:none;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.equi_image = QtWidgets.QLabel(self.window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equi_image.sizePolicy().hasHeightForWidth())
        self.equi_image.setSizePolicy(sizePolicy)
        self.equi_image.setMinimumSize(QtCore.QSize(750, 250))
        self.equi_image.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.equi_image.setFont(font)
        self.equi_image.setMouseTracking(True)
        self.equi_image.setText("")
        self.equi_image.setObjectName("equi_image")
        self.verticalLayout_4.addWidget(self.equi_image)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_play_video = QtWidgets.QPushButton(self.window)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_play_video.setFont(font)
        self.button_play_video.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_play_video.setObjectName("button_play_video")
        self.horizontalLayout.addWidget(self.button_play_video)
        self.button_pause_video = QtWidgets.QPushButton(self.window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pause_video.sizePolicy().hasHeightForWidth())
        self.button_pause_video.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.button_pause_video.setFont(font)
        self.button_pause_video.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_pause_video.setObjectName("button_pause_video")
        self.horizontalLayout.addWidget(self.button_pause_video)
        self.slider_video_duration = QtWidgets.QSlider(self.window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_video_duration.sizePolicy().hasHeightForWidth())
        self.slider_video_duration.setSizePolicy(sizePolicy)
        self.slider_video_duration.setMinimumSize(QtCore.QSize(400, 30))
        self.slider_video_duration.setStyleSheet("background-color: none;")
        self.slider_video_duration.setOrientation(QtCore.Qt.Horizontal)
        self.slider_video_duration.setObjectName("slider_video_duration")
        self.horizontalLayout.addWidget(self.slider_video_duration)
        self.text_time = QtWidgets.QLabel(self.window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_time.sizePolicy().hasHeightForWidth())
        self.text_time.setSizePolicy(sizePolicy)
        self.text_time.setMinimumSize(QtCore.QSize(70, 25))
        self.text_time.setMaximumSize(QtCore.QSize(20, 25))
        self.text_time.setSizeIncrement(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        self.text_time.setFont(font)
        self.text_time.setStyleSheet("background-color: rgb(28, 29, 73);")
        self.text_time.setText("")
        self.text_time.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.text_time.setObjectName("text_time")
        self.horizontalLayout.addWidget(self.text_time)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_previous = QtWidgets.QPushButton(self.window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_previous.sizePolicy().hasHeightForWidth())
        self.button_previous.setSizePolicy(sizePolicy)
        self.button_previous.setMinimumSize(QtCore.QSize(30, 30))
        self.button_previous.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.button_previous.setFont(font)
        self.button_previous.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.button_previous.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_previous.setIcon(icon)
        self.button_previous.setObjectName("button_previous")
        self.horizontalLayout_3.addWidget(self.button_previous)
        self.button_next = QtWidgets.QPushButton(self.window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_next.sizePolicy().hasHeightForWidth())
        self.button_next.setSizePolicy(sizePolicy)
        self.button_next.setMinimumSize(QtCore.QSize(30, 30))
        self.button_next.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.button_next.setFont(font)
        self.button_next.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Images/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_next.setIcon(icon1)
        self.button_next.setObjectName("button_next")
        self.horizontalLayout_3.addWidget(self.button_next)
        self.text_frame_number = QtWidgets.QLabel(self.window)
        self.text_frame_number.setMinimumSize(QtCore.QSize(100, 0))
        self.text_frame_number.setMaximumSize(QtCore.QSize(40, 30))
        self.text_frame_number.setSizeIncrement(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        self.text_frame_number.setFont(font)
        self.text_frame_number.setStyleSheet("background-color: rgb(28, 29, 73);")
        self.text_frame_number.setText("")
        self.text_frame_number.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.text_frame_number.setObjectName("text_frame_number")
        self.horizontalLayout_3.addWidget(self.text_frame_number)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text_nfov_information = QtWidgets.QLabel(self.window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_nfov_information.sizePolicy().hasHeightForWidth())
        self.text_nfov_information.setSizePolicy(sizePolicy)
        self.text_nfov_information.setMaximumSize(QtCore.QSize(16777215, 125))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        self.text_nfov_information.setFont(font)
        self.text_nfov_information.setStyleSheet("background-color:none;")
        self.text_nfov_information.setText("")
        self.text_nfov_information.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.text_nfov_information.setObjectName("text_nfov_information")
        self.verticalLayout_2.addWidget(self.text_nfov_information)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_edit_long_CROI = QtWidgets.QPushButton(self.window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_edit_long_CROI.sizePolicy().hasHeightForWidth())
        self.button_edit_long_CROI.setSizePolicy(sizePolicy)
        self.button_edit_long_CROI.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_edit_long_CROI.setFont(font)
        self.button_edit_long_CROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_edit_long_CROI.setObjectName("button_edit_long_CROI")
        self.horizontalLayout_2.addWidget(self.button_edit_long_CROI)
        self.button_set_init_CROI = QtWidgets.QPushButton(self.window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_set_init_CROI.sizePolicy().hasHeightForWidth())
        self.button_set_init_CROI.setSizePolicy(sizePolicy)
        self.button_set_init_CROI.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_set_init_CROI.setFont(font)
        self.button_set_init_CROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_set_init_CROI.setObjectName("button_set_init_CROI")
        self.horizontalLayout_2.addWidget(self.button_set_init_CROI)
        self.button_save_CROI = QtWidgets.QPushButton(self.window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_save_CROI.sizePolicy().hasHeightForWidth())
        self.button_save_CROI.setSizePolicy(sizePolicy)
        self.button_save_CROI.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_save_CROI.setFont(font)
        self.button_save_CROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_save_CROI.setObjectName("button_save_CROI")
        self.horizontalLayout_2.addWidget(self.button_save_CROI)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.scroll_area_ROI = QtWidgets.QScrollArea(self.window)
        self.scroll_area_ROI.setMinimumSize(QtCore.QSize(70, 50))
        self.scroll_area_ROI.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scroll_area_ROI.setFont(font)
        self.scroll_area_ROI.setStyleSheet("background-color: rgb(28, 29, 73);")
        self.scroll_area_ROI.setWidgetResizable(True)
        self.scroll_area_ROI.setObjectName("scroll_area_ROI")
        self.scroll_area_ROI_contents = QtWidgets.QWidget()
        self.scroll_area_ROI_contents.setGeometry(QtCore.QRect(0, 0, 262, 198))
        self.scroll_area_ROI_contents.setObjectName("scroll_area_ROI_contents")
        self.scroll_area_ROI.setWidget(self.scroll_area_ROI_contents)
        self.horizontalLayout_6.addWidget(self.scroll_area_ROI)
        self.scroll_area_compose_ROI = QtWidgets.QScrollArea(self.window)
        self.scroll_area_compose_ROI.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scroll_area_compose_ROI.setFont(font)
        self.scroll_area_compose_ROI.setStyleSheet("background-color:rgb(28, 29, 73);")
        self.scroll_area_compose_ROI.setWidgetResizable(True)
        self.scroll_area_compose_ROI.setObjectName("scroll_area_compose_ROI")
        self.scroll_area_ROI_contents_2 = QtWidgets.QWidget()
        self.scroll_area_ROI_contents_2.setGeometry(QtCore.QRect(0, 0, 261, 198))
        self.scroll_area_ROI_contents_2.setObjectName("scroll_area_ROI_contents_2")
        self.scroll_area_compose_ROI.setWidget(self.scroll_area_ROI_contents_2)
        self.horizontalLayout_6.addWidget(self.scroll_area_compose_ROI)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.window)
        self.label_2.setMinimumSize(QtCore.QSize(200, 25))
        self.label_2.setMaximumSize(QtCore.QSize(345, 45))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:none;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.perspective_image = QtWidgets.QLabel(self.window)
        self.perspective_image.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perspective_image.sizePolicy().hasHeightForWidth())
        self.perspective_image.setSizePolicy(sizePolicy)
        self.perspective_image.setMinimumSize(QtCore.QSize(400, 400))
        self.perspective_image.setMaximumSize(QtCore.QSize(400, 400))
        self.perspective_image.setStyleSheet("background-color: rgb(28, 29, 73);")
        self.perspective_image.setText("")
        self.perspective_image.setAlignment(QtCore.Qt.AlignCenter)
        self.perspective_image.setObjectName("perspective_image")
        self.verticalLayout.addWidget(self.perspective_image)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.slider_fov_h = QtWidgets.QSlider(self.window)
        self.slider_fov_h.setMinimumSize(QtCore.QSize(100, 15))
        self.slider_fov_h.setMaximumSize(QtCore.QSize(241, 22))
        self.slider_fov_h.setStyleSheet("background-color:none;")
        self.slider_fov_h.setMinimum(0)
        self.slider_fov_h.setMaximum(100)
        self.slider_fov_h.setPageStep(1)
        self.slider_fov_h.setProperty("value", 30)
        self.slider_fov_h.setOrientation(QtCore.Qt.Horizontal)
        self.slider_fov_h.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_fov_h.setTickInterval(1)
        self.slider_fov_h.setObjectName("slider_fov_h")
        self.gridLayout_3.addWidget(self.slider_fov_h, 2, 2, 1, 1)
        self.input_ROI_W = QtWidgets.QLineEdit(self.window)
        self.input_ROI_W.setMinimumSize(QtCore.QSize(30, 15))
        self.input_ROI_W.setMaximumSize(QtCore.QSize(71, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.input_ROI_W.setFont(font)
        self.input_ROI_W.setStyleSheet("")
        self.input_ROI_W.setObjectName("input_ROI_W")
        self.gridLayout_3.addWidget(self.input_ROI_W, 1, 1, 1, 1)
        self.input_ROI_H = QtWidgets.QLineEdit(self.window)
        self.input_ROI_H.setMinimumSize(QtCore.QSize(30, 15))
        self.input_ROI_H.setMaximumSize(QtCore.QSize(71, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.input_ROI_H.setFont(font)
        self.input_ROI_H.setStyleSheet("")
        self.input_ROI_H.setObjectName("input_ROI_H")
        self.gridLayout_3.addWidget(self.input_ROI_H, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.window)
        self.label_4.setMinimumSize(QtCore.QSize(45, 15))
        self.label_4.setMaximumSize(QtCore.QSize(91, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:none;")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.window)
        self.label_3.setMinimumSize(QtCore.QSize(50, 15))
        self.label_3.setMaximumSize(QtCore.QSize(91, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:none;")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.slider_fov_w = QtWidgets.QSlider(self.window)
        self.slider_fov_w.setMinimumSize(QtCore.QSize(100, 15))
        self.slider_fov_w.setMaximumSize(QtCore.QSize(241, 22))
        self.slider_fov_w.setStyleSheet("background-color:none;")
        self.slider_fov_w.setMinimum(0)
        self.slider_fov_w.setMaximum(100)
        self.slider_fov_w.setSingleStep(1)
        self.slider_fov_w.setPageStep(1)
        self.slider_fov_w.setProperty("value", 30)
        self.slider_fov_w.setOrientation(QtCore.Qt.Horizontal)
        self.slider_fov_w.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_fov_w.setTickInterval(1)
        self.slider_fov_w.setObjectName("slider_fov_w")
        self.gridLayout_3.addWidget(self.slider_fov_w, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(self.window)
        self.label_6.setMinimumSize(QtCore.QSize(45, 15))
        self.label_6.setMaximumSize(QtCore.QSize(91, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:none;")
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.slider_pos_x = QtWidgets.QSlider(self.window)
        self.slider_pos_x.setMinimumSize(QtCore.QSize(100, 15))
        self.slider_pos_x.setMaximumSize(QtCore.QSize(311, 25))
        self.slider_pos_x.setStyleSheet("background-color:none;")
        self.slider_pos_x.setMinimum(0)
        self.slider_pos_x.setMaximum(1450)
        self.slider_pos_x.setSingleStep(1)
        self.slider_pos_x.setPageStep(1)
        self.slider_pos_x.setProperty("value", 0)
        self.slider_pos_x.setOrientation(QtCore.Qt.Horizontal)
        self.slider_pos_x.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_pos_x.setTickInterval(1)
        self.slider_pos_x.setObjectName("slider_pos_x")
        self.gridLayout_4.addWidget(self.slider_pos_x, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.window)
        self.label_5.setMinimumSize(QtCore.QSize(45, 15))
        self.label_5.setMaximumSize(QtCore.QSize(91, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:none;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)
        self.slider_pos_y = QtWidgets.QSlider(self.window)
        self.slider_pos_y.setMinimumSize(QtCore.QSize(100, 15))
        self.slider_pos_y.setMaximumSize(QtCore.QSize(311, 25))
        self.slider_pos_y.setStyleSheet("background-color:none;")
        self.slider_pos_y.setMinimum(0)
        self.slider_pos_y.setMaximum(725)
        self.slider_pos_y.setPageStep(1)
        self.slider_pos_y.setProperty("value", 0)
        self.slider_pos_y.setOrientation(QtCore.Qt.Horizontal)
        self.slider_pos_y.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_pos_y.setTickInterval(1)
        self.slider_pos_y.setObjectName("slider_pos_y")
        self.gridLayout_4.addWidget(self.slider_pos_y, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.label_15 = QtWidgets.QLabel(self.window)
        self.label_15.setMinimumSize(QtCore.QSize(200, 25))
        self.label_15.setMaximumSize(QtCore.QSize(341, 25))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color:none;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_end_ROI = QtWidgets.QPushButton(self.window)
        self.button_end_ROI.setMinimumSize(QtCore.QSize(1, 0))
        self.button_end_ROI.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_end_ROI.setFont(font)
        self.button_end_ROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_end_ROI.setObjectName("button_end_ROI")
        self.gridLayout_2.addWidget(self.button_end_ROI, 0, 1, 1, 1)
        self.button_delete_compose_ROI = QtWidgets.QPushButton(self.window)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_delete_compose_ROI.setFont(font)
        self.button_delete_compose_ROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_delete_compose_ROI.setObjectName("button_delete_compose_ROI")
        self.gridLayout_2.addWidget(self.button_delete_compose_ROI, 5, 1, 1, 1)
        self.button_edit_one_compose_ROI = QtWidgets.QPushButton(self.window)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_edit_one_compose_ROI.setFont(font)
        self.button_edit_one_compose_ROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_edit_one_compose_ROI.setObjectName("button_edit_one_compose_ROI")
        self.gridLayout_2.addWidget(self.button_edit_one_compose_ROI, 1, 0, 1, 1)
        self.button_add_compose_roi = QtWidgets.QPushButton(self.window)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_add_compose_roi.setFont(font)
        self.button_add_compose_roi.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_add_compose_roi.setObjectName("button_add_compose_roi")
        self.gridLayout_2.addWidget(self.button_add_compose_roi, 3, 0, 1, 1)
        self.button_cancel_edit_compose_ROI = QtWidgets.QPushButton(self.window)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_cancel_edit_compose_ROI.setFont(font)
        self.button_cancel_edit_compose_ROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_cancel_edit_compose_ROI.setObjectName("button_cancel_edit_compose_ROI")
        self.gridLayout_2.addWidget(self.button_cancel_edit_compose_ROI, 5, 0, 1, 1)
        self.button_init_ROI = QtWidgets.QPushButton(self.window)
        self.button_init_ROI.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_init_ROI.setFont(font)
        self.button_init_ROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_init_ROI.setObjectName("button_init_ROI")
        self.gridLayout_2.addWidget(self.button_init_ROI, 0, 0, 1, 1)
        self.button_save_add_ROI = QtWidgets.QPushButton(self.window)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_save_add_ROI.setFont(font)
        self.button_save_add_ROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_save_add_ROI.setObjectName("button_save_add_ROI")
        self.gridLayout_2.addWidget(self.button_save_add_ROI, 3, 1, 1, 1)
        self.button_save_edit_compose_ROI = QtWidgets.QPushButton(self.window)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_save_edit_compose_ROI.setFont(font)
        self.button_save_edit_compose_ROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_save_edit_compose_ROI.setObjectName("button_save_edit_compose_ROI")
        self.gridLayout_2.addWidget(self.button_save_edit_compose_ROI, 1, 1, 1, 1)
        self.button_add_new_CROI = QtWidgets.QPushButton(self.window)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_add_new_CROI.setFont(font)
        self.button_add_new_CROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_add_new_CROI.setObjectName("button_add_new_CROI")
        self.gridLayout_2.addWidget(self.button_add_new_CROI, 2, 0, 1, 1)
        self.button_set_new_CROI = QtWidgets.QPushButton(self.window)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_set_new_CROI.setFont(font)
        self.button_set_new_CROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_set_new_CROI.setObjectName("button_set_new_CROI")
        self.gridLayout_2.addWidget(self.button_set_new_CROI, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.label_16 = QtWidgets.QLabel(self.window)
        self.label_16.setMinimumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color:none;")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_edit_ROI = QtWidgets.QPushButton(self.window)
        self.button_edit_ROI.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_edit_ROI.setFont(font)
        self.button_edit_ROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_edit_ROI.setObjectName("button_edit_ROI")
        self.horizontalLayout_5.addWidget(self.button_edit_ROI)
        self.button_save_edit = QtWidgets.QPushButton(self.window)
        self.button_save_edit.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_save_edit.setFont(font)
        self.button_save_edit.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_save_edit.setObjectName("button_save_edit")
        self.horizontalLayout_5.addWidget(self.button_save_edit)
        self.button_cancel_edit = QtWidgets.QPushButton(self.window)
        self.button_cancel_edit.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_cancel_edit.setFont(font)
        self.button_cancel_edit.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_cancel_edit.setObjectName("button_cancel_edit")
        self.horizontalLayout_5.addWidget(self.button_cancel_edit)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_save_ROI = QtWidgets.QPushButton(self.window)
        self.button_save_ROI.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_save_ROI.setFont(font)
        self.button_save_ROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_save_ROI.setObjectName("button_save_ROI")
        self.horizontalLayout_4.addWidget(self.button_save_ROI)
        self.button_delete_ROI = QtWidgets.QPushButton(self.window)
        self.button_delete_ROI.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_delete_ROI.setFont(font)
        self.button_delete_ROI.setStyleSheet("background-color: rgb(0, 0, 100);")
        self.button_delete_ROI.setObjectName("button_delete_ROI")
        self.horizontalLayout_4.addWidget(self.button_delete_ROI)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        Anottation.setCentralWidget(self.window)
        self.menubar = QtWidgets.QMenuBar(Anottation)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1319, 26))
        self.menubar.setObjectName("menubar")
        self.menuUpload = QtWidgets.QMenu(self.menubar)
        self.menuUpload.setObjectName("menuUpload")
        Anottation.setMenuBar(self.menubar)
        self.button_upload_image = QtWidgets.QAction(Anottation)
        self.button_upload_image.setObjectName("button_upload_image")
        self.button_upload_folder = QtWidgets.QAction(Anottation)
        self.button_upload_folder.setObjectName("button_upload_folder")
        self.button_upload_video = QtWidgets.QAction(Anottation)
        self.button_upload_video.setObjectName("button_upload_video")
        self.button_save = QtWidgets.QAction(Anottation)
        self.button_save.setObjectName("button_save")
        self.button_upload_Annotations = QtWidgets.QAction(Anottation)
        self.button_upload_Annotations.setObjectName("button_upload_Annotations")
        self.menuUpload.addAction(self.button_upload_image)
        self.menuUpload.addAction(self.button_upload_folder)
        self.menuUpload.addAction(self.button_upload_video)
        self.menuUpload.addAction(self.button_upload_Annotations)
        self.menuUpload.addAction(self.button_save)
        self.menubar.addAction(self.menuUpload.menuAction())

        self.retranslateUi(Anottation)
        QtCore.QMetaObject.connectSlotsByName(Anottation)

    def retranslateUi(self, Anottation):
        _translate = QtCore.QCoreApplication.translate
        Anottation.setWindowTitle(_translate("Anottation", "MainWindow"))
        self.button_go_to_first.setText(_translate("Anottation", "First ROI"))
        self.button_go_to_last.setText(_translate("Anottation", "Last ROI"))
        self.label.setText(_translate("Anottation", "Equirectangular View"))
        self.button_play_video.setText(_translate("Anottation", "Play"))
        self.button_pause_video.setText(_translate("Anottation", "Pause"))
        self.button_edit_long_CROI.setText(_translate("Anottation", "Edit long ROI"))
        self.button_set_init_CROI.setText(_translate("Anottation", "Init Frame"))
        self.button_save_CROI.setText(_translate("Anottation", "Save edit"))
        self.label_2.setText(_translate("Anottation", "Perspective View"))
        self.label_4.setText(_translate("Anottation", "ROI H"))
        self.label_3.setText(_translate("Anottation", "ROI W"))
        self.label_6.setText(_translate("Anottation", "POS X"))
        self.label_5.setText(_translate("Anottation", "POS Y"))
        self.label_15.setText(_translate("Anottation", "Compose ROI"))
        self.button_end_ROI.setText(_translate("Anottation", "Save compose ROI"))
        self.button_delete_compose_ROI.setText(_translate("Anottation", "Delete compose ROI"))
        self.button_edit_one_compose_ROI.setText(_translate("Anottation", "Edit one ROI"))
        self.button_add_compose_roi.setText(_translate("Anottation", "Add ROIs"))
        self.button_cancel_edit_compose_ROI.setText(_translate("Anottation", "Cancel"))
        self.button_init_ROI.setText(_translate("Anottation", "Set Init ROI"))
        self.button_save_add_ROI.setText(_translate("Anottation", "Save add ROIs"))
        self.button_save_edit_compose_ROI.setText(_translate("Anottation", "Save Edit"))
        self.button_add_new_CROI.setText(_translate("Anottation", "Add new \n"
" compose ROI"))
        self.button_set_new_CROI.setText(_translate("Anottation", "Set Init \n"
" Add ROI"))
        self.label_16.setText(_translate("Anottation", "Single ROI"))
        self.button_edit_ROI.setText(_translate("Anottation", "Edit"))
        self.button_save_edit.setText(_translate("Anottation", "Save Edit"))
        self.button_cancel_edit.setText(_translate("Anottation", "Cancel Edit"))
        self.button_save_ROI.setText(_translate("Anottation", "Save"))
        self.button_delete_ROI.setText(_translate("Anottation", "Delete"))
        self.menuUpload.setTitle(_translate("Anottation", "File"))
        self.button_upload_image.setText(_translate("Anottation", "Upload Image"))
        self.button_upload_folder.setText(_translate("Anottation", "Upload Folder"))
        self.button_upload_video.setText(_translate("Anottation", "Upload Video"))
        self.button_save.setText(_translate("Anottation", "Save"))
        self.button_upload_Annotations.setText(_translate("Anottation", "Upload Annotations"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Anottation = QtWidgets.QMainWindow()
    ui = Ui_Anottation()
    ui.setupUi(Anottation)
    Anottation.show()
    sys.exit(app.exec_())
