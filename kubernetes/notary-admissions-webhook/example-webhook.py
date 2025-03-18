
from flask import Flask, request, jsonify
from kubernetes.client import V1AdmissionReview, V1AdmissionResponse, V1ObjectMeta
from kubernetes.client.rest import ApiException

app = Flask(__name__)

@app.route("/validate", methods=["POST"])
def validate():
    # Get the AdmissionReview object
    admission_review = request.get_json()

    # Create a response object
    response = V1AdmissionResponse()

    # Check if the admission review contains the required label
    try:
        # Extracting the pod metadata
        object_metadata = admission_review["request"]["object"]["metadata"]
        labels = object_metadata.get("labels", {})

        # You can customize the label check as needed
        if "example-label" not in labels:
            response.allowed = False
            response.result = {"message": "Missing 'example-label' in labels"}
        else:
            response.allowed = True
    except KeyError as e:
        response.allowed = False
        response.result = {"message": f"Error processing request: {str(e)}"}

    # Return the response in AdmissionReview format
    admission_response = V1AdmissionReview(
        response=response
    )
    
    return jsonify(admission_response.to_dict())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, ssl_context=("certs/tls.crt", "certs/tls.key"))
