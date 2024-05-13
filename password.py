import sys, string, random, pyperclip
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 200, 200)

        # Layouts
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        option_layout = QHBoxLayout()
        password_layout = QHBoxLayout()

        self.setLayout(main_layout)

        # Options
        self.len = QLabel("Enter password length: ", self)
        self.input = QLineEdit(self)
        self.input.setFixedWidth(50)
        self.input.setText("12")
        
        self.check_lower = QCheckBox("LowerCase", self)
        self.check_upper = QCheckBox("UpperCase", self)
        self.check_digits = QCheckBox("Digits", self)
        self.check_symbols = QCheckBox("Symbols", self)

        input_layout.addWidget(self.len)
        input_layout.addWidget(self.input)
        option_layout.addWidget(self.check_lower)
        option_layout.addWidget(self.check_upper)
        option_layout.addWidget(self.check_digits)
        option_layout.addWidget(self.check_symbols)


        # Password
        self.password = QLabel("Password: ", self)

        self.generate = QPushButton("Password Generate", self)
        self.generate.clicked.connect(self.password_generator)

        password_layout.addWidget(self.password)
        password_layout.addWidget(self.generate)


        # Copy to ClipBoard
        self.copy = QPushButton("Copy to Clipboard", self)
        self.copy.clicked.connect(self.copy_to_clipboard)


        # Main Layout
        main_layout.addLayout(input_layout)
        main_layout.addLayout(option_layout)
        main_layout.addLayout(password_layout)
        main_layout.addWidget(self.copy)
        self.show()


    def password_generator(self):
        length = int(self.input.text())

        if length < 4 or length > 32:
            QMessageBox.warning(self, "Error", "Length must be between 4 and 32.")
            return
        
        try:

            characters = ""

            if self.check_lower.isChecked():
                characters += string.ascii_lowercase

            if self.check_upper.isChecked():
                characters += string.ascii_uppercase

            if self.check_digits.isChecked():
                characters += string.digits

            if self.check_symbols.isChecked():
                characters += string.punctuation

            password = ""
            for _ in range(length):
                password += random.choice(characters)

            self.password.setText(password)


        except IndexError:
            QMessageBox.warning(self, "Error", "Please select at least one option.")
            return
        
    
    def copy_to_clipboard(self):
        pyperclip.copy(self.password.text())



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()