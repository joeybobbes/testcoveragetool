from PyQt6.QtWidgets import QApplication, \
    QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem
from PyQt6.QtGui import QIcon, QFont
import sys
 
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 TableWidget")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500,200, 500,400)
 
        vbox = QVBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(3)
        tableWidget.setColumnCount(3)
        tableWidget.setStyleSheet('background-color:yellow')
        tableWidget.setFont(QFont("Times New Roman", 12))
        tableWidget.setItem(0, 0, QTableWidgetItem("FName"))
        tableWidget.setItem(0, 1, QTableWidgetItem("Lname"))
        tableWidget.setItem(0, 2, QTableWidgetItem("email"))
 
        tableWidget.setItem(1, 0, QTableWidgetItem("Parwiz"))
        tableWidget.setItem(1, 1, QTableWidgetItem("Forogh"))
        tableWidget.setItem(1, 2, QTableWidgetItem("parwiz@gmail.com"))
 
        tableWidget.setItem(2, 0, QTableWidgetItem("John"))
        tableWidget.setItem(2, 1, QTableWidgetItem("Doe"))
        tableWidget.setItem(2, 2, QTableWidgetItem("john@gmail.com"))
 
        vbox.addWidget(tableWidget)
 
        self.setLayout(vbox)
 
 
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())