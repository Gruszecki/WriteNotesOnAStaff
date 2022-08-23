from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Sheet(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Write notes on a staff")  # Window title
        self.setGeometry(100, 100, 800, 600)  # Window geometry: x, y, w, h

        self.image = QImage(self.size(), QImage.Format_RGB32)   # Image object
        self.image.fill(Qt.white)   # Paint it white

        self.note_length = 4

        # Menu bar
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("File")
        note_length_menu = main_menu.addMenu("Note length")
        play_menu = main_menu.addMenu("Play")

        # Menu: File: Export
        export_action = QAction("Export", self)
        file_menu.addAction(export_action)
        export_action.triggered.connect(self.save)

        # Menu: File: Clear
        clear_action = QAction("Clear", self)
        file_menu.addAction(clear_action)
        clear_action.triggered.connect(self.clear)

        # Menu: Note length
        note_1 = QAction("1/1", self)
        note_length_menu.addAction(note_1)
        note_1.triggered.connect(self.set_ntoe_1)

        note_2 = QAction("1/2", self)
        note_length_menu.addAction(note_2)
        note_2.triggered.connect(self.set_ntoe_2)

        note_4 = QAction("1/4", self)
        note_length_menu.addAction(note_4)
        note_4.triggered.connect(self.set_ntoe_4)

        note_8 = QAction("1/8", self)
        note_length_menu.addAction(note_8)
        note_8.triggered.connect(self.set_ntoe_8)

        # Menu: Play
        play_action = QAction("Play", self)
        play_menu.addAction(play_action)
        play_action.triggered.connect(self.play)

        # Menu: Stop
        stop_action = QAction("Stop", self)
        play_menu.addAction(stop_action)
        stop_action.triggered.connect(self.stop)

    def save(self):
        print("Saved")

    def clear(self):
        print("Cleared")

    def set_ntoe_1(self):
        print("Set note length: 1/1")

    def set_ntoe_2(self):
        print("Set note length: 1/2")

    def set_ntoe_4(self):
        print("Set note length: 1/4")

    def set_ntoe_8(self):
        print("Set note length: 1/8")

    def play(self):
        print("Playing")

    def stop(self):
        print("Stop playing")
