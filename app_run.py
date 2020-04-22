import sys
from qtDesigner import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QWidget
from dealWithApi import convertMath
from PyQt5 import QtCore
from showLaTeXImage import convertHtml

class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        self.ui.webEngineView.setHtml(convertHtml())
        self.ui.webEngineView.show()
        self.ui.pushButton_copy1.clicked.connect(self.copyText1)
        self.ui.pushButton_copy2.clicked.connect(self.copyText2)
        self.ui.pushButton_copy3.clicked.connect(self.copyText3)
        self.ui.pushButton_paste.clicked.connect(self.copyPasteBoard)
        self._clipBoard = QApplication.clipboard()
        self.ui.pushButton_convert.clicked.connect(self.convertLaTeX)

    def copyText1(self):
        text = self.ui.lineEdit.text()
        self._clipBoard.setText(text)

    def copyText2(self):
        text = self.ui.lineEdit_2.text()
        self._clipBoard.setText(text)

    def copyText3(self):
        text = self.ui.lineEdit_3.text()
        self._clipBoard.setText(text)

    def copyPasteBoard(self):
        data = self._clipBoard.mimeData()
        if data.hasImage():
            pixmap = self._clipBoard.pixmap()
            width = self.ui.label.width()
            height = self.ui.label.height()
            pixmap = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
            self.ui.label.setPixmap(pixmap)
        else:
            pass

    def convertLaTeX(self):
        fileName = "test.jpg"
        self.ui.label.pixmap().toImage().save(fileName)
        result = convertMath(fileName)
        self.ui.lineEdit.setText(result)
        self.ui.lineEdit_2.setText('$' + result + '$')
        self.ui.lineEdit_3.setText('$$' + result + '$$')
        self.ui.webEngineView.setHtml(convertHtml("$$" + result + "$$"))
        self.ui.webEngineView.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    ex.show()
    sys.exit(app.exec_())

