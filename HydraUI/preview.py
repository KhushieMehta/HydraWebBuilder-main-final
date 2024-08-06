import sys
import html
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout
from PySide6.QtCore import QSize
from PySide6.QtWebEngineWidgets import QWebEngineView

class Preview(QWidget):
    def __init__(self):
        super().__init__()
        # Setting Reload Button
        self.reload = QPushButton("Reload")
        self.reload.setFixedSize(QSize(80,40))
        self.reload.show()

        # Setting Reload Button
        self.save = QPushButton("Save")
        self.save.setFixedSize(QSize(80,40))
        self.save.show()

        #initialising webview
        self.web = QWebEngineView()
        self.web.setFixedSize(QSize(400,700))
        self.web.show()

        #setting up layout
        self.setFixedSize(QSize(650,725))

        layout = QHBoxLayout()
        layout.addWidget(self.save)
        layout.addWidget(self.web)
        layout.addWidget(self.reload)
        self.setLayout(layout)
        self.show()

        self.setStyleSheet("""
        QPushButton{
        background-color: #4F4F4F;
        color: #ffffff;
        }
        """)

        #setting up signals
        #self.reload.clicked.connect(self.reload_page)

    #Tester Functions
    def set_html(self, html):
        self.web.setHtml(html)  

    def reload_page(self):
        self.web.reload()


def main():
    app = QApplication(sys.argv)

    wid = Preview()
    wid.set_html(html.html)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
