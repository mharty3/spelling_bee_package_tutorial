import unittest

from word_finder import check_word, word_finder, find_pangrams

class TestCheckWord(unittest.TestCase):

    def test_check_word(self):
        self.assertTrue(check_word('pill', 'liupyubc')) # test a good word
        self.assertTrue(check_word('publicly', 'liuypubc')) # test pangram

        # test failing cases
        self.assertFalse(check_word('ill', 'liupuybc')) # too short
        self.assertFalse(check_word('cubby', 'liupuybc')) # no "key" letter
        self.assertFalse(check_word('prior', 'liupuybc')) # contains bad letters


class TestWordFinder(unittest.TestCase):

    def test_key_letter_in_all_words(self):
        good_words_to_test = word_finder('liupybc')
        
        results = ['l' in w for w in good_words_to_test]
        self.assertTrue(all(results))


    def test_all_words_have_four_or_more_letters(self):
        good_words_to_test = word_finder('liupycb')
        
        results = [len(w) >= 4 for w in good_words_to_test]
        self.assertTrue(all(results))


    def test_only_good_letters_in_words(self):
        good_letters = 'liupycb'
        good_words_to_test = word_finder(good_letters)
        
        results = [set(w).issubset(good_letters) for w in good_words_to_test]
        self.assertTrue(all(results))

class TestPangram(unittest.TestCase):

    def test_pangram(self):
        word_list = ['pill', 'clubby', 'cyclicly', 'publicly']
        self.assertEqual(find_pangrams(word_list), ['publicly'])

        word_list.append('upblicly') # add another "pangram"
        self.assertEqual(len(find_pangrams(word_list)), 2) # Find multiple pangrams

        word_list = word_list[:3]
        self.assertEqual(find_pangrams(word_list), []) # no pangrams

if __name__ == "__main__":
    unittest.main()
