import sys
import math
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QBrush, QColor, QPen
draw_circle = False


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.clicked.clicked.connect(self.shar)

    def shar(self):
        global draw_circle
        draw_circle = True
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        if draw_circle:
            radius = random.randint(10, 100)
            center_x = self.width() // 2
            center_y = self.height() // 2
            brush = QBrush(QColor("yellow"))
            painter.setBrush(brush)
            painter.drawEllipse(center_x - radius, center_y - radius, 2 * radius, 2 * radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())