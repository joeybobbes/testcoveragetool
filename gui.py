#!/usr/bin/python

"""
ZetCode PyQt6 tutorial

This example shows text which
is entered in a QLineEdit
in a QLabel widget.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel,
        QLineEdit, QApplication, QTextEdit, QPushButton, QVBoxLayout)

import mcdc

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('MCDC Tool')
        
        # create objects
        self.textEdit = QTextEdit(self)
        self.btnPress = QPushButton("Calculate MCDC")

        # orient objects
        
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress)
        self.setLayout(layout)
        
        # connect to functions
        self.btnPress.clicked.connect(self.btnPress_Clicked)
    

    def btnPress_Clicked(self):

        self.foo = eval(self.textEdit.toPlainText())
        print(str(mcdc.tc_mcdc(self.foo)))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
