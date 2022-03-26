import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit
from random import randrange
app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Teste")
l1=QLabel()
layout = QGridLayout()


for i in range(9):
    a=randrange(0,10)
    for j in range(9):
        layout.addWidget(QLineEdit(f"{a}"), i, j)


window.setLayout(layout)
window.show()

sys.exit(app.exec_())