import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def validate_request(admission_review):
    """ Validates the incoming Kubernetes AdmissionReview request. """
    try:
        req = admission_review["request"]
        object_metadata = req["object"]["metadata"]
        labels = object_metadata.get("labels", {})

        if "example-label" not in labels:
            allowed = False
            message = "Missing required label: 'example-label'"
        else:
            allowed = True
            message = "Validation successful"

    except KeyError as e:
        allowed = False
        message = f"Error processing request: {str(e)}"

    return {
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
            "uid": admission_review["request"]["uid"],
            "allowed": allowed,
            "status": {
                "message": message
            }
        }
    }

@app.route("/validate", methods=["POST"])
def validate():
    admission_review = request.get_json()
    return jsonify(validate_request(admission_review))

if __name__ == "__main__":
    is_local = os.getenv("LOCAL_MODE", "false").lower() == "true"

    if is_local:
        print("Running in LOCAL mode (HTTP)")
        app.run(host="0.0.0.0", port=5000, debug=True)
    else:
        print("Running in PRODUCTION mode (HTTPS)")
        app.run(host="0.0.0.0", port=443, ssl_context=("certs/tls.crt", "certs/tls.key"))
