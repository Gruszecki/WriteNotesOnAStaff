import numpy as np
import simpleaudio as sa
from pynput.keyboard import Key, Listener, KeyCode, Controller
import matplotlib.pyplot as plt
from scipy import signal


class SoundProvider:
    def __init__(self):
        self.fs = 44100
        self.SOUND_H = 4
        self.WAVE = 0  # 0: sine, 1: sawtooth, 2: square
        self.BPM = 120

    def play_note(self, freq, note_length):
        note_length_s = (self.BPM / 60) / note_length

        t_r = np.linspace(0, note_length_s, int(note_length_s * self.fs), endpoint=False)
        n_r = freq * t_r * 2 * np.pi

        sound_calculation = np.linspace(1, 1, int(note_length_s * self.fs), endpoint=True)

        match self.WAVE:
            case 0:
                note_total = np.sin(n_r) * sound_calculation
            case 1:
                note_total = signal.sawtooth(n_r) * sound_calculation
            case 2:
                note_total = signal.square(n_r) * sound_calculation

        audio_total = note_total * (2 ** 15 - 1) / np.max(np.abs(note_total))
        audio_total = audio_total.astype(np.int16)

        sa.play_buffer(audio_total, 1, 2, self.fs)

    def is_piano_key(self, key):
        # if key == KeyCode.from_char('a') or \
        #         key == KeyCode.from_char('w') or \
        #         key == KeyCode.from_char('s') or \
        #         key == KeyCode.from_char('e') or \
        #         key == KeyCode.from_char('d') or \
        #         key == KeyCode.from_char('f') or \
        #         key == KeyCode.from_char('t') or \
        #         key == KeyCode.from_char('g') or \
        #         key == KeyCode.from_char('y') or \
        #         key == KeyCode.from_char('h') or \
        #         key == KeyCode.from_char('u') or \
        #         key == KeyCode.from_char('j'):
        #     # return str(key)[1:-1]
        #     pass
        # else:
        #     # return False
        #     pass

        match key:
            case KeyCode.from_char('a') | KeyCode.from_char('w') | KeyCode.from_char('s') | KeyCode.from_char('e') | \
                 KeyCode.from_char('d') | KeyCode.from_char('f') | KeyCode.from_char('t') | KeyCode.from_char('g') | \
                 KeyCode.from_char('y') | KeyCode.from_char('h') | KeyCode.from_char('u') | KeyCode.from_char('j'):
                return str(key)[1:-1]
            case _:
                return False

    def is_0to8_key(self, key):
        # if key == KeyCode.from_char('0') or \
        #         key == KeyCode.from_char('1') or \
        #         key == KeyCode.from_char('2') or \
        #         key == KeyCode.from_char('3') or \
        #         key == KeyCode.from_char('4') or \
        #         key == KeyCode.from_char('5') or \
        #         key == KeyCode.from_char('6') or \
        #         key == KeyCode.from_char('7') or \
        #         key == KeyCode.from_char('8'):
        #     return str(key)[1:-1]
        # else:
        #     return False

        match key:
            case KeyCode.from_char('0') | KeyCode.from_char('1') | KeyCode.from_char('2') | KeyCode.from_char('3') | \
                 KeyCode.from_char('4') | KeyCode.from_char('5') | KeyCode.from_char('6') | KeyCode.from_char('7') | \
                 KeyCode.from_char('8') | KeyCode.from_char('9'):
                return str(key)[1:-1]
            case _:
                return False

    def on_press(self, key):
        piano_key = is_piano_key(key)
        tone_h = is_0to8_key(key)

        if piano_key:
            exp_build = f'play_note(FREQ.{FREQ.key_coverity[piano_key]}{self.SOUND_H})'
            eval(exp_build)
        elif tone_h:
            self.SOUND_H = int(tone_h)
        else:
            if (key == Key.up or key == Key.right) and self.SOUND_H < 8:
                self.SOUND_H += 1
                octave_text.set(SOUND_H)
            elif (key == Key.down or key == Key.left) and self.SOUND_H > 0:
                self.SOUND_H -= 1
                octave_text.set(self.SOUND_H)

    def on_release(self, key):
        if key == Key.esc:
            return False
