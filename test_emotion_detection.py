import unittest
import json
from EmotionDetection import emotion_detection

class TestStringMethods(unittest.TestCase):

    def get_dominant_emotion(self, input):
        res = emotion_detection.emotion_detector(input)
        res = json.loads(res)
        return res["dominant_emotion"]
        
    def test1(self):

        tests = [ 
            {"input" : "I am glad this happened", "expected" : "joy"},
            {"input" : "I am really mad about this", "expected" : "anger"},
            {"input" : "I feel disgusted just hearing about this", "expected" : "disgust"},
            {"input" : "I am so sad about this", "expected" : "sadness"},
            {"input" : "I am really afraid that this will happen", "expected" : "fear"},
        ]

        for test in tests:
            emotion = self.get_dominant_emotion(test["input"])
            self.assertEqual(test["expected"], emotion)


if __name__ == '__main__':
    unittest.main()