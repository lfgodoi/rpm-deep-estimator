#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Main script

"""

# Importing packages and modules
from flask import Flask

# Setting the app up
app = Flask(__name__)
app.config["SECRET_KEY"] = "RpMDEEpeStimATor"

# Running the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5016, debug=False)
