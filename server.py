"""Web app with endpoint for assessing emotional features of input string."""
import ast

from flask import Flask, request, make_response
from EmotionDetection import emotion_detection

app = Flask("__name__")

@app.route('/emotionDetector')
# ‘/’ URL is bound with hello_world() function.
def emotion_detector():
    """Handler for emotion detector, reads textToAnalyze param 
    and passes to emotion detection function."""
    template = "For the given statement, the system response is "
    template += "'anger': {}, "
    template += "'disgust': {}, "
    template += "'fear': {}, "
    template += "'joy': {} and "
    template += "'sadness': {}. "
    template += "The dominant emotion is {}."

    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        res = make_response(template.format(None, None, None, None, None, None))
        res.status_code = 400
        return res

    emotions = emotion_detection.emotion_detector(text_to_analyze)
    emotions = ast.literal_eval(emotions)

    if emotions['dominant_emotion'] is None:
        return make_response("Invalid text! Please try again!")

    res = make_response(
        template.format(emotions['anger'],
            emotions['disgust'],
            emotions['fear'],
            emotions['joy'],
            emotions['sadness'],
            emotions['dominant_emotion'])
        )

    return res


if __name__ == '__main__':
    app.run(port="5000")
