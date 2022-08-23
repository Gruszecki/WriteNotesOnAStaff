import sys
from PySide6 import QtWidgets
from Sheet import Sheet


app = QtWidgets.QApplication([])
sheet = Sheet()
sheet.show()
sys.exit(app.exec())
