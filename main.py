import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Teste")
l1=QLabel()
layout = QGridLayout()
layout.addWidget(QLabel('1'), 0, 0)
layout.addWidget(QLabel('2'), 0, 1)
layout.addWidget(QLabel('3'), 0, 2)
layout.addWidget(QLabel('4'), 1, 0)
layout.addWidget(QLabel('5'), 1, 1)
layout.addWidget(QLabel('6'), 1, 2)
layout.addWidget(QLabel('7'), 2, 0)
layout.addWidget(QLabel('8'), 2, 1)
layout.addWidget(QLabel('9'), 2, 2)
window.setLayout(layout)
window.show()

sys.exit(app.exec_())

