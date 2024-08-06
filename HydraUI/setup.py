import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import *

import data 

class Setup(QDialog):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(800,400))
        self.setWindowTitle("Setup Website Configurations")
        
        self.canonical = QLineEdit("https://www.example.com/sample.html")
        self.poster = QLineEdit("https://picsum.photos/900/1600")
        self.logo = QLineEdit("https://picsum.photos/200")
        self.title = QLineEdit("Title")
        self.publisher = QLineEdit("Legit Publisher Name")
        self.submit = QPushButton("Save")
        self.submit.clicked.connect(self.accept)

        layout = QGridLayout()
        layout.addWidget(QLabel("Canonical Link:"),0,0,1,2)
        layout.addWidget(self.canonical,0,2,1,3)
        layout.addWidget(self.title,2,0,1,2)
        layout.addWidget(self.poster,2,3,1,2)
        layout.addWidget(self.publisher,4,0,1,2)
        layout.addWidget(self.logo,4,3,1,2)
        layout.addWidget(self.submit,5,4,1,1)
        layout.addWidget(QLabel("Title:"),1,0,1,1)
        layout.addWidget(QLabel("Poster:"),1,3,1,1)
        layout.addWidget(QLabel("Publisher:"),3,0,1,1)
        layout.addWidget(QLabel("Logo:"),3,3,1,1)

        #Set Styling
        self.setStyleSheet("""
        QDialog {
            color: #FFFFFF;                  
        }
        QLabel {
            color: #FFFFFF;
            font-size: 24px;
        }
        QPushButton {
            color: #FFFFFF; 
            background-color: #042F2E;
            border-width: 5px;
            border-style: solid;
            border-radius: 20px; 
            height: 100px               
            font-size: 20px;                
        }
        QLineEdit {
            color: #FFFFFF;
            font-size: 24px;
            height: 30px;
            margin: 2px;                   
        }
        """)

        self.setLayout(layout)
        self.show()

    def getData(self):
        a = self.canonical.text()
        b = self.title.text()
        c = self.publisher.text()
        d = self.poster.text()
        e = self.logo.text()

        self.data = data.Start(a,b,c,d,e)
        return self.data
    
    def accept(self):
        self.close()
        

def main():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))

    wid = Setup()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()