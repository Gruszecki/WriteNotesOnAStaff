from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Frequency import Frequency

width = 800
height = 600


class Sheet(QMainWindow):
    def __init__(self, sound_provider):
        super().__init__()

        self.setWindowTitle("Write notes on a staff")  # Window title
        self.setGeometry(100, 100, width, height)  # Window geometry: x, y, w, h

        self.sound_provider = sound_provider    # Object of the SoundProvider class

        # Menu bar
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("File")
        note_length_menu = main_menu.addMenu("Note length")
        play_menu = main_menu.addMenu("Play")

        # Menu: File: Export
        export_action = QAction("Export", self)
        file_menu.addAction(export_action)
        export_action.triggered.connect(self.export)

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

        delete_note_action = QAction("Delete last note", self)
        note_length_menu.addAction(delete_note_action)
        delete_note_action.triggered.connect(self.delete_note)

        # Menu: Play
        play_action = QAction("Play", self)
        play_menu.addAction(play_action)
        play_action.triggered.connect(self.play)

        # Menu: Stop
        stop_action = QAction("Stop", self)
        play_menu.addAction(stop_action)
        stop_action.triggered.connect(self.stop)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("Sheet: Left button pressed")

    def export(self):
        print("Sheet: Exporting")

    def clear(self):
        print("Sheet: Clearing")

    def set_ntoe_1(self):
        print("Sheet: Set note length: 1/1")
        self.sound_provider.note_length = 1

    def set_ntoe_2(self):
        print("Sheet: Set note length: 1/2")
        self.sound_provider.note_length = 2

    def set_ntoe_4(self):
        print("Sheet: Set note length: 1/4")
        self.sound_provider.note_length = 4

    def set_ntoe_8(self):
        print("Sheet: Set note length: 1/8")
        self.sound_provider.note_length = 8

    def delete_note(self):
        print("Sheet: Deleting last note")
        self.sound_provider.delete_last_note()

    def play(self):
        print("Sheet: Playing")
        self.sound_provider.play_melody()

    def stop(self):
        print("Sheet: Stop playing")
