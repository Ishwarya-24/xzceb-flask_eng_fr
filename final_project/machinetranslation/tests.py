import unittest
from machinetranslation.translator import englishToFrench, frenchToEnglish

class TranslationTests(unittest.TestCase):
    def test_english_to_french_hello(self):
        english_text = 'Hello'
        translated_text = englishToFrench(english_text)
        expected_text = 'Bonjour'
        self.assertEqual(translated_text, expected_text)

    def test_english_to_french_bonjour(self):
        english_text = 'Bonjour'
        translated_text = englishToFrench(english_text)
        expected_text = 'Bonjour'
        self.assertEqual(translated_text, expected_text)

    def test_french_to_english_bonjour(self):
        french_text = 'Bonjour'
        translated_text = frenchToEnglish(french_text)
        expected_text = 'Hello'
        self.assertEqual(translated_text, expected_text)

    def test_french_to_english_hello(self):
        french_text = 'Hello'
        translated_text = frenchToEnglish(french_text)
        expected_text = 'Hello'
        self.assertEqual(translated_text, expected_text)

if __name__ == '__main__':
    unittest.main()
