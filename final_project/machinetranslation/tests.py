import unittest
from translator import translate_english_to_french, translate_french_to_english

class TranslationTests(unittest.TestCase):

    def test_english_to_french(self):
        # Test translation of 'Hello' to French
        result = translate_english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')

        # Test translation of 'How are you?' to French
        result = translate_english_to_french('How are you?')
        self.assertEqual(result, 'Comment ça va ?')

    def test_french_to_english(self):
        # Test translation of 'Bonjour' to English
        result = translate_french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')

        # Test translation of 'Comment ça va ?' to English
        result = translate_french_to_english('Comment ça va ?')
        self.assertEqual(result, 'How are you?')

if __name__ == '__main__':
    unittest.main()
