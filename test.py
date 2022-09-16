from PyQt5.uic.properties import QtGui
import sys
from PyQt5.Qt import *
from PyQt5 import QtGui, QtWidgets


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("рисовашка")
        self.pix = QPixmap()
        self.lastPoint = QPoint()  # начальная точка
        self.endPoint = QPoint()  # конечная точк
        self.resize(1024, 980)

        block = QtWidgets.QWidget(self)
        block.setStyleSheet('background: #ffffff;')

        pixmap = QtGui.QPixmap('pngwing.com.png').scaled(20, 20)
        cursor = QtGui.QCursor(pixmap)
        block.setCursor(cursor)

        self.newAction = QAction(self)
        self.newAction.setText("&New")
        self.openAction = QAction("&Open...", self)
        self.saveAction = QAction("&Save", self)
        self.exitAction = QAction("&Exit", self)
        self.copyAction = QAction("&Copy", self)
        self.pasteAction = QAction("&Paste", self)
        self.cutAction = QAction("C&ut", self)
        self.helpContentAction = QAction("&Help Content", self)
        self.aboutAction = QAction("&About", self)
        self.roundAction = QAction("&RoundPen", self)
        self.penAction = QAction("&Pen", self)

        menuBar = self.menuBar()

        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        self.openAction.triggered.connect(self.fileopen)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)

        paintMenu = menuBar.addMenu("&Paint")
        paintMenu.addAction(self.roundAction)
        paintMenu.addAction(self.penAction)

        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)

        helpMenu = menuBar.addMenu(QIcon(":help-content.svg"), "&Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)

    def fileopen(self):
        str1 = QFileDialog.getOpenFileName()
        self.pix = QPixmap(str1[0])

    def paintEvent(self, event):
        pp = QPainter(self.pix)
        # Нарисуйте прямую линию в соответствии с двумя положениями до и после указателя мыши
        pp.drawLine(self.lastPoint, self.endPoint)
        # Сделать предыдущее значение координаты равным следующему значению координаты,
        # Таким образом можно нарисовать непрерывную линию
        self.lastPoint = self.endPoint
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)  # Рисуем на холсте

    def mousePressEvent(self, event):
        # Нажми левую кнопку мыши
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint

    # Событие движения мыши
    def mouseMoveEvent(self, event):
        # Перемещай мышь, удерживая нажатой левую кнопку мыши
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            # Сделать перекраску
            self.update()

    # Событие отпускания мыши
    def mouseReleaseEvent(self, event):
        # Отпустить левую кнопку мыши
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            # Сделать перекраску
            self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    sys.exit(app.exec_())
