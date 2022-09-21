import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi



class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('LAB2_AAA.ui', self)



        self.label_img.setPixmap(QPixmap('aa.png'))
        self.label_img.setScaledContents(True)


        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.close)


    def solve(self):
        try:
            a = float(self.lineEdit_a.text())
            b = float(self.lineEdit_b.text())
            d = float(self.lineEdit_d.text())
            c = float(self.lineEdit_d.text())
            x = float(self.lineEdit_x.text())
            if x <= 5:
                otvet = (a ** 2 * c + b ** 2 - d) / x
            else:
                otvet = x**2 + 5
            self.label_otvet.setText('Ответ: ' + str(format(otvet, '.2f')))
        except:
            self.label_otvet.setStyleSheet('QLabel {color:red}')
            self.label_otvet.setText(
                'Ошибка!')


    def clear(self):
        self.lineEdit_a.setText('')
        self.lineEdit_b.setText('')
        self.lineEdit_d.setText('')
        self.lineEdit_c.setText('')
        self.lineEdit_x.setText('')
        self.label_otvet.setText('Ответ: ')



app = QApplication(sys.argv)
window = Main()  #
window.show()  #
sys.exit(app.exec_())  #

if __name__ == '__main__':
 main()


