import sys
from pynput import keyboard
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QListWidgetItem
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt
from managers.keyboard_manager import KeyboardManager
from persistence.database_manager import DatabaseManager
from persistence.bindings.binding_repository import BindingRepository
from ui.widgets.list_item_widget import ListItemWidget

handle_key_press_active = True

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyQt App")
        self.setGeometry(100, 100, 400, 300)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus) 
        
        mainLayout = QVBoxLayout()

        iconLayout = QHBoxLayout()
        addButton = QPushButton("Add")
        deleteButton = QPushButton("Delete")
        iconLayout.addWidget(addButton)
        iconLayout.addWidget(deleteButton)

        listLayout = QVBoxLayout()
        listWidget = QListWidget()
        listLayout.addWidget(listWidget)

        bindings = binding_repo.get_bindings()
        for binding in bindings:
            itemWidget = ListItemWidget(binding.name)
            listItem = QListWidgetItem(listWidget)
            listItem.setSizeHint(itemWidget.sizeHint())
            listWidget.setItemWidget(listItem, itemWidget)

        # Add iconLayout and listLayout to mainLayout
        mainLayout.addLayout(iconLayout)
        mainLayout.addLayout(listLayout)

        # Set main layout to window
        self.setLayout(mainLayout)

    def keyPressEvent(self, event: QKeyEvent):
        key_sequence = event.text()
        print(f"Key pressed: {key_sequence}")  # Debugging statement
        handle_key_press(key_sequence)

def handle_key_press(key):
    global handle_key_press_active
    if not handle_key_press_active:
        return

    try:
        key_sequence = key.char
        binding = binding_repo.get_by_bind_from(key_sequence)
        if binding:
            handle_key_press_active = False
            KeyboardManager.tap_keys(binding.get_bind_to())
            handle_key_press_active = True
    except AttributeError:
        print(f"Special key pressed: {key}")

session = DatabaseManager.setup_database()
#DatabaseManager.insert_records(session)
binding_repo = BindingRepository(session)

app = QApplication([])

window = MainWindow()
window.show()
print("Started")

# Set up pynput listener
listener = keyboard.Listener(on_press=handle_key_press)
listener.start()

sys.exit(app.exec())