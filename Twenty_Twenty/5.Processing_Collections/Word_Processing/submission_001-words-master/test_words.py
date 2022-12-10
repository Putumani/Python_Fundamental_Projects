import unittest
import word_processor

class MyTestCase(unittest.TestCase):

    def test_convert_to_word_list(self):

        a = 'These are indeed interesting, an obvious understatement, times. What say you?'
        b = ['these', 'are', 'indeed', 'interesting', 'an', 'obvious', 'understatement',\
             'times', 'what', 'say', 'you']
        result = word_processor.convert_to_word_list(a)
        self.assertEqual(b, result)


    def test_words_longer_than(self):   

        a = 'These are indeed interesting, an obvious understatement, times. What say you?'
        b = ['interesting', 'understatement']
        result = word_processor.words_longer_than(10,a)
        self.assertEqual(b, result)



    def test_words_lengths_map(self):  

        a = 'These are indeed interesting, an obvious understatement, times. What say you?'
        b = {2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1}
        result = word_processor.words_lengths_map(a)
        self.assertEqual(b, result)


    def test_letters_count_map(self):  

        a = 'These are indeed interesting, an obvious understatement, times. What say you?'
        b = {'a': 5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0,\
             'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8,\
             'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0}
        result = word_processor.letters_count_map(a)
        self.assertEqual(b, result)
    
    def test_most_used_character(self):

        a = 'These are indeed interesting, an obvious understatement, times. What say you?'
        b = 'e'
        result = word_processor.most_used_character(a)
        self.assertEqual(b, result)

    def test_most_used_character_empty(self):
        a = ''
        b = None
        result = word_processor.most_used_character(a)
        self.assertEqual(b, result)
    
    def test_most_used_character_more_than_one_characters(self):
        a = 'These are indeed interesting, an obvious understatement, times. What say you? totaly to'
        b = 'e, t'
        result = word_processor.most_used_character(a)
        self.assertEqual(b, result)

        