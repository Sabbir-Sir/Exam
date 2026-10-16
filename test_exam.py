import exam
import unittest

class TestStringProcessor(unittest.TestCase):
    def test_reverse_1(self):
        self.assertEqual(exam.reverse_string("cat"), "tac")

    def test_reverse_2(self):
        self.assertEqual(exam.reverse_string("Python"), "nohtyP")

    def test_reverse_3(self):
        self.assertNotEqual(exam.reverse_string("hello"), "hello")

    def test_reverse_4(self):
        self.assertEqual(exam.reverse_string("123"), "321")

    def test_reverse_5(self):
        with self.assertRaises(TypeError):
            exam.reverse_string(None)

    def test_vowels_1(self):
        self.assertEqual(exam.count_vowels("apple"), 2)

    def test_vowels_2(self):
        self.assertEqual(exam.count_vowels("education"), 5)

    def test_vowels_3(self):
        self.assertNotEqual(exam.count_vowels("hello"), 5)

    def test_vowels_4(self):
        self.assertEqual(exam.count_vowels("AEIOU"), 5)

    def test_vowels_5(self):
        with self.assertRaises(AttributeError):
            exam.count_vowels(None)

    def test_words_1(self):
        self.assertEqual(exam.word_count("one two three"), 3)

    def test_words_2(self):
        self.assertEqual(exam.word_count("hello"), 1)

    def test_words_3(self):
        self.assertNotEqual(exam.word_count("hello world"), 5)

    def test_words_4(self):
        self.assertEqual(exam.word_count(""), 0)

    def test_words_5(self):
        with self.assertRaises(AttributeError):
            exam.word_count(None)

if __name__ == "__main__":
    unittest.main()
