import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import *

class PageOptions(QDialog):
    def __init__(self):
        super().__init__()
        self.clicked = None

        self.plainTop = QPushButton("Plain Top")
        self.plainBottom = QPushButton("Plain Bottom")
        self.gradientTop = QPushButton("Gradient Top")
        self.gradientBottom = QPushButton("Gradient Bottom")

        self.plainTop.clicked.connect(self.handle)
        self.plainBottom.clicked.connect(self.handle)  
        self.gradientTop.clicked.connect(self.handle)
        self.gradientBottom.clicked.connect(self.handle)

        layout = QGridLayout()
        layout.addWidget(self.plainTop,0,0)
        layout.addWidget(self.plainBottom,0,1)
        layout.addWidget(self.gradientTop,1,0)
        layout.addWidget(self.gradientBottom,1,1)

        self.setLayout(layout)
        self.show()
    
    def handle(self):
        self.clicked = self.sender().text()
        print(self.clicked)
        self.close()

    def getData(self):
        return self.clicked

    
def main():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))

    wid = PageOptions()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()