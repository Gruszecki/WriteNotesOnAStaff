import sys
from PySide6 import QtWidgets
from pynput.keyboard import Listener

from Sheet import Sheet
from SoundProvider import SoundProvider


app = QtWidgets.QApplication(sys.argv)

sound_provider = SoundProvider()

sheet = Sheet(sound_provider)

with Listener(on_press=sound_provider.on_press, on_release=sound_provider.on_release) as listener:
    sheet.show()
    sys.exit(app.exec())
