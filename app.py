# Emotion Detection Web App using Flask and TensorFlow 
from flask import Flask, render_template, request, jsonify  #Flask for web app, render_template for HTML rendering, request gets data from frontend, jsonify for sending JSON responses
import tensorflow as tf
import numpy as np
import cv2 #OpenCV for image processing
from mtcnn import MTCNN #MTCNN for deep learning-based face detection
from PIL import Image
import base64
import io

app = Flask(__name__)

# Load emotion model
model = tf.keras.models.load_model("model/fer_emotion_model.h5")

# Emotion labels (FER2013)
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# Initialize face detector
detector = MTCNN()  #Multi-Task Cascaded Convolutional Networks

# Preprocess face image
def preprocess_face(face_img):
    face_img = cv2.resize(face_img, (48, 48))
    face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
    face_img = face_img / 255.0
    face_img = np.reshape(face_img, (1, 48, 48, 1))
    return face_img

@app.route('/')
def index():
    return render_template('index.html')

# Predict emotion from the uploaded image
# @app.route('/predict', methods=['POST'])
# def predict():

#     data = request.json['image']

#     image_data = base64.b64decode(data.split(',')[1])
#     image = Image.open(io.BytesIO(image_data)).convert("RGB")
#     frame = np.array(image)
    
#     # Detect faces in the image
#     faces = detector.detect_faces(frame)

#     if len(faces) == 0:
#         return jsonify({'emotion': 'No face detected'})
    
#     #Crop the first detected face
#     x, y, width, height = faces[0]['box']
#     face = frame[y:y+height, x:x+width]

#     processed_face = preprocess_face(face)

#     prediction = model.predict(processed_face)
#     emotion = emotion_labels[np.argmax(prediction)]
#     # confidence = float(np.max(prediction)) * 100

#     return jsonify({'emotion': emotion
#                     # 'confidence': round(confidence,2),
#                     })


@app.route('/predict', methods=['POST'])
def predict():

    try:
        data = request.json['image']

        # Remove header and decode
        image_data = base64.b64decode(data.split(',')[1])
        image = Image.open(io.BytesIO(image_data)).convert("RGB")
        frame = np.array(image)

        # Detect faces
        faces = detector.detect_faces(frame)

        if len(faces) == 0:
            return jsonify({'emotion': 'No face detected'})

        # Get first face
        x, y, width, height = faces[0]['box']

        # 🔥 Fix negative values (VERY IMPORTANT)
        x = max(0, x)
        y = max(0, y)

        face = frame[y:y+height, x:x+width]

        if face.size == 0:
            return jsonify({'emotion': 'Face crop error'})

        processed_face = preprocess_face(face)

        prediction = model.predict(processed_face)
        emotion = emotion_labels[np.argmax(prediction)]
        confidence = float(np.max(prediction)) * 100

        return jsonify({
            'emotion': emotion,
            'confidence': round(confidence, 2)
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({'emotion': 'Error processing image'})

if __name__ == "__main__":
    app.run(debug=True)