# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1387, 853)
        MainWindow.setMinimumSize(QSize(940, 605))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Open Sans"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 12pt \"Open Sans\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	backgroun"
                        "d-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(1"
                        "89, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb"
                        "(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	borde"
                        "r-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-st"
                        "yle: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rg"
                        "b(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget \n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-col"
                        "or: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"*/\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-"
                        "color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"background-color: rgb(189, 147, 249);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-p"
                        "osition: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: "
                        "10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"\n"
"/* Sliders DISABLED!!!! */\n"
"QSlider::groove:horizontal:disabled {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
""
                        "    background-color: rgb(150, 150, 150); /* \u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0433\u043e \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430 */\n"
"}\n"
"QSlider::groove:horizontal:disabled:hover {\n"
"    background-color: rgb(150, 150, 150); /* \u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0433\u043e \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"QSlider::handle:horizontal:disabled {\n"
"    background-color: rgb(100, 100, 100); /* \u0426\u0432\u0435\u0442 \u0440\u0443\u0447\u043a\u0438 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0433\u043e \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430 */\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:disabled:hover {\n"
"    background"
                        "-color: rgb(100, 100, 100); /* \u0426\u0432\u0435\u0442 \u0440\u0443\u0447\u043a\u0438 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0433\u043e \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"QSlider::handle:horizontal:disabled:pressed {\n"
"    background-color: rgb(100, 100, 100); /* \u0426\u0432\u0435\u0442 \u0440\u0443\u0447\u043a\u0438 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0433\u043e \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"\n"
"QSlider::groove:vertical:disabled {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    background-color: rgb(150, 150, 150); /* \u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0433\u043e \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430 */\n"
"}\n"
"QSlider::groove:vertic"
                        "al:disabled:hover {\n"
"    background-color: rgb(150, 150, 150); /* \u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0433\u043e \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"QSlider::handle:vertical:disabled {\n"
"    background-color: rgb(100, 100, 100); /* \u0426\u0432\u0435\u0442 \u0440\u0443\u0447\u043a\u0438 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0433\u043e \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430 */\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:disabled:hover {\n"
"    background-color: rgb(100, 100, 100); /* \u0426\u0432\u0435\u0442 \u0440\u0443\u0447\u043a\u0438 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0433\u043e \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430 \u043f\u0440\u0438 \u043d"
                        "\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"QSlider::handle:vertical:disabled:pressed {\n"
"    background-color: rgb(100, 100, 100); /* \u0426\u0432\u0435\u0442 \u0440\u0443\u0447\u043a\u0438 \u0434\u043b\u044f \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0433\u043e \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////"
                        "////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Scrollbox */\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: rgb(170, 170, 0);\n"
"	width: 7px;  /* \u0422\u041e\u041b\u0429\u0418\u041d\u0410 */\n"
"	margin: 5px 0 5px 0;  /* \u041e\u0422\u0421\u0422\u0423\u041f\u042b */\n"
"	border-radius: 3px; /* \u0421\u041a\u0420\u0423\u0413\u041b\u0415\u041d\u0418\u042f */\n"
"}\n"
"\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 12"
                        "2);\n"
"	min-height: 30px;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {	\n"
"	background-color: rgb(90, 90, 138);\n"
"}                                                                             /*\u0426\u0432\u0435\u0442\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438*/\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(90, 90, 138);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	height: 0px;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"/*####################################*/\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: rgb"
                        "(45, 45, 68);\n"
"	height: 7px;  /* \u0422\u041e\u041b\u0429\u0418\u041d\u0410 */\n"
"	margin: 0 7px 0 15px;  /* \u041e\u0422\u0421\u0422\u0423\u041f\u042b */\n"
"	border-radius: 3px; /* \u0421\u041a\u0420\u0423\u0413\u041b\u0415\u041d\u0418\u042f */\n"
"}\n"
"QScrollBar::handle:horizontal {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-width: 30px;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {	\n"
"	background-color: rgb(90, 90, 138);\n"
"}                                                                             /*\u0426\u0432\u0435\u0442\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438*/\n"
"QScrollBar::handle:horizontal:pressed {	\n"
"	background-color: rgb(90, 90, 138);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-arrow:horizontal {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"	ba"
                        "ckground: none;\n"
"}\n"
"\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal {\n"
"	height: 0px;\n"
"}                                                                             /*\u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0441\u0442\u0440\u0435\u043b\u043e\u0447\u043a\u0438*/\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
"	height: 0px;\n"
"}\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"font: 10pt \"Open Sans\";")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Open Sans"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        self.titleLeftDescription.setFont(font1)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font1)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_add = QPushButton(self.topMenu)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setMinimumSize(QSize(0, 45))
        self.btn_add.setFont(font1)
        self.btn_add.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add.setLayoutDirection(Qt.LeftToRight)
        self.btn_add.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user-follow.png);")

        self.verticalLayout_8.addWidget(self.btn_add)

        self.btn_base = QPushButton(self.topMenu)
        self.btn_base.setObjectName(u"btn_base")
        sizePolicy.setHeightForWidth(self.btn_base.sizePolicy().hasHeightForWidth())
        self.btn_base.setSizePolicy(sizePolicy)
        self.btn_base.setMinimumSize(QSize(0, 45))
        self.btn_base.setFont(font1)
        self.btn_base.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_base.setLayoutDirection(Qt.LeftToRight)
        self.btn_base.setStyleSheet(u"\n"
"background-image: url(:/icons/images/icons/cil-people.png);")

        self.verticalLayout_8.addWidget(self.btn_base)

        self.btn_locations = QPushButton(self.topMenu)
        self.btn_locations.setObjectName(u"btn_locations")
        sizePolicy.setHeightForWidth(self.btn_locations.sizePolicy().hasHeightForWidth())
        self.btn_locations.setSizePolicy(sizePolicy)
        self.btn_locations.setMinimumSize(QSize(0, 45))
        self.btn_locations.setFont(font1)
        self.btn_locations.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_locations.setLayoutDirection(Qt.LeftToRight)
        self.btn_locations.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-location-pin.png);")

        self.verticalLayout_8.addWidget(self.btn_locations)

        self.btn_history = QPushButton(self.topMenu)
        self.btn_history.setObjectName(u"btn_history")
        sizePolicy.setHeightForWidth(self.btn_history.sizePolicy().hasHeightForWidth())
        self.btn_history.setSizePolicy(sizePolicy)
        self.btn_history.setMinimumSize(QSize(0, 45))
        self.btn_history.setFont(font1)
        self.btn_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_history.setLayoutDirection(Qt.LeftToRight)
        self.btn_history.setStyleSheet(u"\n"
"background-image: url(:/icons/images/icons/cil-history.png);")

        self.verticalLayout_8.addWidget(self.btn_history)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font1)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-speech.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setMinimumSize(QSize(0, 0))
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font1)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font1)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font1)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)

        self.extraCenter.raise_()
        self.extraBottom.raise_()
        self.extraTopMenu.raise_()

        self.extraColumLayout.addWidget(self.extraContent)

        self.extraContent.raise_()
        self.extraTopBg.raise_()

        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font2 = QFont()
        font2.setFamilies([u"Open Sans Medium"])
        font2.setPointSize(13)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleRightInfo.setFont(font2)
        self.titleRightInfo.setStyleSheet(u"font: 57 13pt \"Open Sans Medium\";")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setFont(font1)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.home.setInputMethodHints(Qt.ImhLatinOnly|Qt.ImhTime)
        self.horizontalLayout_6 = QHBoxLayout(self.home)
        self.horizontalLayout_6.setSpacing(9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.home_video_place = QLabel(self.home)
        self.home_video_place.setObjectName(u"home_video_place")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.home_video_place.sizePolicy().hasHeightForWidth())
        self.home_video_place.setSizePolicy(sizePolicy3)
        self.home_video_place.setMinimumSize(QSize(0, 0))
        self.home_video_place.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;")
        self.home_video_place.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.home_video_place)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_2 = QWidget(self.home)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(50)
        sizePolicy4.setVerticalStretch(50)
        sizePolicy4.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy4)
        self.widget_2.setMaximumSize(QSize(16000, 16777215))
        self.widget_2.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(33, 37, 43);")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_15 = QLabel(self.widget_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 1, 0, 1, 1)

        self.home_name = QLineEdit(self.widget_2)
        self.home_name.setObjectName(u"home_name")
        self.home_name.setEnabled(False)
        self.home_name.setStyleSheet(u"border-color: rgb(40, 44, 52);")

        self.gridLayout_3.addWidget(self.home_name, 1, 1, 1, 1)

        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)

        self.home_age = QLineEdit(self.widget_2)
        self.home_age.setObjectName(u"home_age")
        self.home_age.setEnabled(False)
        self.home_age.setStyleSheet(u"border-color: rgb(40, 44, 52);")

        self.gridLayout_3.addWidget(self.home_age, 2, 1, 1, 1)

        self.home_photo_place = QLabel(self.widget_2)
        self.home_photo_place.setObjectName(u"home_photo_place")
        sizePolicy4.setHeightForWidth(self.home_photo_place.sizePolicy().hasHeightForWidth())
        self.home_photo_place.setSizePolicy(sizePolicy4)
        self.home_photo_place.setMinimumSize(QSize(190, 0))
        self.home_photo_place.setMaximumSize(QSize(16000000, 16777215))
        self.home_photo_place.setStyleSheet(u"background-color: rgb(40, 44, 52);\n"
"border-radius: 10px;\n"
"")
        self.home_photo_place.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.home_photo_place, 0, 0, 1, 2)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 4, 0, 1, 1)

        self.home_department = QLineEdit(self.widget_2)
        self.home_department.setObjectName(u"home_department")
        self.home_department.setEnabled(False)
        self.home_department.setStyleSheet(u"border-color: rgb(40, 44, 52);")

        self.gridLayout_3.addWidget(self.home_department, 4, 1, 1, 1)

        self.home_level_access = QLineEdit(self.widget_2)
        self.home_level_access.setObjectName(u"home_level_access")
        self.home_level_access.setEnabled(False)
        self.home_level_access.setStyleSheet(u"border-color: rgb(40, 44, 52);")

        self.gridLayout_3.addWidget(self.home_level_access, 5, 1, 1, 1)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)

        self.home_gender = QLineEdit(self.widget_2)
        self.home_gender.setObjectName(u"home_gender")
        self.home_gender.setEnabled(False)
        self.home_gender.setStyleSheet(u"border-color: rgb(40, 44, 52);")

        self.gridLayout_3.addWidget(self.home_gender, 3, 1, 1, 1)

        self.gridLayout_3.setRowStretch(0, 5)
        self.gridLayout_3.setRowStretch(1, 2)
        self.gridLayout_3.setRowStretch(2, 1)
        self.gridLayout_3.setRowStretch(3, 1)
        self.gridLayout_3.setRowStretch(4, 1)
        self.gridLayout_3.setRowStretch(5, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 2)

        self.verticalLayout_21.addWidget(self.widget_2)

        self.home_start_system = QPushButton(self.home)
        self.home_start_system.setObjectName(u"home_start_system")
        self.home_start_system.setMinimumSize(QSize(0, 30))
        self.home_start_system.setFont(font1)
        self.home_start_system.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_21.addWidget(self.home_start_system)


        self.horizontalLayout_6.addLayout(self.verticalLayout_21)

        self.horizontalLayout_6.setStretch(0, 5)
        self.horizontalLayout_6.setStretch(1, 2)
        self.stackedWidget.addWidget(self.home)
        self.base = QWidget()
        self.base.setObjectName(u"base")
        self.base.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.base)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.row_1 = QFrame(self.base)
        self.row_1.setObjectName(u"row_1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.row_1.sizePolicy().hasHeightForWidth())
        self.row_1.setSizePolicy(sizePolicy5)
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.view_linestring = QLineEdit(self.frame_content_wid_1)
        self.view_linestring.setObjectName(u"view_linestring")
        self.view_linestring.setMinimumSize(QSize(0, 30))
        self.view_linestring.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.view_linestring, 0, 0, 1, 1)

        self.view_search_button = QPushButton(self.frame_content_wid_1)
        self.view_search_button.setObjectName(u"view_search_button")
        self.view_search_button.setMinimumSize(QSize(150, 30))
        self.view_search_button.setFont(font1)
        self.view_search_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.view_search_button.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.view_search_button.setIcon(icon4)

        self.gridLayout.addWidget(self.view_search_button, 0, 2, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 3)

        self.view_search_type = QComboBox(self.frame_content_wid_1)
        self.view_search_type.addItem("")
        self.view_search_type.addItem("")
        self.view_search_type.addItem("")
        self.view_search_type.setObjectName(u"view_search_type")
        self.view_search_type.setFont(font1)
        self.view_search_type.setAutoFillBackground(False)
        self.view_search_type.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.view_search_type.setIconSize(QSize(16, 16))
        self.view_search_type.setFrame(True)

        self.gridLayout.addWidget(self.view_search_type, 0, 1, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_3 = QFrame(self.base)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setStyleSheet(u" QScrollBar:vertical, \n"
" QScrollBar:horizontal {\n"
"	border: none;\n"
"    background: rgb(56, 56, 85);\n"
" }")
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.view_tabble = QTableWidget(self.row_3)
        if (self.view_tabble.columnCount() < 6):
            self.view_tabble.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.view_tabble.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.view_tabble.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.view_tabble.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.view_tabble.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.view_tabble.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.view_tabble.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.view_tabble.rowCount() < 1):
            self.view_tabble.setRowCount(1)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self.view_tabble.setVerticalHeaderItem(0, __qtablewidgetitem6)
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        self.view_tabble.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font4);
        self.view_tabble.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font4);
        self.view_tabble.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font4);
        self.view_tabble.setItem(0, 3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font4);
        self.view_tabble.setItem(0, 4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font4);
        self.view_tabble.setItem(0, 5, __qtablewidgetitem12)
        self.view_tabble.setObjectName(u"view_tabble")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.view_tabble.sizePolicy().hasHeightForWidth())
        self.view_tabble.setSizePolicy(sizePolicy6)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(33, 37, 43, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.view_tabble.setPalette(palette)
        self.view_tabble.setFont(font1)
        self.view_tabble.setStyleSheet(u"QTableWidget {\n"
" /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"	background-color: rgb(33, 37, 43);\n"
"    border: none;\n"
"    gridline-color: rgb(55, 60, 70); /* \u0426\u0432\u0435\u0442 \u0441\u0435\u0442\u043a\u0438 */\n"
"    border-radius: 13px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432 */\n"
"	padding: 5px;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 5px;\n"
"    border-bottom: 1px solid rgb(55, 60, 70); /* \u041b\u0438\u043d\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u044f\u0447\u0435\u0439\u043a\u0430\u043c\u0438 */\n"
"    border-right: 1px solid rgb(55, 60, 70); /* \u041b\u0438\u043d\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u044f\u0447\u0435\u0439\u043a\u0430\u043c\u0438 */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(69, 79, 97); /* \u0426\u0432\u0435\u0442 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0439 \u044f\u0447\u0435\u0439\u043a\u0438 */\n"
"}\n"
"\n"
""
                        "QTableWidget::item:selected:active {\n"
"    background-color: rgb(61, 70, 86); /* \u0426\u0432\u0435\u0442 \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0439 \u044f\u0447\u0435\u0439\u043a\u0438 */\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*####################################*/\n"
"\n"
" QScrollBar:vertical, \n"
" QScrollBar:horizontal {\n"
"	border: none;\n"
"    background: rgb(56, 56, 85);\n"
" }\n"
"")
        self.view_tabble.setFrameShape(QFrame.NoFrame)
        self.view_tabble.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.view_tabble.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.view_tabble.setAutoScroll(False)
        self.view_tabble.setAutoScrollMargin(30)
        self.view_tabble.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.view_tabble.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.view_tabble.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.view_tabble.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.view_tabble.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.view_tabble.setShowGrid(True)
        self.view_tabble.setGridStyle(Qt.SolidLine)
        self.view_tabble.setSortingEnabled(False)
        self.view_tabble.setWordWrap(True)
        self.view_tabble.setCornerButtonEnabled(True)
        self.view_tabble.horizontalHeader().setVisible(False)
        self.view_tabble.horizontalHeader().setCascadingSectionResizes(True)
        self.view_tabble.horizontalHeader().setDefaultSectionSize(200)
        self.view_tabble.horizontalHeader().setHighlightSections(True)
        self.view_tabble.horizontalHeader().setStretchLastSection(True)
        self.view_tabble.verticalHeader().setVisible(False)
        self.view_tabble.verticalHeader().setCascadingSectionResizes(False)
        self.view_tabble.verticalHeader().setHighlightSections(False)
        self.view_tabble.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_12.addWidget(self.view_tabble)


        self.verticalLayout.addWidget(self.row_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, -1, 25, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.view_edit = QPushButton(self.base)
        self.view_edit.setObjectName(u"view_edit")
        self.view_edit.setMinimumSize(QSize(0, 30))
        self.view_edit.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_8.addWidget(self.view_edit)

        self.view_dellete = QPushButton(self.base)
        self.view_dellete.setObjectName(u"view_dellete")
        self.view_dellete.setMinimumSize(QSize(0, 30))
        self.view_dellete.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_8.addWidget(self.view_dellete)

        self.horizontalLayout_8.setStretch(0, 5)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.stackedWidget.addWidget(self.base)
        self.history = QWidget()
        self.history.setObjectName(u"history")
        self.verticalLayout_20 = QVBoxLayout(self.history)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.labelBoxBlenderInstalation_2 = QLabel(self.history)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        self.labelBoxBlenderInstalation_2.setFont(font1)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"margin-left: 10")

        self.verticalLayout_20.addWidget(self.labelBoxBlenderInstalation_2)

        self.frame_content_wid_2 = QFrame(self.history)
        self.frame_content_wid_2.setObjectName(u"frame_content_wid_2")
        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_content_wid_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.history_linestring = QLineEdit(self.frame_content_wid_2)
        self.history_linestring.setObjectName(u"history_linestring")
        self.history_linestring.setMinimumSize(QSize(0, 30))
        self.history_linestring.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_7.addWidget(self.history_linestring, 0, 0, 1, 1)

        self.history_search_button = QPushButton(self.frame_content_wid_2)
        self.history_search_button.setObjectName(u"history_search_button")
        self.history_search_button.setMinimumSize(QSize(150, 30))
        self.history_search_button.setFont(font1)
        self.history_search_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.history_search_button.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.history_search_button.setIcon(icon4)

        self.gridLayout_7.addWidget(self.history_search_button, 0, 2, 1, 1)

        self.labelVersion_4 = QLabel(self.frame_content_wid_2)
        self.labelVersion_4.setObjectName(u"labelVersion_4")
        self.labelVersion_4.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.labelVersion_4, 1, 0, 1, 3)

        self.history_search_type = QComboBox(self.frame_content_wid_2)
        self.history_search_type.addItem("")
        self.history_search_type.addItem("")
        self.history_search_type.addItem("")
        self.history_search_type.setObjectName(u"history_search_type")
        self.history_search_type.setFont(font1)
        self.history_search_type.setAutoFillBackground(False)
        self.history_search_type.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.history_search_type.setIconSize(QSize(16, 16))
        self.history_search_type.setFrame(True)

        self.gridLayout_7.addWidget(self.history_search_type, 0, 1, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_7)


        self.verticalLayout_20.addWidget(self.frame_content_wid_2)

        self.histiry_table = QTableWidget(self.history)
        if (self.histiry_table.columnCount() < 6):
            self.histiry_table.setColumnCount(6)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.histiry_table.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.histiry_table.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.histiry_table.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.histiry_table.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.histiry_table.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.histiry_table.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        if (self.histiry_table.rowCount() < 1):
            self.histiry_table.setRowCount(1)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font3);
        self.histiry_table.setVerticalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font4);
        self.histiry_table.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font4);
        self.histiry_table.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font4);
        self.histiry_table.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font4);
        self.histiry_table.setItem(0, 3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font4);
        self.histiry_table.setItem(0, 4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font4);
        self.histiry_table.setItem(0, 5, __qtablewidgetitem25)
        self.histiry_table.setObjectName(u"histiry_table")
        sizePolicy6.setHeightForWidth(self.histiry_table.sizePolicy().hasHeightForWidth())
        self.histiry_table.setSizePolicy(sizePolicy6)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.histiry_table.setPalette(palette1)
        self.histiry_table.setFont(font1)
        self.histiry_table.setStyleSheet(u"QTableWidget {\n"
" /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"	background-color: rgb(33, 37, 43);\n"
"    border: none;\n"
"    gridline-color: rgb(55, 60, 70); /* \u0426\u0432\u0435\u0442 \u0441\u0435\u0442\u043a\u0438 */\n"
"    border-radius: 13px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u043a\u0440\u0430\u0435\u0432 */\n"
"	padding: 5px;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 5px;\n"
"    border-bottom: 1px solid rgb(55, 60, 70); /* \u041b\u0438\u043d\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u044f\u0447\u0435\u0439\u043a\u0430\u043c\u0438 */\n"
"    border-right: 1px solid rgb(55, 60, 70); /* \u041b\u0438\u043d\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u044f\u0447\u0435\u0439\u043a\u0430\u043c\u0438 */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(69, 79, 97); /* \u0426\u0432\u0435\u0442 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0439 \u044f\u0447\u0435\u0439\u043a\u0438 */\n"
"}\n"
"\n"
""
                        "QTableWidget::item:selected:active {\n"
"    background-color: rgb(61, 70, 86); /* \u0426\u0432\u0435\u0442 \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0439 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u043e\u0439 \u044f\u0447\u0435\u0439\u043a\u0438 */\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*####################################*/\n"
"\n"
" QScrollBar:vertical, \n"
" QScrollBar:horizontal {\n"
"	border: none;\n"
"    background: rgb(56, 56, 85);\n"
" }\n"
"")
        self.histiry_table.setFrameShape(QFrame.NoFrame)
        self.histiry_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.histiry_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.histiry_table.setAutoScroll(False)
        self.histiry_table.setAutoScrollMargin(30)
        self.histiry_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.histiry_table.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.histiry_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.histiry_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.histiry_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.histiry_table.setShowGrid(True)
        self.histiry_table.setGridStyle(Qt.SolidLine)
        self.histiry_table.setSortingEnabled(False)
        self.histiry_table.setWordWrap(True)
        self.histiry_table.setCornerButtonEnabled(True)
        self.histiry_table.horizontalHeader().setVisible(False)
        self.histiry_table.horizontalHeader().setCascadingSectionResizes(True)
        self.histiry_table.horizontalHeader().setDefaultSectionSize(200)
        self.histiry_table.horizontalHeader().setHighlightSections(True)
        self.histiry_table.horizontalHeader().setStretchLastSection(True)
        self.histiry_table.verticalHeader().setVisible(False)
        self.histiry_table.verticalHeader().setCascadingSectionResizes(False)
        self.histiry_table.verticalHeader().setHighlightSections(False)
        self.histiry_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_20.addWidget(self.histiry_table)

        self.stackedWidget.addWidget(self.history)
        self.location = QWidget()
        self.location.setObjectName(u"location")
        self.gridLayout_10 = QGridLayout(self.location)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalSpacer_10 = QSpacerItem(20, 232, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_10, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(309, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(15)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_60 = QLabel(self.location)
        self.label_60.setObjectName(u"label_60")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy7)
        self.label_60.setFont(font1)
        self.label_60.setStyleSheet(u"\n"
"padding: 0px;\n"
"margin: 0px;")
        self.label_60.setAlignment(Qt.AlignCenter)
        self.label_60.setMargin(5)

        self.verticalLayout_23.addWidget(self.label_60)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_59 = QLabel(self.location)
        self.label_59.setObjectName(u"label_59")
        sizePolicy2.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy2)
        self.label_59.setMinimumSize(QSize(129, 0))
        self.label_59.setStyleSheet(u"font: 12pt \"Open Sans\";\n"
"margin-left:10px;")
        self.label_59.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_59)

        self.choose_location_choose = QComboBox(self.location)
        self.choose_location_choose.setObjectName(u"choose_location_choose")
        self.choose_location_choose.setMinimumSize(QSize(0, 48))
        self.choose_location_choose.setMaximumSize(QSize(16777215, 48))
        self.choose_location_choose.setFont(font1)
        self.choose_location_choose.setAutoFillBackground(False)
        self.choose_location_choose.setStyleSheet(u"\n"
"margin: 7px;\n"
"background-color: rgb(33, 37, 43);")
        self.choose_location_choose.setIconSize(QSize(16, 16))
        self.choose_location_choose.setFrame(True)

        self.horizontalLayout_16.addWidget(self.choose_location_choose)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 3)

        self.verticalLayout_23.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_58 = QLabel(self.location)
        self.label_58.setObjectName(u"label_58")
        sizePolicy2.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy2)
        self.label_58.setStyleSheet(u"font: 12pt \"Open Sans\";\n"
"margin-left:10px;")

        self.horizontalLayout_18.addWidget(self.label_58)

        self.choose_location_access_level = QLineEdit(self.location)
        self.choose_location_access_level.setObjectName(u"choose_location_access_level")
        self.choose_location_access_level.setEnabled(False)
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.choose_location_access_level.sizePolicy().hasHeightForWidth())
        self.choose_location_access_level.setSizePolicy(sizePolicy8)
        self.choose_location_access_level.setMinimumSize(QSize(0, 48))
        self.choose_location_access_level.setMaximumSize(QSize(16777215, 48))
        self.choose_location_access_level.setStyleSheet(u"margin: 7px;\n"
"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_18.addWidget(self.choose_location_access_level)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 3)

        self.verticalLayout_23.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 10, -1, -1)
        self.choose_location_delete = QPushButton(self.location)
        self.choose_location_delete.setObjectName(u"choose_location_delete")
        sizePolicy8.setHeightForWidth(self.choose_location_delete.sizePolicy().hasHeightForWidth())
        self.choose_location_delete.setSizePolicy(sizePolicy8)
        self.choose_location_delete.setMinimumSize(QSize(120, 35))
        self.choose_location_delete.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(221, 221, 221);\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(57, 65, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(33, 37, 43);\n"
"}")

        self.horizontalLayout_17.addWidget(self.choose_location_delete)

        self.choose_location_addnew = QPushButton(self.location)
        self.choose_location_addnew.setObjectName(u"choose_location_addnew")
        sizePolicy8.setHeightForWidth(self.choose_location_addnew.sizePolicy().hasHeightForWidth())
        self.choose_location_addnew.setSizePolicy(sizePolicy8)
        self.choose_location_addnew.setMinimumSize(QSize(120, 35))
        self.choose_location_addnew.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(221, 221, 221);\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(57, 65, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(33, 37, 43);\n"
"}")

        self.horizontalLayout_17.addWidget(self.choose_location_addnew)

        self.choose_location_apply = QPushButton(self.location)
        self.choose_location_apply.setObjectName(u"choose_location_apply")
        self.choose_location_apply.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.choose_location_apply.sizePolicy().hasHeightForWidth())
        self.choose_location_apply.setSizePolicy(sizePolicy8)
        self.choose_location_apply.setMinimumSize(QSize(120, 35))
        self.choose_location_apply.setStyleSheet(u"/* \u041a\u043d\u043e\u043f\u043a\u0430 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f (OK) */\n"
"QPushButton {\n"
"    background-color: rgb(189, 147, 249);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(164, 118, 233);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(139, 88, 217);\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: rgb(128, 128, 128); /* \u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}")

        self.horizontalLayout_17.addWidget(self.choose_location_apply)


        self.verticalLayout_23.addLayout(self.horizontalLayout_17)

        self.verticalLayout_23.setStretch(1, 1)
        self.verticalLayout_23.setStretch(3, 1)

        self.gridLayout_10.addLayout(self.verticalLayout_23, 1, 1, 1, 2)

        self.horizontalSpacer_12 = QSpacerItem(309, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_12, 1, 3, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 232, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_11, 2, 2, 1, 1)

        self.gridLayout_10.setColumnStretch(0, 3)
        self.gridLayout_10.setColumnStretch(1, 3)
        self.gridLayout_10.setColumnStretch(2, 3)
        self.gridLayout_10.setColumnStretch(3, 3)
        self.stackedWidget.addWidget(self.location)
        self.add_location = QWidget()
        self.add_location.setObjectName(u"add_location")
        self.gridLayout_6 = QGridLayout(self.add_location)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_55 = QLabel(self.add_location)
        self.label_55.setObjectName(u"label_55")
        sizePolicy6.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy6)
        self.label_55.setStyleSheet(u"font: 12pt \"Open Sans\";\n"
"margin-left:10px;")

        self.gridLayout_5.addWidget(self.label_55, 0, 0, 1, 1)

        self.add_location_titles = QLineEdit(self.add_location)
        self.add_location_titles.setObjectName(u"add_location_titles")
        sizePolicy8.setHeightForWidth(self.add_location_titles.sizePolicy().hasHeightForWidth())
        self.add_location_titles.setSizePolicy(sizePolicy8)
        self.add_location_titles.setMinimumSize(QSize(0, 48))
        self.add_location_titles.setMaximumSize(QSize(16777215, 48))
        self.add_location_titles.setStyleSheet(u"margin: 7px;\n"
"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.add_location_titles, 0, 1, 1, 1)

        self.label_57 = QLabel(self.add_location)
        self.label_57.setObjectName(u"label_57")
        sizePolicy2.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy2)
        self.label_57.setStyleSheet(u"font: 12pt \"Open Sans\";\n"
"margin-left:10px;")

        self.gridLayout_5.addWidget(self.label_57, 1, 0, 1, 1)

        self.add_location_access = QComboBox(self.add_location)
        self.add_location_access.addItem("")
        self.add_location_access.addItem("")
        self.add_location_access.addItem("")
        self.add_location_access.setObjectName(u"add_location_access")
        self.add_location_access.setMinimumSize(QSize(0, 48))
        self.add_location_access.setMaximumSize(QSize(16777215, 48))
        self.add_location_access.setFont(font1)
        self.add_location_access.setAutoFillBackground(False)
        self.add_location_access.setStyleSheet(u"\n"
"margin: 7px;\n"
"background-color: rgb(33, 37, 43);")
        self.add_location_access.setIconSize(QSize(16, 16))
        self.add_location_access.setFrame(True)

        self.gridLayout_5.addWidget(self.add_location_access, 1, 1, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 2)
        self.gridLayout_5.setColumnStretch(1, 5)

        self.gridLayout_6.addLayout(self.gridLayout_5, 2, 1, 1, 2)

        self.horizontalSpacer_15 = QSpacerItem(315, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_15, 2, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(315, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_16, 2, 3, 1, 1)

        self.label_56 = QLabel(self.add_location)
        self.label_56.setObjectName(u"label_56")
        sizePolicy7.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy7)
        self.label_56.setFont(font1)
        self.label_56.setStyleSheet(u"")
        self.label_56.setAlignment(Qt.AlignCenter)
        self.label_56.setMargin(15)

        self.gridLayout_6.addWidget(self.label_56, 1, 1, 1, 2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(40, -1, 40, -1)
        self.add_location_back = QPushButton(self.add_location)
        self.add_location_back.setObjectName(u"add_location_back")
        sizePolicy8.setHeightForWidth(self.add_location_back.sizePolicy().hasHeightForWidth())
        self.add_location_back.setSizePolicy(sizePolicy8)
        self.add_location_back.setMinimumSize(QSize(120, 35))
        self.add_location_back.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(221, 221, 221);\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(57, 65, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(33, 37, 43);\n"
"}")

        self.horizontalLayout_13.addWidget(self.add_location_back)

        self.add_location_add = QPushButton(self.add_location)
        self.add_location_add.setObjectName(u"add_location_add")
        self.add_location_add.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.add_location_add.sizePolicy().hasHeightForWidth())
        self.add_location_add.setSizePolicy(sizePolicy8)
        self.add_location_add.setMinimumSize(QSize(120, 35))
        self.add_location_add.setStyleSheet(u"/* \u041a\u043d\u043e\u043f\u043a\u0430 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f (OK) */\n"
"QPushButton {\n"
"    background-color: rgb(189, 147, 249);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(164, 118, 233);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(139, 88, 217);\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: rgb(128, 128, 128); /* \u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}")

        self.horizontalLayout_13.addWidget(self.add_location_add)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 1)

        self.gridLayout_6.addLayout(self.horizontalLayout_13, 4, 1, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(635, 198, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_4, 7, 1, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(635, 198, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 0, 1, 1, 2)

        self.verticalSpacer_7 = QSpacerItem(635, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_7, 3, 1, 1, 2)

        self.add_location_successfully = QLabel(self.add_location)
        self.add_location_successfully.setObjectName(u"add_location_successfully")
        self.add_location_successfully.setStyleSheet(u"color: green;")
        self.add_location_successfully.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.add_location_successfully, 6, 1, 1, 2)

        self.verticalSpacer_9 = QSpacerItem(635, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_9, 5, 1, 1, 2)

        self.gridLayout_6.setRowStretch(0, 10)
        self.gridLayout_6.setRowStretch(1, 1)
        self.gridLayout_6.setRowStretch(2, 1)
        self.gridLayout_6.setRowStretch(3, 1)
        self.gridLayout_6.setRowStretch(4, 1)
        self.gridLayout_6.setRowStretch(5, 1)
        self.gridLayout_6.setRowStretch(6, 1)
        self.gridLayout_6.setRowStretch(7, 10)
        self.gridLayout_6.setColumnStretch(0, 10)
        self.gridLayout_6.setColumnStretch(1, 1)
        self.gridLayout_6.setColumnStretch(2, 1)
        self.gridLayout_6.setColumnStretch(3, 10)
        self.stackedWidget.addWidget(self.add_location)
        self.add = QWidget()
        self.add.setObjectName(u"add")
        self.verticalLayout_22 = QVBoxLayout(self.add)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(20, -1, 30, -1)
        self.label_38 = QLabel(self.add)
        self.label_38.setObjectName(u"label_38")
        sizePolicy2.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_38, 3, 0, 1, 1)

        self.label_39 = QLabel(self.add)
        self.label_39.setObjectName(u"label_39")
        sizePolicy6.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.label_39, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(50, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 4, 3, 1, 1)

        self.label_35 = QLabel(self.add)
        self.label_35.setObjectName(u"label_35")
        sizePolicy7.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy7)
        self.label_35.setFont(font1)
        self.label_35.setStyleSheet(u"margin-left: 20px;")
        self.label_35.setMargin(15)

        self.gridLayout_2.addWidget(self.label_35, 0, 0, 1, 1)

        self.add_female = QRadioButton(self.add)
        self.add_female.setObjectName(u"add_female")
        sizePolicy2.setHeightForWidth(self.add_female.sizePolicy().hasHeightForWidth())
        self.add_female.setSizePolicy(sizePolicy2)
        self.add_female.setMinimumSize(QSize(0, 40))
        self.add_female.setMaximumSize(QSize(16777215, 70))

        self.gridLayout_2.addWidget(self.add_female, 3, 2, 1, 1)

        self.add_male = QRadioButton(self.add)
        self.add_male.setObjectName(u"add_male")
        sizePolicy2.setHeightForWidth(self.add_male.sizePolicy().hasHeightForWidth())
        self.add_male.setSizePolicy(sizePolicy2)
        self.add_male.setMinimumSize(QSize(0, 40))
        self.add_male.setMaximumSize(QSize(16777215, 70))
        self.add_male.setChecked(True)

        self.gridLayout_2.addWidget(self.add_male, 3, 1, 1, 1)

        self.label_41 = QLabel(self.add)
        self.label_41.setObjectName(u"label_41")
        sizePolicy2.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_41, 2, 0, 1, 1)

        self.label_37 = QLabel(self.add)
        self.label_37.setObjectName(u"label_37")
        sizePolicy2.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_37, 4, 0, 1, 1)

        self.label_42 = QLabel(self.add)
        self.label_42.setObjectName(u"label_42")
        sizePolicy2.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_42, 5, 0, 1, 1)

        self.label_40 = QLabel(self.add)
        self.label_40.setObjectName(u"label_40")
        sizePolicy2.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_40, 6, 0, 1, 1)

        self.label_36 = QLabel(self.add)
        self.label_36.setObjectName(u"label_36")
        sizePolicy2.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_36, 9, 0, 1, 1)

        self.label_34 = QLabel(self.add)
        self.label_34.setObjectName(u"label_34")
        sizePolicy2.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_34, 7, 0, 1, 1)

        self.add_button_path = QPushButton(self.add)
        self.add_button_path.setObjectName(u"add_button_path")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.add_button_path.sizePolicy().hasHeightForWidth())
        self.add_button_path.setSizePolicy(sizePolicy9)
        self.add_button_path.setMinimumSize(QSize(100, 40))
        self.add_button_path.setMaximumSize(QSize(16777215, 70))
        self.add_button_path.setFont(font1)
        self.add_button_path.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_button_path.setStyleSheet(u"margin: 7px;\n"
"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_button_path.setIcon(icon5)

        self.gridLayout_2.addWidget(self.add_button_path, 10, 2, 1, 1)

        self.label_33 = QLabel(self.add)
        self.label_33.setObjectName(u"label_33")
        sizePolicy2.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_33, 8, 0, 1, 1)

        self.label_3 = QLabel(self.add)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_3, 10, 0, 1, 1)

        self.add_email = QLineEdit(self.add)
        self.add_email.setObjectName(u"add_email")
        sizePolicy6.setHeightForWidth(self.add_email.sizePolicy().hasHeightForWidth())
        self.add_email.setSizePolicy(sizePolicy6)
        self.add_email.setMinimumSize(QSize(0, 40))
        self.add_email.setMaximumSize(QSize(16777215, 70))
        self.add_email.setStyleSheet(u"margin: 7px;\n"
"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.add_email, 9, 1, 1, 2)

        self.add_last_name = QLineEdit(self.add)
        self.add_last_name.setObjectName(u"add_last_name")
        sizePolicy1.setHeightForWidth(self.add_last_name.sizePolicy().hasHeightForWidth())
        self.add_last_name.setSizePolicy(sizePolicy1)
        self.add_last_name.setMinimumSize(QSize(0, 40))
        self.add_last_name.setMaximumSize(QSize(16777215, 70))
        self.add_last_name.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"margin: 7px;")

        self.gridLayout_2.addWidget(self.add_last_name, 2, 1, 1, 2)

        self.add_text_path = QLineEdit(self.add)
        self.add_text_path.setObjectName(u"add_text_path")
        sizePolicy6.setHeightForWidth(self.add_text_path.sizePolicy().hasHeightForWidth())
        self.add_text_path.setSizePolicy(sizePolicy6)
        self.add_text_path.setMinimumSize(QSize(0, 40))
        self.add_text_path.setMaximumSize(QSize(16777215, 70))
        self.add_text_path.setStyleSheet(u"margin: 7px;\n"
"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.add_text_path, 10, 1, 1, 1)

        self.add_first_name = QLineEdit(self.add)
        self.add_first_name.setObjectName(u"add_first_name")
        sizePolicy6.setHeightForWidth(self.add_first_name.sizePolicy().hasHeightForWidth())
        self.add_first_name.setSizePolicy(sizePolicy6)
        self.add_first_name.setMinimumSize(QSize(0, 40))
        self.add_first_name.setMaximumSize(QSize(16777215, 70))
        self.add_first_name.setStyleSheet(u"margin: 7px;\n"
"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.add_first_name, 1, 1, 1, 2)

        self.add_department = QLineEdit(self.add)
        self.add_department.setObjectName(u"add_department")
        sizePolicy6.setHeightForWidth(self.add_department.sizePolicy().hasHeightForWidth())
        self.add_department.setSizePolicy(sizePolicy6)
        self.add_department.setMinimumSize(QSize(0, 40))
        self.add_department.setMaximumSize(QSize(16777215, 70))
        self.add_department.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"margin: 7px;")

        self.gridLayout_2.addWidget(self.add_department, 4, 1, 1, 2)

        self.add_passport_id = QLineEdit(self.add)
        self.add_passport_id.setObjectName(u"add_passport_id")
        sizePolicy6.setHeightForWidth(self.add_passport_id.sizePolicy().hasHeightForWidth())
        self.add_passport_id.setSizePolicy(sizePolicy6)
        self.add_passport_id.setMinimumSize(QSize(0, 40))
        self.add_passport_id.setMaximumSize(QSize(16777215, 70))
        self.add_passport_id.setStyleSheet(u"margin: 7px;\n"
"background-color: rgb(33, 37, 43);")
        self.add_passport_id.setInputMethodHints(Qt.ImhPreferNumbers)
        self.add_passport_id.setMaxLength(10)
        self.add_passport_id.setCursorPosition(0)

        self.gridLayout_2.addWidget(self.add_passport_id, 7, 1, 1, 2)

        self.add_phone_number = QLineEdit(self.add)
        self.add_phone_number.setObjectName(u"add_phone_number")
        sizePolicy6.setHeightForWidth(self.add_phone_number.sizePolicy().hasHeightForWidth())
        self.add_phone_number.setSizePolicy(sizePolicy6)
        self.add_phone_number.setMinimumSize(QSize(0, 40))
        self.add_phone_number.setMaximumSize(QSize(16777215, 70))
        self.add_phone_number.setStyleSheet(u"margin: 7px;\n"
"background-color: rgb(33, 37, 43);")
        self.add_phone_number.setMaxLength(16)

        self.gridLayout_2.addWidget(self.add_phone_number, 8, 1, 1, 2)

        self.add_photo_place = QLabel(self.add)
        self.add_photo_place.setObjectName(u"add_photo_place")
        sizePolicy4.setHeightForWidth(self.add_photo_place.sizePolicy().hasHeightForWidth())
        self.add_photo_place.setSizePolicy(sizePolicy4)
        self.add_photo_place.setMinimumSize(QSize(190, 0))
        self.add_photo_place.setMaximumSize(QSize(16000000, 16777215))
        self.add_photo_place.setSizeIncrement(QSize(0, 0))
        self.add_photo_place.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"image: url(:/images/images/images/real_man.png);\n"
"background-position: center center;\n"
"background-repeat: no-repeat;\n"
"border-radius: 10px;\n"
"margin: 7px;")
        self.add_photo_place.setScaledContents(False)
        self.add_photo_place.setAlignment(Qt.AlignCenter)
        self.add_photo_place.setWordWrap(False)
        self.add_photo_place.setMargin(10)

        self.gridLayout_2.addWidget(self.add_photo_place, 1, 4, 10, 1)

        self.add_birthday = QLineEdit(self.add)
        self.add_birthday.setObjectName(u"add_birthday")
        sizePolicy6.setHeightForWidth(self.add_birthday.sizePolicy().hasHeightForWidth())
        self.add_birthday.setSizePolicy(sizePolicy6)
        self.add_birthday.setMinimumSize(QSize(0, 40))
        self.add_birthday.setMaximumSize(QSize(16777215, 70))
        self.add_birthday.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"margin: 7px;")
        self.add_birthday.setMaxLength(10)

        self.gridLayout_2.addWidget(self.add_birthday, 6, 1, 1, 2)

        self.add_access_level = QComboBox(self.add)
        self.add_access_level.addItem("")
        self.add_access_level.addItem("")
        self.add_access_level.setObjectName(u"add_access_level")
        self.add_access_level.setMinimumSize(QSize(0, 40))
        self.add_access_level.setMaximumSize(QSize(16777215, 70))
        self.add_access_level.setFont(font1)
        self.add_access_level.setAutoFillBackground(False)
        self.add_access_level.setStyleSheet(u"\n"
"margin: 7px;\n"
"background-color: rgb(33, 37, 43);")
        self.add_access_level.setIconSize(QSize(16, 16))
        self.add_access_level.setFrame(True)

        self.gridLayout_2.addWidget(self.add_access_level, 5, 1, 1, 2)

        self.gridLayout_2.setColumnStretch(0, 4)
        self.gridLayout_2.setColumnStretch(1, 7)
        self.gridLayout_2.setColumnStretch(2, 3)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.gridLayout_2.setColumnStretch(4, 7)

        self.verticalLayout_22.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_22.addItem(self.verticalSpacer)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, 15, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.add_message = QLabel(self.add)
        self.add_message.setObjectName(u"add_message")
        self.add_message.setFont(font1)
        self.add_message.setStyleSheet(u"color: red;")

        self.horizontalLayout_10.addWidget(self.add_message)

        self.horizontalSpacer_5 = QSpacerItem(50, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.add_clear_person = QPushButton(self.add)
        self.add_clear_person.setObjectName(u"add_clear_person")
        sizePolicy8.setHeightForWidth(self.add_clear_person.sizePolicy().hasHeightForWidth())
        self.add_clear_person.setSizePolicy(sizePolicy8)
        self.add_clear_person.setMinimumSize(QSize(120, 35))
        self.add_clear_person.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(221, 221, 221);\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(57, 65, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(33, 37, 43);\n"
"}")

        self.horizontalLayout_10.addWidget(self.add_clear_person)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.add_add_person = QPushButton(self.add)
        self.add_add_person.setObjectName(u"add_add_person")
        self.add_add_person.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.add_add_person.sizePolicy().hasHeightForWidth())
        self.add_add_person.setSizePolicy(sizePolicy8)
        self.add_add_person.setMinimumSize(QSize(120, 35))
        self.add_add_person.setStyleSheet(u"/* \u041a\u043d\u043e\u043f\u043a\u0430 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f (OK) */\n"
"QPushButton {\n"
"background-color: rgb(128, 128, 128);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(164, 118, 233);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(139, 88, 217);\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.add_add_person)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_10.setStretch(0, 20)
        self.horizontalLayout_10.setStretch(1, 5)
        self.horizontalLayout_10.setStretch(2, 3)
        self.horizontalLayout_10.setStretch(3, 5)
        self.horizontalLayout_10.setStretch(4, 1)
        self.horizontalLayout_10.setStretch(5, 5)
        self.horizontalLayout_10.setStretch(6, 1)

        self.verticalLayout_22.addLayout(self.horizontalLayout_10)

        self.stackedWidget.addWidget(self.add)
        self.edit = QWidget()
        self.edit.setObjectName(u"edit")
        self.verticalLayout_19 = QVBoxLayout(self.edit)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(20, -1, 30, -1)
        self.label_52 = QLabel(self.edit)
        self.label_52.setObjectName(u"label_52")
        sizePolicy2.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.label_52, 7, 0, 1, 1)

        self.label_51 = QLabel(self.edit)
        self.label_51.setObjectName(u"label_51")
        sizePolicy2.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.label_51, 8, 0, 1, 1)

        self.lineEdit_30 = QLineEdit(self.edit)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        sizePolicy1.setHeightForWidth(self.lineEdit_30.sizePolicy().hasHeightForWidth())
        self.lineEdit_30.setSizePolicy(sizePolicy1)
        self.lineEdit_30.setMinimumSize(QSize(0, 40))
        self.lineEdit_30.setMaximumSize(QSize(16777215, 70))
        self.lineEdit_30.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"margin: 7px;")

        self.gridLayout_4.addWidget(self.lineEdit_30, 2, 1, 1, 2)

        self.lineEdit_29 = QLineEdit(self.edit)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        sizePolicy6.setHeightForWidth(self.lineEdit_29.sizePolicy().hasHeightForWidth())
        self.lineEdit_29.setSizePolicy(sizePolicy6)
        self.lineEdit_29.setMinimumSize(QSize(0, 40))
        self.lineEdit_29.setMaximumSize(QSize(16777215, 70))
        self.lineEdit_29.setStyleSheet(u"margin: 7px;\n"
"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.lineEdit_29, 9, 1, 1, 2)

        self.lineEdit_31 = QLineEdit(self.edit)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        sizePolicy6.setHeightForWidth(self.lineEdit_31.sizePolicy().hasHeightForWidth())
        self.lineEdit_31.setSizePolicy(sizePolicy6)
        self.lineEdit_31.setMinimumSize(QSize(0, 40))
        self.lineEdit_31.setMaximumSize(QSize(16777215, 70))
        self.lineEdit_31.setStyleSheet(u"margin: 7px;\n"
"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.lineEdit_31, 7, 1, 1, 2)

        self.lineEdit_10 = QLineEdit(self.edit)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy6.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy6)
        self.lineEdit_10.setMinimumSize(QSize(0, 40))
        self.lineEdit_10.setMaximumSize(QSize(16777215, 70))
        self.lineEdit_10.setStyleSheet(u"margin: 7px;\n"
"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.lineEdit_10, 1, 1, 1, 2)

        self.add_female_4 = QRadioButton(self.edit)
        self.add_female_4.setObjectName(u"add_female_4")
        sizePolicy2.setHeightForWidth(self.add_female_4.sizePolicy().hasHeightForWidth())
        self.add_female_4.setSizePolicy(sizePolicy2)
        self.add_female_4.setMinimumSize(QSize(0, 40))
        self.add_female_4.setMaximumSize(QSize(16777215, 70))

        self.gridLayout_4.addWidget(self.add_female_4, 3, 2, 1, 1)

        self.label_48 = QLabel(self.edit)
        self.label_48.setObjectName(u"label_48")
        sizePolicy2.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.label_48, 9, 0, 1, 1)

        self.add_male_4 = QRadioButton(self.edit)
        self.add_male_4.setObjectName(u"add_male_4")
        sizePolicy2.setHeightForWidth(self.add_male_4.sizePolicy().hasHeightForWidth())
        self.add_male_4.setSizePolicy(sizePolicy2)
        self.add_male_4.setMinimumSize(QSize(0, 40))
        self.add_male_4.setMaximumSize(QSize(16777215, 70))
        self.add_male_4.setChecked(True)

        self.gridLayout_4.addWidget(self.add_male_4, 3, 1, 1, 1)

        self.label_4 = QLabel(self.edit)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.label_4, 10, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.edit)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy6.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy6)
        self.lineEdit_7.setMinimumSize(QSize(0, 40))
        self.lineEdit_7.setMaximumSize(QSize(16777215, 70))
        self.lineEdit_7.setStyleSheet(u"margin: 7px;\n"
"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.lineEdit_7, 10, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.edit)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy9.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy9)
        self.pushButton_13.setMinimumSize(QSize(100, 40))
        self.pushButton_13.setMaximumSize(QSize(16777215, 70))
        self.pushButton_13.setFont(font1)
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u"margin: 7px;\n"
"background-color: rgb(52, 59, 72);")
        self.pushButton_13.setIcon(icon5)

        self.gridLayout_4.addWidget(self.pushButton_13, 10, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(50, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 4, 3, 1, 1)

        self.label_44 = QLabel(self.edit)
        self.label_44.setObjectName(u"label_44")
        sizePolicy2.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.label_44, 3, 0, 1, 1)

        self.label_47 = QLabel(self.edit)
        self.label_47.setObjectName(u"label_47")
        sizePolicy2.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.label_47, 4, 0, 1, 1)

        self.label_46 = QLabel(self.edit)
        self.label_46.setObjectName(u"label_46")
        sizePolicy2.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.label_46, 2, 0, 1, 1)

        self.label_45 = QLabel(self.edit)
        self.label_45.setObjectName(u"label_45")
        sizePolicy6.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.label_45, 1, 0, 1, 1)

        self.lineEdit_32 = QLineEdit(self.edit)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        sizePolicy6.setHeightForWidth(self.lineEdit_32.sizePolicy().hasHeightForWidth())
        self.lineEdit_32.setSizePolicy(sizePolicy6)
        self.lineEdit_32.setMinimumSize(QSize(0, 40))
        self.lineEdit_32.setMaximumSize(QSize(16777215, 70))
        self.lineEdit_32.setStyleSheet(u"margin: 7px;\n"
"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.lineEdit_32, 8, 1, 1, 2)

        self.lineEdit_33 = QLineEdit(self.edit)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        sizePolicy6.setHeightForWidth(self.lineEdit_33.sizePolicy().hasHeightForWidth())
        self.lineEdit_33.setSizePolicy(sizePolicy6)
        self.lineEdit_33.setMinimumSize(QSize(0, 40))
        self.lineEdit_33.setMaximumSize(QSize(16777215, 70))
        self.lineEdit_33.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"margin: 7px;")

        self.gridLayout_4.addWidget(self.lineEdit_33, 4, 1, 1, 2)

        self.lineEdit_34 = QLineEdit(self.edit)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        sizePolicy6.setHeightForWidth(self.lineEdit_34.sizePolicy().hasHeightForWidth())
        self.lineEdit_34.setSizePolicy(sizePolicy6)
        self.lineEdit_34.setMinimumSize(QSize(0, 40))
        self.lineEdit_34.setMaximumSize(QSize(16777215, 70))
        self.lineEdit_34.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"margin: 7px;")

        self.gridLayout_4.addWidget(self.lineEdit_34, 6, 1, 1, 2)

        self.lineEdit_35 = QLineEdit(self.edit)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        sizePolicy6.setHeightForWidth(self.lineEdit_35.sizePolicy().hasHeightForWidth())
        self.lineEdit_35.setSizePolicy(sizePolicy6)
        self.lineEdit_35.setMinimumSize(QSize(0, 40))
        self.lineEdit_35.setMaximumSize(QSize(16777215, 70))
        self.lineEdit_35.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"margin: 7;\n"
"")

        self.gridLayout_4.addWidget(self.lineEdit_35, 5, 1, 1, 2)

        self.label_53 = QLabel(self.edit)
        self.label_53.setObjectName(u"label_53")
        sizePolicy4.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy4)
        self.label_53.setMinimumSize(QSize(190, 0))
        self.label_53.setMaximumSize(QSize(16000000, 16777215))
        self.label_53.setSizeIncrement(QSize(0, 0))
        self.label_53.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"image: url(:/images/images/images/real_man.png);\n"
"background-position: center center;\n"
"background-repeat: no-repeat;\n"
"border-radius: 10px;\n"
"margin: 7px;")
        self.label_53.setScaledContents(False)
        self.label_53.setAlignment(Qt.AlignCenter)
        self.label_53.setWordWrap(False)
        self.label_53.setMargin(10)

        self.gridLayout_4.addWidget(self.label_53, 1, 4, 10, 1)

        self.label_50 = QLabel(self.edit)
        self.label_50.setObjectName(u"label_50")
        sizePolicy2.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.label_50, 5, 0, 1, 1)

        self.label_49 = QLabel(self.edit)
        self.label_49.setObjectName(u"label_49")
        sizePolicy2.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.label_49, 6, 0, 1, 1)

        self.label_43 = QLabel(self.edit)
        self.label_43.setObjectName(u"label_43")
        sizePolicy7.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy7)
        self.label_43.setFont(font1)
        self.label_43.setStyleSheet(u"margin-left: 20px;")
        self.label_43.setMargin(15)

        self.gridLayout_4.addWidget(self.label_43, 0, 0, 1, 3)

        self.gridLayout_4.setColumnStretch(0, 4)
        self.gridLayout_4.setColumnStretch(1, 7)
        self.gridLayout_4.setColumnStretch(2, 3)
        self.gridLayout_4.setColumnStretch(3, 1)
        self.gridLayout_4.setColumnStretch(4, 7)

        self.verticalLayout_19.addLayout(self.gridLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, 15, -1)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.pushButton_11 = QPushButton(self.edit)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy8.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy8)
        self.pushButton_11.setMinimumSize(QSize(120, 35))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(221, 221, 221);\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(57, 65, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(33, 37, 43);\n"
"}")

        self.horizontalLayout_11.addWidget(self.pushButton_11)

        self.horizontalSpacer_10 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.pushButton_12 = QPushButton(self.edit)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy8)
        self.pushButton_12.setMinimumSize(QSize(120, 35))
        self.pushButton_12.setStyleSheet(u"/* \u041a\u043d\u043e\u043f\u043a\u0430 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f (OK) */\n"
"QPushButton {\n"
"    background-color: rgb(189, 147, 249);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(164, 118, 233);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(139, 88, 217);\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: rgb(128, 128, 128); /* \u0426\u0432\u0435\u0442 \u0434\u043b\u044f \u0432\u044b\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}")

        self.horizontalLayout_11.addWidget(self.pushButton_12)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.horizontalLayout_11.setStretch(0, 36)
        self.horizontalLayout_11.setStretch(1, 6)
        self.horizontalLayout_11.setStretch(2, 1)
        self.horizontalLayout_11.setStretch(3, 6)
        self.horizontalLayout_11.setStretch(4, 2)

        self.verticalLayout_19.addLayout(self.horizontalLayout_11)

        self.stackedWidget.addWidget(self.edit)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setMinimumSize(QSize(0, 0))
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_adb = QStackedWidget(self.contentSettings)
        self.stackedWidget_adb.setObjectName(u"stackedWidget_adb")
        self.stackedWidget_adb.setStyleSheet(u"background-color: transparent;")
        self.frame_settings_db = QWidget()
        self.frame_settings_db.setObjectName(u"frame_settings_db")
        self.label_11 = QLabel(self.frame_settings_db)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 10, 241, 91))
        self.label_11.setStyleSheet(u"font-size: 20px;\n"
"")
        self.label_11.setScaledContents(False)
        self.label_11.setWordWrap(True)
        self.label_11.setMargin(14)
        self.label_11.setOpenExternalLinks(False)
        self.themeSettingsTopDetail_2 = QFrame(self.frame_settings_db)
        self.themeSettingsTopDetail_2.setObjectName(u"themeSettingsTopDetail_2")
        self.themeSettingsTopDetail_2.setGeometry(QRect(0, 0, 240, 3))
        self.themeSettingsTopDetail_2.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail_2.setStyleSheet(u"background-color: rgb(189, 147, 249);")
        self.themeSettingsTopDetail_2.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_settings_db)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 100, 241, 351))
        self.layoutWidget.setStyleSheet(u"")
        self.verticalLayout_24 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(20, 0, 20, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(113, 126, 149);\n"
"padding-top: 10px;\n"
"padding-left: 10px;")

        self.verticalLayout_24.addWidget(self.label)

        self.adb_name = QLineEdit(self.layoutWidget)
        self.adb_name.setObjectName(u"adb_name")
        self.adb_name.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"font: 75 12pt \"Open Sans\";")

        self.verticalLayout_24.addWidget(self.adb_name)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(113, 126, 149);\n"
"padding-top: 10px;\n"
"padding-left: 10px;")

        self.verticalLayout_24.addWidget(self.label_2)

        self.adb_user = QLineEdit(self.layoutWidget)
        self.adb_user.setObjectName(u"adb_user")
        self.adb_user.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"font: 75 12pt \"Open Sans\";")

        self.verticalLayout_24.addWidget(self.adb_user)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(113, 126, 149);\n"
"padding-top: 10px;\n"
"padding-left: 10px;")

        self.verticalLayout_24.addWidget(self.label_5)

        self.adb_password = QLineEdit(self.layoutWidget)
        self.adb_password.setObjectName(u"adb_password")
        self.adb_password.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"font: 75 12pt \"Open Sans\";")
        self.adb_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_24.addWidget(self.adb_password)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(113, 126, 149);\n"
"padding-top: 10px;\n"
"padding-left: 10px;")

        self.verticalLayout_24.addWidget(self.label_8)

        self.adb_host = QLineEdit(self.layoutWidget)
        self.adb_host.setObjectName(u"adb_host")
        self.adb_host.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"font: 75 12pt \"Open Sans\";")

        self.verticalLayout_24.addWidget(self.adb_host)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: rgb(113, 126, 149);\n"
"padding-top: 10px;\n"
"padding-left: 10px;")

        self.verticalLayout_24.addWidget(self.label_10)

        self.adb_port = QLineEdit(self.layoutWidget)
        self.adb_port.setObjectName(u"adb_port")
        self.adb_port.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"font: 75 12pt \"Open Sans\";")

        self.verticalLayout_24.addWidget(self.adb_port)

        self.layoutWidget1 = QWidget(self.frame_settings_db)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 470, 241, 61))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setSpacing(14)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(14, 10, 14, 0)
        self.adb_cancel = QPushButton(self.layoutWidget1)
        self.adb_cancel.setObjectName(u"adb_cancel")
        sizePolicy8.setHeightForWidth(self.adb_cancel.sizePolicy().hasHeightForWidth())
        self.adb_cancel.setSizePolicy(sizePolicy8)
        self.adb_cancel.setMinimumSize(QSize(80, 30))
        self.adb_cancel.setLayoutDirection(Qt.LeftToRight)
        self.adb_cancel.setAutoFillBackground(False)
        self.adb_cancel.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(221, 221, 221);\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"border: none;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(57, 65, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(33, 37, 43);\n"
"}")

        self.horizontalLayout_7.addWidget(self.adb_cancel)

        self.adb_connect = QPushButton(self.layoutWidget1)
        self.adb_connect.setObjectName(u"adb_connect")
        sizePolicy8.setHeightForWidth(self.adb_connect.sizePolicy().hasHeightForWidth())
        self.adb_connect.setSizePolicy(sizePolicy8)
        self.adb_connect.setMinimumSize(QSize(80, 30))
        self.adb_connect.setStyleSheet(u"/* \u041a\u043d\u043e\u043f\u043a\u0430 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f (OK) */\n"
"QPushButton {\n"
"background-color: rgb(189, 147, 249);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"border: none;\n"
"text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(164, 118, 233);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(139, 88, 217);\n"
"}")

        self.horizontalLayout_7.addWidget(self.adb_connect)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)
        self.db_incorrect_data = QLabel(self.frame_settings_db)
        self.db_incorrect_data.setObjectName(u"db_incorrect_data")
        self.db_incorrect_data.setGeometry(QRect(0, 550, 241, 20))
        self.db_incorrect_data.setStyleSheet(u"color: rgb(255, 30, 30);")
        self.db_incorrect_data.setAlignment(Qt.AlignCenter)
        self.stackedWidget_adb.addWidget(self.frame_settings_db)
        self.frame_settings = QWidget()
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setStyleSheet(u"QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.themeSettingsTopDetail_4 = QFrame(self.frame_settings)
        self.themeSettingsTopDetail_4.setObjectName(u"themeSettingsTopDetail_4")
        self.themeSettingsTopDetail_4.setGeometry(QRect(0, 0, 240, 3))
        self.themeSettingsTopDetail_4.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail_4.setStyleSheet(u"background-color: rgb(189, 147, 249);")
        self.themeSettingsTopDetail_4.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail_4.setFrameShadow(QFrame.Raised)
        self.settings_database = QPushButton(self.frame_settings)
        self.settings_database.setObjectName(u"settings_database")
        self.settings_database.setGeometry(QRect(0, 3, 241, 45))
        sizePolicy6.setHeightForWidth(self.settings_database.sizePolicy().hasHeightForWidth())
        self.settings_database.setSizePolicy(sizePolicy6)
        self.settings_database.setMinimumSize(QSize(0, 45))
        self.settings_database.setFont(font1)
        self.settings_database.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_database.setLayoutDirection(Qt.LeftToRight)
        self.settings_database.setStyleSheet(u"background-image: url(:/icons/images/icons/database20.png);")
        self.setting_face_detection = QPushButton(self.frame_settings)
        self.setting_face_detection.setObjectName(u"setting_face_detection")
        self.setting_face_detection.setGeometry(QRect(0, 48, 241, 45))
        sizePolicy6.setHeightForWidth(self.setting_face_detection.sizePolicy().hasHeightForWidth())
        self.setting_face_detection.setSizePolicy(sizePolicy6)
        self.setting_face_detection.setMinimumSize(QSize(0, 45))
        self.setting_face_detection.setFont(font1)
        self.setting_face_detection.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_face_detection.setLayoutDirection(Qt.LeftToRight)
        self.setting_face_detection.setStyleSheet(u"background-image: url(:/icons/images/icons/facebox20.png);")
        self.settings_bbox_style = QPushButton(self.frame_settings)
        self.settings_bbox_style.setObjectName(u"settings_bbox_style")
        self.settings_bbox_style.setGeometry(QRect(0, 93, 241, 45))
        sizePolicy6.setHeightForWidth(self.settings_bbox_style.sizePolicy().hasHeightForWidth())
        self.settings_bbox_style.setSizePolicy(sizePolicy6)
        self.settings_bbox_style.setMinimumSize(QSize(0, 45))
        self.settings_bbox_style.setFont(font1)
        self.settings_bbox_style.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_bbox_style.setLayoutDirection(Qt.LeftToRight)
        self.settings_bbox_style.setStyleSheet(u"background-image: url(:/icons/images/icons/lipstick20.png);")
        self.settings_for_developers = QPushButton(self.frame_settings)
        self.settings_for_developers.setObjectName(u"settings_for_developers")
        self.settings_for_developers.setGeometry(QRect(0, 138, 241, 45))
        sizePolicy6.setHeightForWidth(self.settings_for_developers.sizePolicy().hasHeightForWidth())
        self.settings_for_developers.setSizePolicy(sizePolicy6)
        self.settings_for_developers.setMinimumSize(QSize(0, 45))
        self.settings_for_developers.setFont(font1)
        self.settings_for_developers.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_for_developers.setLayoutDirection(Qt.LeftToRight)
        self.settings_for_developers.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-code.png);")
        self.stackedWidget_adb.addWidget(self.frame_settings)
        self.frame_db_connect_successful = QWidget()
        self.frame_db_connect_successful.setObjectName(u"frame_db_connect_successful")
        self.verticalLayout_33 = QVBoxLayout(self.frame_db_connect_successful)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail_5 = QFrame(self.frame_db_connect_successful)
        self.themeSettingsTopDetail_5.setObjectName(u"themeSettingsTopDetail_5")
        self.themeSettingsTopDetail_5.setMinimumSize(QSize(0, 3))
        self.themeSettingsTopDetail_5.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail_5.setStyleSheet(u"background-color: rgb(189, 147, 249);")
        self.themeSettingsTopDetail_5.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_33.addWidget(self.themeSettingsTopDetail_5)

        self.verticalSpacer_5 = QSpacerItem(5, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_33.addItem(self.verticalSpacer_5)

        self.label_12 = QLabel(self.frame_db_connect_successful)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font-size: 20px;\n"
"")
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setMargin(15)
        self.label_12.setOpenExternalLinks(False)

        self.verticalLayout_33.addWidget(self.label_12)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(30, -1, 30, -1)
        self.db_successful_back = QPushButton(self.frame_db_connect_successful)
        self.db_successful_back.setObjectName(u"db_successful_back")
        sizePolicy8.setHeightForWidth(self.db_successful_back.sizePolicy().hasHeightForWidth())
        self.db_successful_back.setSizePolicy(sizePolicy8)
        self.db_successful_back.setMinimumSize(QSize(120, 35))
        self.db_successful_back.setStyleSheet(u"/* \u041a\u043d\u043e\u043f\u043a\u0430 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f (OK) */\n"
"QPushButton {\n"
"background-color: rgb(189, 147, 249);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"border: none;\n"
"text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(164, 118, 233);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(139, 88, 217);\n"
"}")

        self.horizontalLayout_19.addWidget(self.db_successful_back)


        self.verticalLayout_33.addLayout(self.horizontalLayout_19)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_6)

        self.verticalLayout_33.setStretch(4, 50)
        self.stackedWidget_adb.addWidget(self.frame_db_connect_successful)
        self.for_developers = QWidget()
        self.for_developers.setObjectName(u"for_developers")
        self.label_19 = QLabel(self.for_developers)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 0, 240, 61))
        self.label_19.setStyleSheet(u"font: 14pt \"Open Sans\";\n"
"")
        self.label_19.setScaledContents(False)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setWordWrap(True)
        self.label_19.setMargin(15)
        self.label_19.setOpenExternalLinks(False)
        self.layoutWidget_2 = QWidget(self.for_developers)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 440, 241, 61))
        self.horizontalLayout_15 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_15.setSpacing(14)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(20, 10, 20, 0)
        self.dev_setting_cancel = QPushButton(self.layoutWidget_2)
        self.dev_setting_cancel.setObjectName(u"dev_setting_cancel")
        sizePolicy8.setHeightForWidth(self.dev_setting_cancel.sizePolicy().hasHeightForWidth())
        self.dev_setting_cancel.setSizePolicy(sizePolicy8)
        self.dev_setting_cancel.setMinimumSize(QSize(80, 30))
        self.dev_setting_cancel.setLayoutDirection(Qt.LeftToRight)
        self.dev_setting_cancel.setAutoFillBackground(False)
        self.dev_setting_cancel.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(221, 221, 221);\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"border: none;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(57, 65, 80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(33, 37, 43);\n"
"}")

        self.horizontalLayout_15.addWidget(self.dev_setting_cancel)

        self.dev_setting_apply = QPushButton(self.layoutWidget_2)
        self.dev_setting_apply.setObjectName(u"dev_setting_apply")
        sizePolicy8.setHeightForWidth(self.dev_setting_apply.sizePolicy().hasHeightForWidth())
        self.dev_setting_apply.setSizePolicy(sizePolicy8)
        self.dev_setting_apply.setMinimumSize(QSize(80, 30))
        self.dev_setting_apply.setStyleSheet(u"/* \u041a\u043d\u043e\u043f\u043a\u0430 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f (OK) */\n"
"QPushButton {\n"
"background-color: rgb(189, 147, 249);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"padding: 5px 10px;\n"
"border: none;\n"
"text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(164, 118, 233);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(139, 88, 217);\n"
"}")

        self.horizontalLayout_15.addWidget(self.dev_setting_apply)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 1)
        self.widget = QWidget(self.for_developers)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 60, 221, 121))
        self.widget.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(40, 44, 52);")
        self.layoutWidget2 = QWidget(self.widget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 201, 110))
        self.gridLayout_8 = QGridLayout(self.layoutWidget2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.dev_setting_number_lbl = QLabel(self.layoutWidget2)
        self.dev_setting_number_lbl.setObjectName(u"dev_setting_number_lbl")
        self.dev_setting_number_lbl.setStyleSheet(u"font: 12pt \"Open Sans\";")
        self.dev_setting_number_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.dev_setting_number_lbl, 4, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_8, 2, 0, 1, 2)

        self.dev_setting_distance_lbl = QLabel(self.layoutWidget2)
        self.dev_setting_distance_lbl.setObjectName(u"dev_setting_distance_lbl")
        self.dev_setting_distance_lbl.setFont(font)
        self.dev_setting_distance_lbl.setStyleSheet(u"font: 12pt \"Open Sans\";")
        self.dev_setting_distance_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.dev_setting_distance_lbl, 1, 1, 1, 1)

        self.label_16 = QLabel(self.layoutWidget2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_8.addWidget(self.label_16, 3, 0, 1, 2)

        self.dev_setting_number_slider = QSlider(self.layoutWidget2)
        self.dev_setting_number_slider.setObjectName(u"dev_setting_number_slider")
        self.dev_setting_number_slider.setMaximumSize(QSize(170, 16777215))
        self.dev_setting_number_slider.setMinimum(1)
        self.dev_setting_number_slider.setMaximum(10)
        self.dev_setting_number_slider.setValue(3)
        self.dev_setting_number_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.dev_setting_number_slider, 4, 0, 1, 1)

        self.dev_setting_distance_slider = QSlider(self.layoutWidget2)
        self.dev_setting_distance_slider.setObjectName(u"dev_setting_distance_slider")
        self.dev_setting_distance_slider.setMaximumSize(QSize(170, 16777215))
        self.dev_setting_distance_slider.setMaximum(1000)
        self.dev_setting_distance_slider.setValue(800)
        self.dev_setting_distance_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_8.addWidget(self.dev_setting_distance_slider, 1, 0, 1, 1)

        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_8.addWidget(self.label_9, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.for_developers)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 190, 221, 51))
        self.widget_3.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(40, 44, 52);")
        self.dev_setting_backbone = QComboBox(self.widget_3)
        self.dev_setting_backbone.addItem("")
        self.dev_setting_backbone.addItem("")
        self.dev_setting_backbone.addItem("")
        self.dev_setting_backbone.addItem("")
        self.dev_setting_backbone.setObjectName(u"dev_setting_backbone")
        self.dev_setting_backbone.setGeometry(QRect(90, 10, 121, 31))
        self.dev_setting_backbone.setFont(font1)
        self.dev_setting_backbone.setAutoFillBackground(False)
        self.dev_setting_backbone.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.dev_setting_backbone.setIconSize(QSize(16, 16))
        self.dev_setting_backbone.setFrame(True)
        self.label_17 = QLabel(self.widget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 10, 71, 31))
        self.label_17.setStyleSheet(u"font: 11pt \"Open Sans\";")
        self.widget_4 = QWidget(self.for_developers)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 250, 221, 51))
        self.widget_4.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(40, 44, 52);")
        self.dev_setting_device = QComboBox(self.widget_4)
        self.dev_setting_device.addItem("")
        self.dev_setting_device.addItem("")
        self.dev_setting_device.setObjectName(u"dev_setting_device")
        self.dev_setting_device.setGeometry(QRect(90, 10, 121, 31))
        self.dev_setting_device.setFont(font1)
        self.dev_setting_device.setAutoFillBackground(False)
        self.dev_setting_device.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.dev_setting_device.setIconSize(QSize(16, 16))
        self.dev_setting_device.setFrame(True)
        self.label_20 = QLabel(self.widget_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(15, 10, 71, 31))
        self.label_20.setStyleSheet(u"font: 11pt \"Open Sans\";")
        self.widget_5 = QWidget(self.for_developers)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(10, 310, 221, 61))
        self.widget_5.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(40, 44, 52);")
        self.layoutWidget_3 = QWidget(self.widget_5)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 10, 201, 50))
        self.gridLayout_9 = QGridLayout(self.layoutWidget_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.dev_setting_gpu_memory_lbl = QLabel(self.layoutWidget_3)
        self.dev_setting_gpu_memory_lbl.setObjectName(u"dev_setting_gpu_memory_lbl")
        self.dev_setting_gpu_memory_lbl.setFont(font)
        self.dev_setting_gpu_memory_lbl.setStyleSheet(u"font: 12pt \"Open Sans\";")
        self.dev_setting_gpu_memory_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.dev_setting_gpu_memory_lbl, 1, 1, 1, 1)

        self.dev_setting_gpu_memory_slider = QSlider(self.layoutWidget_3)
        self.dev_setting_gpu_memory_slider.setObjectName(u"dev_setting_gpu_memory_slider")
        self.dev_setting_gpu_memory_slider.setEnabled(True)
        self.dev_setting_gpu_memory_slider.setMaximumSize(QSize(170, 16777215))
        self.dev_setting_gpu_memory_slider.setStyleSheet(u"")
        self.dev_setting_gpu_memory_slider.setMaximum(1000)
        self.dev_setting_gpu_memory_slider.setValue(400)
        self.dev_setting_gpu_memory_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.dev_setting_gpu_memory_slider, 1, 0, 1, 1)

        self.label_21 = QLabel(self.layoutWidget_3)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_9.addWidget(self.label_21, 0, 0, 1, 2)

        self.widget_6 = QWidget(self.for_developers)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(10, 380, 221, 61))
        self.widget_6.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(40, 44, 52);")
        self.label_22 = QLabel(self.widget_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 10, 71, 41))
        self.label_22.setStyleSheet(u"font: 11pt \"Open Sans\";\n"
"background-color: rgb(85, 170, 0, 0);")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(10, 10, 201, 41))
        self.widget_7.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(33, 37, 43);")
        self.dev_setting_show_fps = QCheckBox(self.widget_7)
        self.dev_setting_show_fps.setObjectName(u"dev_setting_show_fps")
        self.dev_setting_show_fps.setGeometry(QRect(160, 0, 131, 41))
        self.dev_setting_show_fps.setStyleSheet(u"background-color: rgb(255, 170, ,0,0);")
        self.widget_7.raise_()
        self.label_22.raise_()
        self.stackedWidget_adb.addWidget(self.for_developers)
        self.widget_3.raise_()
        self.label_19.raise_()
        self.layoutWidget_2.raise_()
        self.widget.raise_()
        self.widget_4.raise_()
        self.widget_5.raise_()
        self.widget_6.raise_()

        self.verticalLayout_13.addWidget(self.stackedWidget_adb)

        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setFont(font1)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)

        self.extraLeftBox.raise_()
        self.leftMenuBg.raise_()
        self.contentBox.raise_()

        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_adb.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"CourseWork", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Face recognition", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Add a person", None))
        self.btn_base.setText(QCoreApplication.translate("MainWindow", u"Personality database", None))
        self.btn_locations.setText(QCoreApplication.translate("MainWindow", u"Analytics", None))
        self.btn_history.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Open Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-ri"
                        "ght:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>ExSec</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.stackedWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.home_video_place.setText(QCoreApplication.translate("MainWindow", u"Place for video stream", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.home_name.setText("")
        self.home_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.home_age.setText("")
        self.home_age.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.home_photo_place.setText(QCoreApplication.translate("MainWindow", u"Place for photo", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Level of access", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.home_department.setText("")
        self.home_department.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.home_level_access.setText("")
        self.home_level_access.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Access level", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.home_gender.setText("")
        self.home_gender.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Gender", None))
#if QT_CONFIG(tooltip)
        self.home_start_system.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.home_start_system.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"Find a person", None))
        self.view_linestring.setText("")
        self.view_linestring.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.view_search_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Start entering the person's data", None))
        self.view_search_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Name", None))
        self.view_search_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Passport ID", None))
        self.view_search_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Subdivision", None))

        ___qtablewidgetitem = self.view_tabble.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.view_tabble.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.view_tabble.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.view_tabble.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.view_tabble.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem5 = self.view_tabble.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem6 = self.view_tabble.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.view_tabble.isSortingEnabled()
        self.view_tabble.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.view_tabble.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem8 = self.view_tabble.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem9 = self.view_tabble.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem10 = self.view_tabble.item(0, 3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Passport ID", None));
        ___qtablewidgetitem11 = self.view_tabble.item(0, 4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Phone number", None));
        ___qtablewidgetitem12 = self.view_tabble.item(0, 5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.view_tabble.setSortingEnabled(__sortingEnabled)

        self.view_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.view_dellete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"Find in history", None))
        self.history_linestring.setText("")
        self.history_linestring.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.history_search_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_4.setText(QCoreApplication.translate("MainWindow", u"Start entering...", None))
        self.history_search_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Name", None))
        self.history_search_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Passport ID", None))
        self.history_search_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Department", None))

        ___qtablewidgetitem13 = self.histiry_table.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem14 = self.histiry_table.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem15 = self.histiry_table.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem16 = self.histiry_table.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem17 = self.histiry_table.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem18 = self.histiry_table.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem19 = self.histiry_table.verticalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.histiry_table.isSortingEnabled()
        self.histiry_table.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.histiry_table.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem21 = self.histiry_table.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem22 = self.histiry_table.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem23 = self.histiry_table.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Passport ID", None));
        ___qtablewidgetitem24 = self.histiry_table.item(0, 4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Department", None));
        ___qtablewidgetitem25 = self.histiry_table.item(0, 5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.histiry_table.setSortingEnabled(__sortingEnabled1)

        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Choose current location</span></p></body></html>", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Level of access", None))
        self.choose_location_access_level.setText("")
        self.choose_location_access_level.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Here will access level", None))
        self.choose_location_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.choose_location_addnew.setText(QCoreApplication.translate("MainWindow", u"Add new", None))
        self.choose_location_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.add_location_titles.setText("")
        self.add_location_titles.setPlaceholderText(QCoreApplication.translate("MainWindow", u"KIchen", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Level of access", None))
        self.add_location_access.setItemText(0, QCoreApplication.translate("MainWindow", u"Public", None))
        self.add_location_access.setItemText(1, QCoreApplication.translate("MainWindow", u"All employes", None))
        self.add_location_access.setItemText(2, QCoreApplication.translate("MainWindow", u"Enhanced", None))

        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Add a location</span></p></body></html>", None))
        self.add_location_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.add_location_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.add_location_successfully.setText(QCoreApplication.translate("MainWindow", u"Location added successfully", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"First name", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Add person</span></p></body></html>", None))
        self.add_female.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.add_male.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Last name", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Level of access", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Birthdate", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Passport ID", None))
        self.add_button_path.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Phone number", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Photo", None))
        self.add_email.setText("")
        self.add_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example@mospolygon.ru", None))
        self.add_last_name.setText("")
        self.add_last_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kolmogorov", None))
        self.add_text_path.setText("")
        self.add_text_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\image\\photo.jpeg", None))
        self.add_first_name.setText("")
        self.add_first_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Andrey", None))
        self.add_department.setText("")
        self.add_department.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nature guardian", None))
        self.add_passport_id.setText("")
        self.add_passport_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"6149250984", None))
        self.add_phone_number.setText("")
        self.add_phone_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"+7 908 432 53 12", None))
        self.add_photo_place.setText("")
        self.add_birthday.setInputMask("")
        self.add_birthday.setText("")
        self.add_birthday.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mm/dd/yyyy", None))
        self.add_access_level.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.add_access_level.setItemText(1, QCoreApplication.translate("MainWindow", u"Enhanced", None))

        self.add_message.setText(QCoreApplication.translate("MainWindow", u"This user already exist", None))
        self.add_clear_person.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.add_add_person.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Passport ID", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Phone number", None))
        self.lineEdit_30.setText("")
        self.lineEdit_30.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kolmogorov", None))
        self.lineEdit_29.setText("")
        self.lineEdit_29.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example@mospolygon.ru", None))
        self.lineEdit_31.setText("")
        self.lineEdit_31.setPlaceholderText(QCoreApplication.translate("MainWindow", u"6149250984", None))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Andrey", None))
        self.add_female_4.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.add_male_4.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Photo", None))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\image\\photo.jpeg", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Last name", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"First name", None))
        self.lineEdit_32.setText("")
        self.lineEdit_32.setPlaceholderText(QCoreApplication.translate("MainWindow", u"+7 908 432 53 12", None))
        self.lineEdit_33.setText("")
        self.lineEdit_33.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nature guardian", None))
        self.lineEdit_34.setText("")
        self.lineEdit_34.setPlaceholderText(QCoreApplication.translate("MainWindow", u"25.04.2004", None))
        self.lineEdit_35.setText("")
        self.lineEdit_35.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wooden squad", None))
        self.label_53.setText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Subdivision", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Birthdate", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Edit the person</span></p></body></html>", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Database connection options", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"database name", None))
        self.adb_name.setText(QCoreApplication.translate("MainWindow", u"PersonBase", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"user", None))
        self.adb_user.setText(QCoreApplication.translate("MainWindow", u"postgres", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"host", None))
        self.adb_host.setText(QCoreApplication.translate("MainWindow", u"localhost", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"port", None))
        self.adb_port.setText(QCoreApplication.translate("MainWindow", u"10007", None))
        self.adb_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.adb_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.db_incorrect_data.setText(QCoreApplication.translate("MainWindow", u"The entered data are incorrect", None))
        self.settings_database.setText(QCoreApplication.translate("MainWindow", u"DataBase options", None))
        self.setting_face_detection.setText(QCoreApplication.translate("MainWindow", u"Face detection method", None))
        self.settings_bbox_style.setText(QCoreApplication.translate("MainWindow", u"Bounding box style", None))
        self.settings_for_developers.setText(QCoreApplication.translate("MainWindow", u"For developers", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Connection successful</p></body></html>", None))
        self.db_successful_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Developer settings</span></p></body></html>", None))
        self.dev_setting_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.dev_setting_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.dev_setting_number_lbl.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.dev_setting_distance_lbl.setText(QCoreApplication.translate("MainWindow", u"0.80", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Number of positive recognitions", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Distance threshold", None))
        self.dev_setting_backbone.setItemText(0, QCoreApplication.translate("MainWindow", u"ResNet18", None))
        self.dev_setting_backbone.setItemText(1, QCoreApplication.translate("MainWindow", u"ResNet34", None))
        self.dev_setting_backbone.setItemText(2, QCoreApplication.translate("MainWindow", u"ResNet50", None))
        self.dev_setting_backbone.setItemText(3, QCoreApplication.translate("MainWindow", u"ResNet100", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Backbone", None))
        self.dev_setting_device.setItemText(0, QCoreApplication.translate("MainWindow", u"CPU", None))
        self.dev_setting_device.setItemText(1, QCoreApplication.translate("MainWindow", u"GPU (CUDA)", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Device", None))
        self.dev_setting_gpu_memory_lbl.setText(QCoreApplication.translate("MainWindow", u"40%", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Allocated device memory ", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Show FPS", None))
        self.dev_setting_show_fps.setText("")
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"i m tirred", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.1.1", None))
    # retranslateUi

