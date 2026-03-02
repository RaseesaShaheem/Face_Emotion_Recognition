# 😊 Face Emotion Recognition System

# 📌 Project Overview

Human emotions play a vital role in communication, behavior analysis, and decision-making. Detecting emotions automatically from facial expressions is a challenging task due to variations in lighting, facial orientation, and individual differences.

This project focuses on building a Face Emotion Recognition (FER) system that predicts human emotions from facial images using Deep Learning. The system uses MTCNN for face detection and a Convolutional Neural Network (CNN) for emotion classification. The application is deployed using Flask, allowing users to perform real-time webcam detection or upload images for emotion prediction.

---

# 🎯 Objective

The main objective of this project is to develop an accurate and efficient deep learning model that:

- Detects faces using MTCNN
- Classifies emotions using CNN
- Provides real-time prediction
- Supports both webcam and image upload

---

## 🧠 Emotions Detected

- 😄 Happy
- 😢 Sad
- 😠 Angry
- 😲 Surprise
- 😐 Neutral
- 😨 Fear
- 🤢 Disgust

---

## 🚀 Features

- Real-time emotion detection using webcam  
- Upload image and predict emotion  
- Accurate face detection using MTCNN  
- Face detection using OpenCV
- CNN-based emotion classification 
- Preprocessing with grayscale normalization
- Clean and modular code structure
- Clean and user-friendly web interface  

---

## 🛠 Technologies Used

Programming:

Python

Deep Learning:

TensorFlow

Keras

ML / Data Processing:

NumPy

Pandas

Scikit-learn

Computer Version:

OpenCV

MTCNN

Web Framework:

Flask

Frontend:

HTML

JavaScript

CSS

Deployment Model:

Trained CNN model (.h5 file)

---

## 🏗 System Architecture

User (Web Interface)

        ↓

Flask Backend (app.py)

        ↓

MTCNN Face Detection

        ↓

Preprocessing (Grayscale + Resize 48x48)

        ↓

CNN Model Prediction

        ↓
        
Display Emotion

---

## 📂 Project Structure

Face-Emotion-Recognition/

│

├── model/

│ └── fer_emotion_model.h5

│

├── static/

│ ├── css/

│ └── styles.css

│ ├── js/

│ └── Script.js

│ ├── outputImage/

│ └── project Out.png

│

├── templates/

│ ├── index.html

│

├── app.py

├── Model.ipynb

├── requirements.txt

└── README.md

---

# 📊 Dataset Description

- Source:

The dataset is obtained from:
UCI Machine Learning Repository – FER-2013 Dataset

- Dataset Details:

Grayscale facial images

Image size: 48x48 pixels

Total Classes: 7 emotions

-  Target Variable:

Emotion – Multi-class classification problem predicting one of the seven emotion categories.

---

# ⚙️ Quick Start

🔹 Frontend

- Develop HTML page for webcam and image upload

- Display predicted emotion and confidence score

🔹 Backend

Import Required Libraries

- NumPy

- Pandas

- TensorFlow / Keras

- OpenCV

- MTCNN

- Flask

🔹 Model Training

Load Dataset

- Import FER-2013 dataset (CSV format)

Data Preprocessing

- Convert pixel strings into images

- Normalize pixel values (0–255 → 0–1)

- Reshape into (48, 48, 1)

🔹 CNN Architecture

- Convolution Layer + ReLU

- MaxPooling

- Dropout

- Fully Connected Layer

- Softmax Output Layer (7 Classes)

🔹 Model Evaluation

Evaluate using:

- Training Accuracy 

- Validation Accuracy

Identify:

Best-performing model configuration

🔹 Save Model

Save trained model:

emotion_model.h5

---

# 🚀 Deployment (Flask Web App)

1️⃣ Load trained CNN model

2️⃣ Initialize MTCNN detector

3️⃣ Detect face

4️⃣ Preprocess face (grayscale + resize)

5️⃣ Predict emotion

6️⃣ Display result on webpage

---

# 📷 Output

- Home Page

Upload image

Start webcam option

- Prediction Output

Detected face

Predicted emotion

- Output Screenshot

![Output](static/outputImage/project%20out.png)

---

# 📌 Future Enhancements

Improve accuracy using Transfer Learning (MobileNetV2)

Add emotion history tracking

Multi-face emotion analytics

# 🏆 Conclusion

This project successfully demonstrates the implementation of Deep Learning for emotion recognition. By combining MTCNN for face detection and CNN for classification, the system achieves reliable emotion prediction and real-time deployment using Flask.

---

# 👩‍💻 Author

Raseesa Shaheem