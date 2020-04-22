from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore


class ImageArea(QLabel):

    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("text/uri-list"):
            event.acceptProposedAction()

    def dropEvent(self, event) -> None:
        text = event.mimeData().text()
        if text.endswith(".png") or text.endswith(".jpg") or text.endswith(".jpeg"):
            path = event.mimeData().urls()[0].toLocalFile()
            pixmap = QPixmap(path)
            width = self.width()
            height = self.height()
            pixmap = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
            self.setPixmap(pixmap)

