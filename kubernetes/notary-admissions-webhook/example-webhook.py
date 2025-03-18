from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/validate", methods=["POST"])
def validate():
    admission_review = request.get_json()

    # Extract relevant details from the request
    try:
        req = admission_review["request"]
        object_metadata = req["object"]["metadata"]
        labels = object_metadata.get("labels", {})

        # Check if the required label exists
        if "example-label" not in labels:
            allowed = False
            message = "Missing required label: 'example-label'"
        else:
            allowed = True
            message = "Validation successful"

    except KeyError as e:
        allowed = False
        message = f"Error processing request: {str(e)}"

    # Construct the AdmissionReview response
    admission_response = {
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

    return jsonify(admission_response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, ssl_context=("certs/tls.crt", "certs/tls.key"))
