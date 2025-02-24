#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Utility functions

"""

# Importing packages
import yaml

# Reading the configuration parameters
def load_config():
    with open("./config.yaml", "r") as file:
        config = yaml.safe_load(file)
    config["min_frequency"] = float(config["min_frequency"])
    config["precision"] = int(config["precision"])
    config["eps"] = float(config["eps"])
    return config