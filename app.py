from PyQt6.QtWidgets import QApplication
from main_win import MainWindow
import sys

def close():
    print("Closing...")

app = QApplication(sys.argv)
window = MainWindow()
window.showMaximized()
app.destroyed.connect(close)
app.exec()
