#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
import rqrqr  # module test.py

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWindow = QDialog()
    myUi = rqrqr.Ui_Dialog()
    myUi.setupUi(myMainWindow)
    myMainWindow.show()
    sys.exit(app.exec_())
