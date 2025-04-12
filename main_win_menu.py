from PyQt6.QtCore import QEvent
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu

class MainWinMenu(QMenu):
    def __init__(self):
        super().__init__()
        self.action_helo = QAction("Написать привет!", self)
        self.action_new = QAction("Написать новый!", self)
        self.action_close = QAction("Написать закрыть!", self)
        self.addAction(self.action_helo)
        self.addAction(self.action_new)
        self.addAction(self.action_close)
