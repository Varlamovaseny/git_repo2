import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.flag = False

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.flag:
            c = QPainter()
            c.begin(self)
            self.draw_circle(c)
            c.end()

    def draw_circle(self, c):
        c.setBrush(QColor(255, 255, 0))
        x, y = random.randint(30, 400), random.randint(30, 600)
        w = random.randint(10, 200)
        h = w
        c.drawEllipse(x, y, w, h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
