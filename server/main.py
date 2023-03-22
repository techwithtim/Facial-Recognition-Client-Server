from flask import Flask, request, jsonify, send_file
from face_rec import classify_faces
import cv2
import base64
from PIL import Image
import numpy as np 
import os, io, sys

app = Flask(__name__)


@app.route('/classify-faces', methods=["POST"])
def classify():
    if not request.files.get("image"):
        return jsonify({error: "please pass a valid image"}), 400

    file = request.files['image'].read() ## byte file
    npimg = np.fromstring(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    new_img = classify_faces(img)
    img = Image.fromarray(new_img.astype("uint8"))
    rawBytes = io.BytesIO()
    img.save(rawBytes, "JPEG")
    rawBytes.seek(0)
    img_base64 = base64.b64encode(rawBytes.read())

    return jsonify({"image": str(img_base64)})


if __name__ == "__main__":
    app.run(debug=True)