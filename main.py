import sys
from tkinter.messagebox import YES
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit
from random import randrange

from numpy import square
from torch import square_
app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Sudoku")
l1=QLabel()
layout = QGridLayout()

square_values = [
    [5, 3, None, None, 7, None, None, None, None],
    [6, None, None, 1, 9, 5, None, None, None,...]]

for i in range(9):
    for j in range(9):
        a=[x for x in square_values]
        print(a)
        lineedit=QLineEdit(f"{*a,}")
        lineedit.setFixedWidth(20)
        lineedit.setReadOnly(True)
        #   lineedit.move(20 + 40 * j, 20 + 40 * i)
        layout.addWidget(lineedit,i,j)
window.setLayout(layout)
window.show()

sys.exit(app.exec_())