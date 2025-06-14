# Form implementation generated from reading ui file 'assets/ui/create_schedule.ui'
#
# Created by: PyQt6 UI code generator 6.9.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(462, 591)
        Dialog.setStyleSheet("background-color:     #333333")
        self.templates_combobox = QtWidgets.QComboBox(parent=Dialog)
        self.templates_combobox.setGeometry(QtCore.QRect(220, 40, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display Regular")
        font.setPointSize(18)
        self.templates_combobox.setFont(font)
        self.templates_combobox.setStyleSheet("border-radius : 10; \n"
"border : 0px solid white;\n"
"background-color: #0080ff;\n"
"color: white")
        self.templates_combobox.setEditable(False)
        self.templates_combobox.setObjectName("templates_combobox")
        self.DateEdit_2 = QtWidgets.QDateEdit(parent=Dialog)
        self.DateEdit_2.setGeometry(QtCore.QRect(10, 40, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display Regular")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.DateEdit_2.setFont(font)
        self.DateEdit_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.DateEdit_2.setStyleSheet("border-radius : 10; \n"
"border : 0px solid white;\n"
"background-color: #0080ff;\n"
"color: white")
        self.DateEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.DateEdit_2.setObjectName("DateEdit_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 441, 321))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: white")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Title")
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Text")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Text")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Text")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(133)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.finish_creating_button = QtWidgets.QPushButton(parent=Dialog)
        self.finish_creating_button.setGeometry(QtCore.QRect(140, 530, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display Bold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.finish_creating_button.setFont(font)
        self.finish_creating_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.finish_creating_button.setStyleSheet("color: white;\n"
"background-color: #0080ff;\n"
"border-radius: 12;\n"
"")
        self.finish_creating_button.setIconSize(QtCore.QSize(25, 25))
        self.finish_creating_button.setObjectName("finish_creating_button")
        self.label_66 = QtWidgets.QLabel(parent=Dialog)
        self.label_66.setGeometry(QtCore.QRect(10, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display Thin")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("color: white;\n"
"background-color: rgb(255,160,0, 0);\n"
"")
        self.label_66.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_66.setWordWrap(True)
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(parent=Dialog)
        self.label_67.setGeometry(QtCore.QRect(230, 10, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display Thin")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_67.setFont(font)
        self.label_67.setStyleSheet("color: white;\n"
"background-color: rgb(255,160,0, 0);\n"
"")
        self.label_67.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_67.setWordWrap(True)
        self.label_67.setObjectName("label_67")
        self.add_row_button = QtWidgets.QPushButton(parent=Dialog)
        self.add_row_button.setGeometry(QtCore.QRect(10, 430, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.add_row_button.setFont(font)
        self.add_row_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add_row_button.setStyleSheet("color: white;\n"
"background-color: #0080ff;\n"
"border-radius: 5;\n"
"")
        self.add_row_button.setIconSize(QtCore.QSize(25, 25))
        self.add_row_button.setObjectName("add_row_button")
        self.browse_file_button = QtWidgets.QPushButton(parent=Dialog)
        self.browse_file_button.setGeometry(QtCore.QRect(10, 460, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display Bold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.browse_file_button.setFont(font)
        self.browse_file_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.browse_file_button.setStyleSheet("color: white;\n"
"background-color: #0080ff;\n"
"border-radius: 8;\n"
"")
        self.browse_file_button.setIconSize(QtCore.QSize(25, 25))
        self.browse_file_button.setObjectName("browse_file_button")
        self.file_name_edit = QtWidgets.QLineEdit(parent=Dialog)
        self.file_name_edit.setGeometry(QtCore.QRect(140, 460, 311, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_name_edit.sizePolicy().hasHeightForWidth())
        self.file_name_edit.setSizePolicy(sizePolicy)
        self.file_name_edit.setMinimumSize(QtCore.QSize(291, 41))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(12)
        self.file_name_edit.setFont(font)
        self.file_name_edit.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.file_name_edit.setStyleSheet("border-radius: 9; \n"
"border: 2px solid white;\n"
"color: white")
        self.file_name_edit.setText("")
        self.file_name_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.file_name_edit.setObjectName("file_name_edit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Play time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Music"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.finish_creating_button.setText(_translate("Dialog", "Create"))
        self.label_66.setText(_translate("Dialog", "Date"))
        self.label_67.setText(_translate("Dialog", "Template"))
        self.add_row_button.setText(_translate("Dialog", "add row"))
        self.browse_file_button.setText(_translate("Dialog", "Browse file"))
