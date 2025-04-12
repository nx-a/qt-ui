from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton


class AddWin(QWidget):
    def __init__(self, title: str, hide_after_write: bool = True):
        super().__init__()
        self._text = ""
        self._hide_after_write = hide_after_write
        self.setWindowTitle(title)
        self.resize(400, 100)
        self.action = QAction()
        win_vbox = QVBoxLayout()
        self.add_line = QLineEdit()
        add_btn = QPushButton("Сохранить")
        add_btn.clicked.connect(self.write)
        win_vbox.addWidget(self.add_line)
        win_vbox.addWidget(add_btn)
        self.setLayout(win_vbox)
    def write(self):
        self._text = self.add_line.text()
        self.add_line.clear()
        self.action.trigger()
        if self._hide_after_write:
            self.hide()
        else:
            self.add_line.setFocus()
    def getText(self):
        return self._text