#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Computing signal envelope by applying the Hilbert Transform

"""

# Importing packages and modules
import numpy as np
from scipy.signal import hilbert
from sources.config import Config

# Envelope analysis class
class EnvelopeAnalysis:

    # Constructor
    def __init__(self):

        # Configuration parameters
        config = Config()
        self.precision = config.precision
        self.eps = config.eps

    # Computing the envelopes
    def compute(self, signal: list):
        envelope = np.round(np.abs(hilbert(signal)), self.precision)
        return envelope