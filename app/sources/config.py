#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Configuration parameters

"""

# Importing packages
import yaml

# Configuration parameter class
class Config:

    # Constructor
    def __init__(self):
        with open("./app/sources/config.yaml", "r") as file:
            config = yaml.safe_load(file)
        self.min_frequency = float(config["min_frequency"])
        self.precision = int(config["precision"])
        self.eps = float(config["eps"])