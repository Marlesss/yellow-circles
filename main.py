import sys
from random import randint
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen
from UI import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.circles = []
        self.pushButton.clicked.connect(self.generateCircles)

    def generateCircles(self):
        self.circles = [[randint(0, self.width() - 1), randint(0, self.height() - 1),
                         randint(1, min(self.width(),
                                        self.height()) // 5)] for _ in range(randint(1, 10))]
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for circle in self.circles:
            self.draw_circle(qp, circle)
        qp.end()

    def draw_circle(self, qp, circle):
        qp.setPen(QPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)), 4))
        x, y, r = circle
        qp.drawEllipse(x - r // 2, y - r // 2, r, r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
