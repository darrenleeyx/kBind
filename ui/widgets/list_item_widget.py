from PyQt6.QtWidgets import QLabel, QWidget, QHBoxLayout, QPushButton

class ListItemWidget(QWidget):
    def __init__(self, text):
        super().__init__()
        layout = QHBoxLayout()
        self.label = QLabel(text)
        self.button = QPushButton("Enable/Disable")
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)