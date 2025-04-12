from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QListWidget, QVBoxLayout, QPushButton, QWidget, QLineEdit
from scipy.sparse import data

from add_win import AddWin


class Tasks(QWidget):
    def __init__(self, action:QAction):
        super().__init__()
        self.current_book = 0
        self.data = []
        self.action = action
        self.action.triggered.connect(self.onActionTriggered)
        self.lw = QListWidget()
        self.btn = QPushButton("Добавить")
        self.btn.clicked.connect(self.add)
        v = QVBoxLayout()
        v.setContentsMargins(0,0,0,0)
        v.addWidget(self.lw)
        v.addWidget(self.btn)
        self.setLayout(v)
        self.add_win = AddWin("Tasks", False)
        self.add_win.action.triggered.connect(self.write)
    def onActionTriggered(self):
        self.current_book = self.action.data()
        while True:
            if len(self.data) <= self.current_book:
                self.data.append([])
            else:
                break
        self.view()
    def add(self):
        print("add")
        self.add_win.show()
    def write(self):
        self.data[self.current_book].append(self.add_win.getText())
        self.view()
    def view(self):
        lines = self.data[self.current_book]
        self.lw.clear()
        self.lw.addItems(lines)
