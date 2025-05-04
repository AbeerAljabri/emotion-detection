"""Flask web server for Emotion Detection Application."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Correct folder structure for templates and static
app = Flask(__name__)
            #template_folder='oaqjp-final-project-emb-ai/templates',  # Pointing to templates folder
           # static_folder='oaqjp-final-project-emb-ai/static')      # Pointing to static folder

# Route for emotion detection, which serves index.html and handles AJAX request
@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():
    """
    Handle emotion detection requests.
    
    Accepts a text input via GET, calls the emotion_detector function,
    and returns formatted response with emotion scores and dominant emotion.
    If input is invalid, returns an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')  # Get text from GET request

    # Process the text to detect emotion
    result = emotion_detector(text_to_analyze)

    anger = result.get('anger')
    disgust = result.get('disgust')
    fear = result.get('fear')
    joy = result.get('joy')
    sadness = result.get('sadness')
    dominant_emotion = result.get('dominant_emotion')

        # Error case: if dominant_emotion is None ➔ invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Prepare the response to return to JavaScript
    response = (f"For the given statement, the system response is"
                f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear},"
                f"'joy': {joy} and 'sadness': {sadness}."
                f"The dominant emotion is {dominant_emotion}.")
    return response

# Serve the index.html page when a user visits the site
@app.route("/")
def home():
    """
    Serve the index.html page when user visits the root URL.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
  