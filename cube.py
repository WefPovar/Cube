import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame

# нужно собрать флаг россии
class Cube(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rubik\'s Cube')
        self.setGeometry(100, 100, 300, 300)
        self.colors = {
            'white': QColor(255, 255, 255),
            'blue': QColor(0, 0, 255),
            'red': QColor(255, 0, 0),
        }
        self.matrix = [['white', 'white', 'blue'], ['red', 'blue', 'red'], ['red', 'white', 'blue']]
        self.selected = None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        width = self.width() // 3
        height = self.height() // 3

        for i in range(3):
            for j in range(3):
                color = self.colors[self.matrix[i][j]]
                painter.setBrush(color)
                painter.drawRect(i * width, j * height, width, height)

                painter.setBrush(Qt.NoBrush)
                painter.setPen(QColor(0, 0, 0))
                painter.drawRect(i * width, j * height, width, height)

        if self.selected:
            i, j, direction = self.selected
            if direction == 'row':
                painter.setBrush(QColor(255, 255, 255, 128))
                painter.drawRect(0, j * height, self.width(), height)
            else:
                painter.setBrush(QColor(255, 255, 255, 128))
                painter.drawRect(i * width, 0, width, self.height())

    def check_win(self):
        win = [['white', 'blue', 'red'], ['white', 'blue', 'red'], ['white', 'blue', 'red']]
        return self.matrix == win


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rubik\'s Cube')
        self.setGeometry(100, 100, 300, 300)
        self.cube = Cube()
        self.setCentralWidget(self.cube)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_R:
            temp = self.cube.matrix
            temp2 = [temp[0][0], temp[1][0], temp[2][0]]
            temp[0][0] = temp2[2]
            temp[1][0] = temp2[0]
            temp[2][0] = temp2[1]
            self.cube.matrix = temp
        elif event.key() == Qt.Key_F:
            temp = self.cube.matrix
            temp2 = [temp[0][1], temp[1][1], temp[2][1]]
            temp[0][1] = temp2[2]
            temp[1][1] = temp2[0]
            temp[2][1] = temp2[1]
            self.cube.matrix = temp
        elif event.key() == Qt.Key_V:
            temp = self.cube.matrix
            temp2 = [temp[0][2], temp[1][2], temp[2][2]]
            temp[0][2] = temp2[2]
            temp[1][2] = temp2[0]
            temp[2][2] = temp2[1]
            self.cube.matrix = temp
        elif event.key() == Qt.Key_Q:
            temp = self.cube.matrix
            temp2 = [temp[0][0], temp[0][1], temp[0][2]]
            temp[0][0] = temp2[2]
            temp[0][1] = temp2[0]
            temp[0][2] = temp2[1]
            self.cube.matrix = temp
        elif event.key() == Qt.Key_W:
            temp = self.cube.matrix
            temp2 = [temp[1][0], temp[1][1], temp[1][2]]
            temp[1][0] = temp2[2]
            temp[1][1] = temp2[0]
            temp[1][2] = temp2[1]
            self.cube.matrix = temp
        elif event.key() == Qt.Key_E:
            temp = self.cube.matrix
            temp2 = [temp[2][0], temp[2][1], temp[2][2]]
            temp[2][0] = temp2[2]
            temp[2][1] = temp2[0]
            temp[2][2] = temp2[1]
            self.cube.matrix = temp
        else:
            super().keyPressEvent(event)
        self.repaint()
        if self.cube.check_win():
            self.setWindowTitle('You Win!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
