import sys
from tkinter.messagebox import YES
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit

app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Sudoku")
layout = QGridLayout()

square_values = [
    [5, 3, None, None, 7, None, None, None, None],
    [6, None, None, 1, 9, 5, None, None, None],
    [None, 9,  8, None,None,None, None, 6, None],
    [8, None, None, None, 6, None, None, None, 3]
    ,[4, None, None, 8, None, 3, None, None, 1],
    [7, None, None, None, 2, None, None, None, 6],
    [None, 6, None, None, None, None, 2, 8, None],
    [None, None, None, 4, 1, 9, None, None, 5]
    ,[None, None, None, None, 8, None, None, 7, 9]]
for i in range(9):
    for j in range(9):
        row=square_values[i]
        number=row[j]
        if number==None:
            number=''
        lineedit=QLineEdit(f'{number}')
        lineedit.setFixedWidth(20)
        lineedit.setReadOnly(False)
    #lineedit.move(20 + 40 * j, 20 + 40 * i)
        layout.addWidget(lineedit,i,j) 
window.setLayout(layout)
window.show()

sys.exit(app.exec_())