"""

Estimator routes

"""

# Importing packages and modules
from flask import Blueprint, request, jsonify
import json
from sources.fft import FFT
from sources.envelope_analysis import EnvelopeAnalysis
from sources.feature_extractor import FeatureExtractor
from sources.estimator import Estimator

# Setting the blueprint
estimation_blueprint = Blueprint("estimation_routes", __name__)

# Estimation route
@estimation_blueprint.route("/estimation/estimate", methods=["POST",])
def estimate():

    # Trying to estimate RPM...
    try:

        # Extracting the payload
        data = json.loads(request.data)
        signal = data["signal"]
        sampling_frequency = data["sampling_frequency"]

        # Computing the signal envelope
        envelope_analysis = EnvelopeAnalysis()
        envelope = envelope_analysis.compute(signal)

        # Computing the spectrum of both the original signal and the envelope
        fft = FFT()
        original_amplitudes, original_frequencies = fft.compute(signal, sampling_frequency)
        envelope_amplitudes, envelope_frequencies = fft.compute(envelope, sampling_frequency)

        # Adopting the amplitudes of relevant frequency bands as features
        feature_extractor = FeatureExtractor()
        original_features = feature_extractor.extract(original_amplitudes, original_frequencies)
        envelope_features = feature_extractor.extract(envelope_amplitudes, envelope_frequencies)

        # Processing the features through the deep learning model
        estimator = Estimator()
        estimated_rpm = estimator.estimate(original_features, envelope_features)

        # Setting up the results
        results = {
            "estimation_success": True,
            "estimated_rpm": estimated_rpm,
            "confidence_margin": feature_extractor.confidence_margin
        }
        status_code = 200

    # If it was not possible to estimate...
    except Exception as ex:

        # Logging the exception
        print(ex)

        # Setting up the results
        results = {
            "estimation_success": False,
            "estimated_rpm": None,
            "confidence_margin": None
        }
        status_code = 500

    return jsonify(results), status_code