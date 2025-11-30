import unittest
import json
from EmotionDetection import emotion_detection

class TestStringMethods(unittest.TestCase):

    def get_dominant_emotion():
        
    def test1(self):
        res = emotion_detection.emotion_detector("I am glad this happened")
        res = json.loads(res)

        self.assertEqual(res["dominant_emotion"], "joy")


if __name__ == '__main__':
    unittest.main()