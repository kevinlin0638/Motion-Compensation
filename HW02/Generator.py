# -*-coding:utf-8-*-
import numpy as np
import scipy.io.wavfile as wwf


class SoundGenerator:
    def __init__(self, sample_rate, amplitude):
        self.sample_rate = sample_rate
        self.amplitude = amplitude
        self.spectrum = []
        self.hzArr = [
            ['X', 1],
            ['C', 262],
            ['D', 294],
            ['E', 330],
            ['F', 349],
            ['G', 392],
            ['A', 440],
            ['B', 494]
        ]

        self.lowhzArr = [
            ['X', 1],
            ['C', 65],
            ['D', 76],
            ['E', 82],
            ['F', 87],
            ['G', 98],
            ['A', 110],
            ['B', 124]
        ]

    def print_properties(self):
        print(self.sample_rate, self.amplitude)

    def generate_wave(self, chord, sec):
        wave_data = self.amplitude * np.sin(2 * np.pi * self.hzArr[chord][1] / self.sample_rate * np.arange(sec * 0.5 * self.sample_rate)).astype(np.float32)
        return wave_data

    def lowgenerate_wave(self, chord, sec):
        wave_data = 8 * np.sin(2 * np.pi * self.lowhzArr[chord][1] / self.sample_rate * np.arange(sec * 0.5 * self.sample_rate)).astype(np.float32)
        return wave_data

    def save_wave(self, wave_data, mode):
        # 寫入 Wave 檔案
        if mode == 0:
            wwf.write('HomeWorkP1.wav', self.sample_rate, wave_data)
        elif mode == 1:
                wwf.write('HomeWorkP2.wav', self.sample_rate, wave_data)

    def save_w(self, wave_data, name):
        # 寫入 Wave 檔案
        wwf.write(name+'.wav', self.sample_rate, wave_data)

    def kappa(self, chord, sec, low):
        if low is True:
            am = 3
        else:
            am = 10
        wave_data = []
        wave_data = np.array(wave_data)
        for i in np.arange(sec * 0.5 * self.sample_rate):
            hz = self.lowhzArr[chord][1] * np.cos(2 * np.pi * (100 + 400 * i) * i)
            wave_data = np.hstack([wave_data, am * np.sin(2 * np.pi * hz / self.sample_rate * i).astype(np.float32)])
        return wave_data



