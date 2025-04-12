from PyQt6.QtWidgets import QApplication
from main_win import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.showMaximized()
app.exec()
print("Bye")
