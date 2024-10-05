import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QListWidgetItem

class ListItemWidget(QWidget):
    def __init__(self, text):
        super().__init__()
        layout = QHBoxLayout()
        self.label = QLabel(text)
        self.button = QPushButton("Enable/Disable")
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

app = QApplication([])

window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 400, 300)

# Create main layout
mainLayout = QVBoxLayout()

# Create layout for row of icons
iconLayout = QHBoxLayout()
addButton = QPushButton("Add")
deleteButton = QPushButton("Delete")
iconLayout.addWidget(addButton)
iconLayout.addWidget(deleteButton)

# Create layout for list of components
listLayout = QVBoxLayout()
listWidget = QListWidget()
listLayout.addWidget(listWidget)

# Add sample items to the list
for i in range(5):
    itemWidget = ListItemWidget(f"Binding {i+1}")
    listItem = QListWidgetItem(listWidget)
    listItem.setSizeHint(itemWidget.sizeHint())
    listWidget.setItemWidget(listItem, itemWidget)

# Add iconLayout and listLayout to mainLayout
mainLayout.addLayout(iconLayout)
mainLayout.addLayout(listLayout)

# Set main layout to window
window.setLayout(mainLayout)

window.show()
sys.exit(app.exec())