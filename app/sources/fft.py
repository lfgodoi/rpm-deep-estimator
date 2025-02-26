#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Computing signal spectrum by applying the Fast Fourier Transform (FFT)

"""

# Importing packages and modules
import numpy as np
from sources.config import Config

# FFT class
class FFT:

    # Constructor
    def __init__(self):

        # Configuration parameters
        config = Config()
        self.min_frequency = config.min_frequency
        self.precision = config.precision
        self.eps = config.eps

    #  Computing the FFT
    def compute(self, signal: list, sampling_frequency: float):
        frequencies = np.fft.fftfreq(len(signal), 1/sampling_frequency)
        frequencies = frequencies[:int(frequencies.shape[0]/2)]
        amplitudes = np.abs(np.fft.fft(signal)*(2/len(signal)))
        amplitudes = amplitudes[:int(amplitudes.shape[0]/2)]
        amplitudes = np.round(amplitudes, self.precision)
        frequencies = np.round(frequencies, self.precision)
        return amplitudes, frequencies