import os
import subprocess
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set Notary trust server (default to your server)
NOTARY_SERVER = os.getenv("DOCKER_CONTENT_TRUST_SERVER", "https://notary.container.ucds.io")

def is_image_signed(image):
    """Check if the image is signed using `docker trust inspect` and `jq`."""
    try:
        # Run `docker trust inspect` and parse output with `jq`
        result = subprocess.run(
            ["docker", "trust", "inspect", image, "--format", "{{json .}}"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
            env={**os.environ, "DOCKER_CONTENT_TRUST_SERVER": NOTARY_SERVER}
        )
        
        if result.returncode != 0:
            print(f"Error running docker trust inspect: {result.stderr}")
            return False
        
        # Parse JSON output
        trust_data = json.loads(result.stdout)
        
        # Extract SignedTags array length
        signed_tags_length = len(trust_data[0].get("SignedTags", []))
        
        return signed_tags_length > 0
    except Exception as e:
        print(f"Error checking image signature: {e}")
        return False

@app.route("/", methods=["POST"])
def validate():
    request_data = request.json

    # Extract images from the admission request
    images = [container["image"] for container in request_data["request"]["object"]["spec"]["containers"]]

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
    app.run(host="0.0.0.0", port=8080)  # HTTP only
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set Notary trust server (default to your server)
NOTARY_SERVER = os.getenv("DOCKER_CONTENT_TRUST_SERVER", "https://notary.container.ucds.io")

def is_image_signed(image):
    """Check if the image is signed using `docker trust inspect`."""
    try:
        # Run `docker trust inspect` with Notary server environment variable
        result = subprocess.run(
            ["docker", "trust", "inspect", image],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
            env={**os.environ, "DOCKER_CONTENT_TRUST_SERVER": NOTARY_SERVER}
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
    images = [container["image"] for container in request_data["request"]["object"]["spec"]["containers"]]

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
    app.run(host="0.0.0.0", port=8080)  # HTTP only
