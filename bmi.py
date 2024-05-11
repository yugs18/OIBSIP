from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QLabel, QGridLayout, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setting window's title
        self.setWindowTitle("BMI Calculator")
        # Fixing the size of the window
        self.setFixedSize(300, 200)

        self.layout = QGridLayout()

        self.widget = QWidget()
        # Setting the layout in widget
        self.widget.setLayout(self.layout)
        # setting widget in center
        self.setCentralWidget(self.widget)

        # Height Label
        self.height_label = QLabel("Enter height in cm: ")
        self.layout.addWidget(self.height_label, 0, 0)

        # Taking height from user
        self.height_input = QLineEdit()

        self.height_input.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.height_input, 0, 1)

        
        # Weight Label
        self.weight_label = QLabel("Enter weight in Kg: ")
        self.layout.addWidget(self.weight_label, 1, 0)

        # Taking Weight from user
        self.weight_input = QLineEdit()

        self.weight_input.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.weight_input, 1, 1)


        self.calculate = QPushButton("Calculate BMI")
        self.layout.addWidget(self.calculate, 2, 0, 1, 2)
        self.calculate.clicked.connect(self.calculate_bmi)


        self.result = QLabel()
        self.layout.addWidget(self.result, 3, 0, 1, 2)
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)


    def calculate_bmi(self):
        try:
            height = float(self.height_input.text()) / 100.0
            weight = float(self.weight_input.text())

            bmi = weight / (height ** 2)
            category = self.bmi_category(bmi)

            self.result.setText(f"BMI is {bmi:.2f}.\nCategory: {category}")

        except ValueError:
            QMessageBox.warning(self, "Error", "Enter valid height and weight.")


    def bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi <= 24.9:
            return "Healthy weight"
        elif bmi <= 29.9:
            return "Overweight"
        else:
            return "Obese"



app = QApplication([])

window = MainWindow()
window.show()

app.exec()