#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Computing signal spectra by applying the Fast Fourier Transform (FFT)

"""

# Importing packages and modules
import numpy as np
from utils import load_config

# FFT class
class FFT:

    # Constructor
    def __init__(self, sampling_frequency: float):

        # Instance's parameters
        self.sampling_frequency = sampling_frequency

        # Configuration parameters
        config = load_config()
        self.min_frequency = config["min_frequency"]
        self.precision = config["precision"]
        self.eps = config["eps"]

    #  Computing the FFT
    def compute(self, signals: np.ndarray):
        frequencies = np.fft.fftfreq(signals.shape[1], 1/self.sampling_frequency)
        frequencies = frequencies[:int(frequencies.shape[0]/2)]
        amplitudes = np.abs(np.fft.fft(signals)*(2/signals.shape[1]))
        amplitudes = amplitudes[:, :int(amplitudes.shape[1]/2)]
        min_index = np.where(frequencies > self.min_frequency)[0][0]
        amplitudes[:, :min_index] = self.eps
        amplitudes = np.round(amplitudes, self.precision)
        frequencies = np.round(frequencies, self.precision)
        return amplitudes, frequencies