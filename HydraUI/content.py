import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import *


class Content(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(350,750))

        # Image/Video Options
        #self.op = QPushButton("O")
        ##self.op.clicked.connect(self.getdata)
        #self.op.setFixedSize(QSize(50,50))

        self.imgurl = QLineEdit()
        self.imgurl.setFixedSize(QSize(330,30))

        self.radioImg = QRadioButton("Image")
        self.radioVideo = QRadioButton("Video")
        self.radioImg.setChecked(True)

        self.radio = QButtonGroup()
        self.radio.addButton(self.radioImg)
        self.radio.addButton(self.radioVideo)
  
        a = QWidget()
        al = QHBoxLayout()
        al.addWidget(QLabel("Image/Video URL"), alignment= Qt.AlignLeft)
        #al.addWidget(self.op, alignment= Qt.AlignRight)
        a.setLayout(al)
        a.setFixedSize(QSize(330,70))

        #Header Options
        self.header = QCheckBox("Header")
        self.headerdata = QTextEdit()
        self.headerdata.setFixedSize(QSize(330,100))

        #Content Options
        self.content = QCheckBox("Content")
        self.contentdata = QTextEdit()
        self.contentdata.setFixedSize(QSize(330,150))

        # Create layout
        layout = QVBoxLayout(self)
        layout.addWidget(a)
        layout.addWidget(self.imgurl)
        layout.addWidget(self.radioImg)
        layout.addWidget(self.radioVideo)
        layout.addWidget(self.header)
        layout.addWidget(self.headerdata)
        layout.addWidget(self.content)
        layout.addWidget(self.contentdata)

        self.setStyleSheet("""
        QLineEdit, QTextEdit{
            background-color: #2D2D2D;
            border: none;
        }
        """)

        # Set layout
        self.setLayout(layout)
        self.show()

        # Tester Funtions for individual Widget (Combined use in Builder.py)
#    def getdata(self):
#        url = self.imgurl.text()
#        hd = self.headerdata.toPlainText()
#        cd = self.contentdata.toPlainText()
#        h = self.header.isChecked()
#        c = self.content.isChecked()
#        iv = self.radio.checkedButton().text()
#        print(f"Header: {h} Checked: {c} Img/Vid: {iv}")
#        print(f"""Url: {url}
#Header Data: {hd}
#Content Data: {cd}""")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Content()
    sys.exit(app.exec())
