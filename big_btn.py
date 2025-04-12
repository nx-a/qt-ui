from PyQt6.QtWidgets import QPushButton


class BigButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Большая кнопка")
        self.clicked.connect(self._on_clicked)
    def _on_clicked(self):
        self.setEnabled(False)