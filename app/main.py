#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Main script

"""

# Importing packages and modules
from flask import Flask

# Setting the app
app = Flask(__name__)
app.config["VERSION"] = "1.0.0"

# Running the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5016, debug=False)
