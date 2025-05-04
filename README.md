# Emotion Detection App
A simple Flask web app that detects emotions in text using the **IBM Watson NLP Library**'s **Emotion Predict** function.

## 🚀 Features
- Detects emotions like joy, sadness, anger, fear, and disgust in text.
- Takes user input via a web form.
- Displays emotion scores.
- Uses IBM Watson NLP API for emotion prediction.

## 🗂️ Project Structure
emotion_detection/ # Python package
├── init.py
├── emotion_detection.py
├── set_up.py

static/ # Static files (sourced from IBM repo)
├── script.js

templates/ # HTML templates (sourced from IBM repo)
├── index.html

tests/ # HTML templates # Unit test
├── test_emotion_detection.py

server.py # Flask app server
requirements.txt
README.md
