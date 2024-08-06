from PySide6.QtWidgets import QFileDialog

import sys
from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)  # Create the application instance

filename, _ = QFileDialog.getSaveFileName(
    parent= None,  
    caption="Save",    
    filter="HTML File (*.html)",     
)

if filename:
    print(f"File saved: {filename}")

sys.exit(app.exec())