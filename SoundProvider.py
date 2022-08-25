import matplotlib.pyplot as plt
import numpy as np
import simpleaudio as sa
import time

from pynput.keyboard import Key, Listener, KeyCode, Controller
from PySide6.QtWidgets import *
from scipy import signal

from Frequency import Frequency


class Note:
    def __init__(self, sound, octave, length):
        self.sound = sound
        self.octave = octave
        self.length = length

    def __str__(self):
        return f'{self.sound}{self.octave}'.ljust(6) + f'1/{self.length}\n'


class SoundProvider:
    def __init__(self):
        self.fs = 44100
        self.octave = 4
        self.wave = 0  # 0: sine, 1: sawtooth, 2: square
        self.bpm = 120
        self.note_length = 4
        self.melody = []
        self.text_area = None

    def play_note(self, sound, octave, note_length):
        note_length_s = ((60 / self.bpm) * 4) / note_length
        exp_build = f'Frequency.{sound}{octave}'    # Expression built for take frequency
        freq = eval(exp_build)

        t_r = np.linspace(0, note_length_s, int(note_length_s * self.fs), endpoint=False)
        n_r = freq * t_r * 2 * np.pi

        sound_calculation = np.linspace(1, 1, int(note_length_s * self.fs), endpoint=True)

        match self.wave:
            case 0:
                note_total = np.sin(n_r) * sound_calculation
            case 1:
                note_total = signal.sawtooth(n_r) * sound_calculation
            case 2:
                note_total = signal.square(n_r) * sound_calculation

        audio_total = note_total * (2 ** 15 - 1) / np.max(np.abs(note_total))
        audio_total = audio_total.astype(np.int16)

        sa.play_buffer(audio_total, 1, 2, self.fs)

    def play_melody(self):
        for note in self.melody:
            self.play_note(note.sound, note.octave, note.length)
            time.sleep((self.bpm / 60) / note.length)

    def is_piano_key(self, key):
        if key == KeyCode.from_char('a') or \
                key == KeyCode.from_char('w') or \
                key == KeyCode.from_char('s') or \
                key == KeyCode.from_char('e') or \
                key == KeyCode.from_char('d') or \
                key == KeyCode.from_char('f') or \
                key == KeyCode.from_char('t') or \
                key == KeyCode.from_char('g') or \
                key == KeyCode.from_char('y') or \
                key == KeyCode.from_char('h') or \
                key == KeyCode.from_char('u') or \
                key == KeyCode.from_char('j'):
            return str(key)[1:-1]
        else:
            return False

    def is_0to8_key(self, key):
        if key == KeyCode.from_char('0') or \
                key == KeyCode.from_char('1') or \
                key == KeyCode.from_char('2') or \
                key == KeyCode.from_char('3') or \
                key == KeyCode.from_char('4') or \
                key == KeyCode.from_char('5') or \
                key == KeyCode.from_char('6') or \
                key == KeyCode.from_char('7') or \
                key == KeyCode.from_char('8'):
            return str(key)[1:-1]
        else:
            return False

    def is_play_button(self, key):
        if key == KeyCode.from_char('p'):
            return str(key)[1:-1]
        else:
            return False

    def on_press(self, key):
        piano_key = self.is_piano_key(key)
        tone_h = self.is_0to8_key(key)
        play_melody = self.is_play_button(key)

        if piano_key:
            print(f"SoundProvider: Playing the sound ({Frequency.key_coverity[piano_key]}{self.octave} 1/{self.note_length})")
            self.play_note(Frequency.key_coverity[piano_key], self.octave, self.note_length)

            note = Note(Frequency.key_coverity[piano_key], self.octave, self.note_length)
            self.melody.append(note)
            self.insert_text_to_text_area(note.__str__())

        elif tone_h:
            print(f"SoundProvider: Changing octave to {tone_h}")
            self.octave = int(tone_h)
        elif play_melody:
            print("SoundProvider: Playing melody")
            self.play_melody()
        else:
            if (key == Key.up or key == Key.right) and self.octave < 8:
                print(f"SoundProvider: Changing octave to higher ({self.octave + 1})")
                self.octave += 1
            elif (key == Key.down or key == Key.left) and self.octave > 0:
                print(f"SoundProvider: Changing octave to lower ({self.octave - 1})")
                self.octave -= 1
            elif key == Key.backspace:
                print("SoundProvider: Please use Note length menu in menu bar")
                # print("SoundProvider: Deleting last note")
                # self.delete_last_note()

    def on_release(self, key):
        pass

    def insert_text_to_text_area(self, text):
        self.text_area.insertPlainText(text)

    def clear_melody_n_text(self):
        self.melody = []
        self.text_area.clear()
        self.text_area.insertPlainText('Sound Length\n')

    def delete_last_note(self):
        if len(self.melody):
            self.melody.pop()
            self.text_area.clear()
            self.text_area.insertPlainText('Sound Length\n')
            for note in self.melody:
                self.insert_text_to_text_area(note.__str__())
        else:
            print("There is no note to delete")