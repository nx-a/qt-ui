from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from books import Books
from main_win_menu import MainWinMenu
from tasks import Tasks
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            books_data = []
            task_data = []
            for key in data:
                books_data.append(key)
                task_data.append(data[key])
        self.setWindowTitle("Новое окно")
        self.resize(400, 600)
        action =QAction()
        self.books = Books(action)
        self.books.content = books_data
        self.books.view()
        self.books.setMaximumWidth(400)
        self.tasks = Tasks(action)
        self.tasks.data = task_data
        self.tasks.view()
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.books)
        hLayout.addWidget(self.tasks)
        container = QWidget()
        container.setLayout(hLayout)
        self.setCentralWidget(container)
    def contextMenuEvent(self, event):
        menu = MainWinMenu()
        menu.exec(event.globalPos())
    def closeEvent(self, event):
        data = {}
        for i, name in enumerate(self.books.content):
            data[name] = self.tasks.data[i]
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("close")