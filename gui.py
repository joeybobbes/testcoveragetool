#!/usr/bin/python

"""
ZetCode PyQt6 tutorial

This example shows text which
is entered in a QLineEdit
in a QLabel widget.

Author: Jan Bodnar
Website: zetcode.com
"""

from inspect import signature
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel,
        QLineEdit, QApplication, QTextEdit, QPushButton, QVBoxLayout)

from PyQt6.QtWidgets import QApplication, \
    QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem
from PyQt6.QtGui import QIcon, QFont
import sys
 
import mcdc

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('MCDC Tool')
        
        # create objects
        self.textEdit = QTextEdit(self)
        self.btnPress1 = QPushButton("Calculate MCDC")
        self.btnPress2 = QPushButton("Calculate MCC")

        self.tableWidget = QTableWidget()
        self.rowCount=3
        self.columnCount=2
        self.tableWidget.setRowCount(self.rowCount)
        self.tableWidget.setColumnCount(self.columnCount)
        #tableWidget.setStyleSheet('background-color:yellow')
        self.tableWidget.setFont(QFont("Times New Roman", 12))
        #tableWidget.setItem(0, 0, QTableWidgetItem("FName"))
 
        # orient objects
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)
        
        # connect to functions
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)
    

    def btnPress1_Clicked(self):

        self.foo = eval(self.textEdit.toPlainText())
        print(self.textEdit.toPlainText())
        items = mcdc.tc_mcdc(self.foo)
        print(items)
        self.fillTable(items)
        
    def btnPress2_Clicked(self):

        self.foo = eval(self.textEdit.toPlainText())
        print(self.textEdit.toPlainText())
        n=len(self.getArguments(self.foo))
        items = mcdc.tc_gen(n)
        print(items)
        self.fillTable(items)
    
    def fillTable(self, items):
        
        self.clearTable()
        self.rowCount=len(items)
        self.columnCount=len(self.getArguments(self.foo))
        self.tableWidget.setRowCount(self.rowCount)
        self.tableWidget.setColumnCount(self.columnCount)
        for i in range(len(items)):
            for j in range (len(items[0])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(items[i][j])))
                self.show()
                
    def getArguments(self, foo):
        sig=signature(foo)
        return sig.parameters

    def clearTable(self):
        
        for i in range(self.rowCount):
            for j in range (self.columnCount):
                self.tableWidget.setItem(i, j, QTableWidgetItem(""))
     

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
