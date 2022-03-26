import sys
from tkinter.messagebox import YES
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit
from random import randrange
app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Teste")
l1=QLabel()
layout = QGridLayout()


for i in range(9):
    for j in range(9):
        a=randrange(1,10)
        lineedit=QLineEdit(f"{a}")
        lineedit.setFixedWidth(20)
        lineedit.setReadOnly(True)
        lineedit.move(20 + 40 * j, 20 + 40 * i)
        layout.addWidget(lineedit,i,j)
window.setLayout(layout)
window.show()

sys.exit(app.exec_())