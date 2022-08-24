import sys
from PySide6 import QtWidgets
from Sheet import Sheet
from SoundProvider import SoundProvider



app = QtWidgets.QApplication(sys.argv)

sound_provider = SoundProvider()

sheet = Sheet(sound_provider)

sheet.show()
sys.exit(app.exec())
