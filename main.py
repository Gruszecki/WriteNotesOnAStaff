import sys
from PyQt5.QtWidgets import *
from Sheet import Sheet

App = QApplication(sys.argv)
sheet = Sheet()
sheet.show()
sys.exit(App.exec())
