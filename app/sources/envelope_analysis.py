#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Computing signal envelopes by applying the Hilbert Transform

"""

# Importing packages and modules
import numpy as np
from scipy.signal import hilbert
from sources.utils import load_config

# Envelope analysis class
class EnvelopeAnalysis:

    # Constructor
    def __init__(self):

        # Configuration parameters
        config = load_config()
        self.precision = config["precision"]
        self.eps = config["eps"]

    # Computing the envelopes
    def compute(self, signals):
        envelopes = np.round(np.abs(hilbert(signals)), self.precision)
        return envelopes