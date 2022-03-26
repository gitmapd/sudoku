import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Teste")
l1=QLabel()
layout = QGridLayout()
for i in range(9):
    for j in range(9):
        layout.addWidget(QLabel(f"{i+1}"), i, j)


window.setLayout(layout)
window.show()

sys.exit(app.exec_())

