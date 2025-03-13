
from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

def is_image_signed(image):
    """Check if the image is signed using `docker trust inspect`."""
    try:
        result = subprocess.run(
            ["docker", "trust", "inspect", image],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        output = result.stdout.strip()

        # If output contains signers, it is signed
        if "Signers" in output and "No signatures or cannot access trust data" not in output:
            return True
        return False
    except Exception as e:
        print(f"Error checking image signature: {e}")
        return False

@app.route("/", methods=["POST"])
def validate():
    request_data = request.json

    # Extract images from the admission request
    images = []
    for container in request_data["request"]["object"]["spec"]["containers"]:
        images.append(container["image"])

    unsigned_images = [img for img in images if not is_image_signed(img)]

    if unsigned_images:
        return jsonify({
            "response": {
                "allowed": False,
                "status": {
                    "message": f"Blocked: Unsigned images detected: {unsigned_images}"
                }
            }
        })

    return jsonify({
        "response": {
            "allowed": True
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8443)  # No TLS, Linkerd handles it
