#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Extracting features from original signal and envelope spectra to be processed by the deep learning model

"""

# Importing packages and modules
from sources.config import Config

# Feature Extractor class
class FeatureExtractor:

    # Constructor
    def __init__(self):

        # Configuration parameters
        config = Config()
        self.eps = config.eps

        # Instance parameters
        self.confidence_margin = config.eps

    # Updating the confidence margin according to the current feature extraction
    def update_confidence_margin(self, frequencies):
        resolution = frequencies[1] - frequencies[0]
        if resolution > self.confidence_margin/60:
            self.confidence_margin = resolution*60

    #  Computing the FFT
    def extract(self, amplitudes: list, frequencies: list):
        features = []
        self.update_confidence_margin(frequencies)
        return features