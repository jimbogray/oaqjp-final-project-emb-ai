import ast

from flask import Flask, request, make_response
from EmotionDetection import emotion_detection

app = Flask("__name__")

@app.route('/emotionDetector')
# ‘/’ URL is bound with hello_world() function.
def emotion_detector():
    template = "For the given statement, the system response is "
    template += "'anger': {0}, "
    template += "'disgust': {1}, "
    template += "'fear': {2}, "
    template += "'joy': {3} and "
    template += "'sadness': {4}. "
    template += "The dominant emotion is {5}."

    textToAnalyze = request.args.get('textToAnalyze')

    if not textToAnalyze:
        res = make_response(template.format(None, None, None, None, None, None))
        res.status_code = 400
        return res

    emotions = emotion_detection.emotion_detector(textToAnalyze)
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