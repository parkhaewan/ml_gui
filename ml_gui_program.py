from PyQt5.QtWidgets import *
import sys, pickle
from PyQt5 import uic, QtWidgets
from data_visualize import data_

# ui 클래스라는 객체 생성
class UI(QMainWindow) :
    def __init__(self) :
        super(UI, self).__init__()
        uic.loadUi('ui_files/mainwindow.ui', self)

        # self.show()

        global data, steps
        data = data_()

        # 버튼 등록(버튼을 통한 기능 구현)
        self.Browse = self.findChild(QPushButton, "Browse")
        self.columns = self.findChild(QListWidget, "listWidget")

        self.Browse.clicked.connect(self.get_csv)

    def filldetails(self, fleg=1) :
        if fleg == 0 :
            self.df = data.read_file(self.file_path)

        self.columns.clear()
        self.column_list = data.get_column_list(self.df)
        # print(self.column_list)
        # column_list 가 어떻게 나오는지 한번 확인해봄

        for i, j in enumerate(self.column_list):
            stri = f'{j}------{str(self.df[j].dtype)}'
            print(stri)

            # listWidget 에 채워넣는 방법은 메소드 하나만(insertItem) 쓰면 됨
            self.columns.insertItem(i, stri)

    def get_csv(self) :
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "csv(*.csv)")
        # _ = : return 을 해주는데 이 변수는 안써먹으려고 공백으로 채워넣음
        self.columns.clear()

        if self.file_path != "" :
            self.filldetails(0)

if __name__ == '__main__' :
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    window.show() # 여기서 show를 확인하므로 self.show는 주석처리

    sys.exit(app.exec_())