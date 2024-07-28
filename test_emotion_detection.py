'''Tests the emotion_detector function'''

from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    
    def test_emotion_detector(self):
        test_cases = {
            'I am glad this happened': 'joy',
            'I am really mad about this': 'anger',
            'I feel disgusted just hearing about this': 'disgust',
            'I am so sad about this': 'sadness',
            'I am really afraid that this will happen': 'fear'
        }

        for statement, emotion in test_cases.items():
            result = emotion_detector(statement)
            self.assertEqual(result['dominant_emotion'], emotion)

unittest.main()