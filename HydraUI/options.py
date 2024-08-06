import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor


class AnimationOptions(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(350,200))
        
        #Main
        items = ["None", "drop","fade-in", "fly-in-bottom","fly-in-left","fly-in-right","fly-in-top","pulse","rotate-in-left","rotate-in-right","twirl-in","whoosh-in-left","whoosh-in-right","pan-left","pan-right","pan-down","pan-up","pan-left","zoom-in","zoom-out"]
        self.mainCombo = QComboBox()
        self.mainCombo.addItems(items)
        #self.mainCombo.activated.connect(self.getdata)


        main = QWidget()
        mainl = QHBoxLayout()
        mainl.addWidget(QLabel("Main"))
        mainl.addWidget(self.mainCombo)
        main.setLayout(mainl)

        #Heading
        self.headCombo = QComboBox()
        self.headCombo.addItems(items)
        #self.headCombo.activated.connect(self.getdata)


        head = QWidget()
        headl = QHBoxLayout()
        headl.addWidget(QLabel("Heading"))
        headl.addWidget(self.headCombo)
        head.setLayout(headl)

        #Content
        self.contentCombo = QComboBox()
        self.contentCombo.addItems(items)
        #self.contentCombo.activated.connect(self.getdata)

        content = QWidget()
        contentl = QHBoxLayout()
        contentl.addWidget(QLabel("Content"))
        contentl.addWidget(self.contentCombo)
        content.setLayout(contentl)

        #boundingbox
        box = QWidget()
        boxl = QVBoxLayout()
        boxl.addWidget(main)
        boxl.addWidget(head)
        boxl.addWidget(content)
        box.setLayout(boxl)
        
        #layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Animation Settings"))
        layout.addWidget(box)
        self.setLayout(layout)
        self.show()

    def getdata(self, _):
        mc = self.mainCombo.currentText()
        hc = self.headCombo.currentText()
        cc = self.contentCombo.currentText()
        print(f"main: {mc}, heading: {hc}, content: {cc}")

class ColorPicker(QPushButton):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(150,30))
        self.setStyleSheet("background-color: #FFFFFF;")

        self.show()

        self.clicked.connect(self.get_color)

        self.selected_color = QColor("FFFFFF") # Initialize selected color variable

    def get_color(self):

        color = QColorDialog.getColor()  

        if color.isValid():  
            self.selected_color = color
            self.setStyleSheet(f"background-color: {color.name()};")
            #print(color.name())

class HeaderOptions(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(350,200))
        
        #Font
        items = ['Courier New', 'Times New Roman', 'Ariel', 'Brush Script MT', 'Garamond', 'Georgia', 'Trebuchet MS', 'Tahoma', 'Verdana']
        self.fontCombo = QComboBox()
        self.fontCombo.addItems(items)
        #self.fontCombo.activated.connect(self.getdata)


        font = QWidget()
        fontl = QHBoxLayout()
        fontl.addWidget(QLabel("Font"))
        fontl.addWidget(self.fontCombo)
        font.setLayout(fontl)

        #Size
        self.sizebox = QSpinBox()
        self.sizebox.setValue(16)
        #self.sizebox.valueChanged.connect(self.getdata)

        size = QWidget()
        sizel = QHBoxLayout()
        sizel.addWidget(QLabel("Font Size"))
        sizel.addWidget(self.sizebox)
        size.setLayout(sizel)

        #Color
        self.colorBox = ColorPicker()

        color = QWidget()
        colorl = QHBoxLayout()
        colorl.addWidget(QLabel("Font Color"))
        colorl.addWidget(self.colorBox)
        color.setLayout(colorl)

        #boundingbox
        box = QWidget()
        boxl = QVBoxLayout()
        boxl.addWidget(font)
        boxl.addWidget(size)
        boxl.addWidget(color)
        box.setLayout(boxl)
        
        #layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Header Settings"))
        layout.addWidget(box)
        self.setLayout(layout)
        self.show()

    def getdata(self, _):
        font = self.fontCombo.currentText()
        size = self.sizebox.value()
        print(f"font: {font}, size: {size}")

class ContentOptions(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(350,200))
        
        #Font
        items = ['Courier New', 'Times New Roman', 'Ariel', 'Brush Script MT', 'Garamond', 'Georgia', 'Trebuchet MS', 'Tahoma', 'Verdana']
        self.fontCombo = QComboBox()
        self.fontCombo.addItems(items)
        #self.fontCombo.activated.connect(self.getdata)


        font = QWidget()
        fontl = QHBoxLayout()
        fontl.addWidget(QLabel("Font"))
        fontl.addWidget(self.fontCombo)
        font.setLayout(fontl)

        #Size
        self.sizebox = QSpinBox()
        self.sizebox.setValue(16)
        #self.sizebox.valueChanged.connect(self.getdata)

        size = QWidget()
        sizel = QHBoxLayout()
        sizel.addWidget(QLabel("Font Size"))
        sizel.addWidget(self.sizebox)
        size.setLayout(sizel)

        #Color
        self.colorBox = ColorPicker()

        color = QWidget()
        colorl = QHBoxLayout()
        colorl.addWidget(QLabel("Font Color"))
        colorl.addWidget(self.colorBox)
        color.setLayout(colorl)

        #boundingbox
        box = QWidget()
        boxl = QVBoxLayout()
        boxl.addWidget(font)
        boxl.addWidget(size)
        boxl.addWidget(color)
        box.setLayout(boxl)
        
        #layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Content Settings"))
        layout.addWidget(box)
        self.setLayout(layout)
        self.show()

    def getdata(self, _):
        font = self.fontCombo.currentText()
        size = self.sizebox.value()
        print(f"font: {font}, size: {size}")

class Options(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(350,750))

        self.heading = HeaderOptions()
        self.animate = AnimationOptions()
        self.content = ContentOptions()

        # Setting Layout
        layout = QVBoxLayout()
        layout.addWidget(self.heading)
        layout.addWidget(self.content)
        layout.addWidget(self.animate)
        self.setLayout(layout)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Options()
    sys.exit(app.exec())