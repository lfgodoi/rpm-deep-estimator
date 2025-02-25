"""

RPM Estimator routes

"""

# Importing packages and modules
from flask import Blueprint, request, jsonify
import json
from sources.fft import FFT
from sources.envelope_analysis import EnvelopeAnalysis

# Setting the blueprint
rpm_estimator_blueprint = Blueprint("rpm_estimator_routes", __name__)

# RPM Estimation route
@rpm_estimator_blueprint.route("/rpm-estimator/estimate", methods=["POST",])
def estimate():

    # Trying to estimate RPM...
    try:
        data = json.loads(request.data)
        signals = data["signals"]
        sampling_frequencies = data["sampling_frequencies"]
        results = {
            "estimation_success": True,
            "estimated_rpm": None,
            "confidence_margin": None
        }
        status_code = 200

    # If it was not possible to estimate...
    except:
        results = {
            "estimation_success": False,
            "estimated_rpm": None,
            "confidence_margin": None
        }
        status_code = 500

    return jsonify(results), status_code