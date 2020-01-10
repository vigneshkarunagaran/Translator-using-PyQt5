from PyQt5 import QtCore, QtWidgets
from googletrans import Translator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(361, 179)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btTranslate = QtWidgets.QPushButton(self.centralwidget)
        self.btTranslate.setGeometry(QtCore.QRect(260, 50, 91, 23))
        self.btTranslate.setObjectName("Translate")
        self.language = QtWidgets.QComboBox(self.centralwidget)
        self.language.setGeometry(QtCore.QRect(260, 20, 91, 22))
        self.language.setObjectName("comboBox")
        self.language.addItem("")
        self.language.addItem("")
        self.language.addItem("")
        self.language.addItem("")
        self.language.addItem("")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 89, 341, 81))
        self.groupBox.setObjectName("groupBox")
        self.output = QtWidgets.QLabel(self.groupBox)
        self.output.setGeometry(QtCore.QRect(10, 20, 321, 51))
        self.output.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.output.setObjectName("label")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(10, 10, 241, 71))
        self.input.setMinimumSize(QtCore.QSize(241, 71))
        self.input.setMaximumSize(QtCore.QSize(241, 16777215))
        self.input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.input.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btTranslate.clicked.connect(self.transFunction)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translator"))
        MainWindow.setFixedSize(361,179)
        self.btTranslate.setText(_translate("MainWindow", "Translate"))
        self.language.setItemText(0, _translate("MainWindow", "English"))
        self.language.setItemText(1, _translate("MainWindow", "Hindi"))
        self.language.setItemText(2, _translate("MainWindow", "Tamil"))
        self.language.setItemText(3, _translate("MainWindow", "Telugu"))
        self.language.setItemText(4, _translate("MainWindow", "Malayalam"))
        self.groupBox.setTitle(_translate("MainWindow", "Translated text"))
        self.output.setText(_translate("MainWindow", ""))

    def transFunction(self):
        languages =['en','hi', 'ta','te','ml']
        lan = languages[int(self.language.currentIndex())]
        word = self.input.text()
        translatorMod = Translator()
        out = translatorMod.translate(word, lan)
        self.output.setText(out.text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
