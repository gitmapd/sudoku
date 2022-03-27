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
        number=square_values[i][j]
        if number != None:
            qlabel=QLabel(f'{number}')
        else:
            if number == None:
                number=''
                lineedit=QLineEdit(f'{number}')
                lineedit.setFixedWidth(20)
                lineedit.setReadOnly(False)
                layout.addWidget(lineedit,i,j) 
        layout.addWidget(qlabel,i,j)
window.setLayout(layout)
window.show()

sys.exit(app.exec_())