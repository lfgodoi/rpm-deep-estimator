## RPM Deep Estimator (rpm-deep-estimator)

A deep learning-based RPM estimator based on spectral features extracted from vibration signals of rotating machines.

- Developer: _Leonardo Franco de Godói_
- GitHub profile: _https://github.com/lfgodoi_
- Contact: _eng.leonardogodoi@gmail.com_

### Running the app directly

It is usually common to need to run the app directly using Python for development and testing purposes, without the need to use Docker, which will only be required for its automatic deployment.

_Inside the project folder, create a virtual environment._

    python3 -m venv .venv

_Activate the virtual environment._

    source .venv/bin/activate

_Update the Pip._

    pip install --upgrade pip

_Install the app dependencies._

    pip install -r requirements.txt

_Run the app._

    python app/main.py
