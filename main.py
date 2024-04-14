
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QPushButton,QHBoxLayout, QLabel,QVBoxLayout,
    QListWidget, QFileDialog
)
import os
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Easy editor')
main_win.resize(700,500)
lb_image = QLabel('Картинка')
lb_files = QListWidget()
btn_dir = QPushButton('Папка')

btn_left = QPushButton('влево')
btn_right = QPushButton('вправо')
btn_zerk = QPushButton('Зеркало')
btn_rezk = QPushButton('Резкость')
btn_bw = QPushButton('Ч\Б')
row = QHBoxLayout()
row_tools = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lb_files)
col2.addWidget(lb_image,95)
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_rezk)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_zerk)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)
row.addLayout(col1, 20)
row.addLayout(col2, 80)
main_win.setLayout(row)

def workdlr():
    global workdlr
    workdlr = QFileDialog.getExistingDirectory()
def showfilenameList():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdlr()


main_win.show()
app.exec_()

