from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QWidget, QPushButton, QVBoxLayout

from add_win import AddWin


class Books(QWidget):
    def __init__(self , action: QAction):
        super().__init__()
        self.action = action
        self.content = []
        self.lw = QListWidget()
        self.lw.currentItemChanged.connect(self.indexChanged)
        self.btn = QPushButton("Добавить")
        self.btn.clicked.connect(self.add)
        v = QVBoxLayout()
        v.setContentsMargins(0,0,0,0)
        v.addWidget(self.lw)
        v.addWidget(self.btn)
        self.setLayout(v)
        self.view()
        self.add_win = AddWin("Добавление книги")
        self.add_win.action.triggered.connect(self.write)
    def view(self):
        self.lw.clear()
        self.lw.addItems(self.content)
    def add(self):
        self.add_win.show()
    def indexChanged(self, index):
        if index is None:
            return
        for i, book in enumerate(self.content):
            if book == index.text():
                self.action.setData(i)
                self.action.trigger()
    def write(self):
        self.content.append(self.add_win.getText())
        self.view()
