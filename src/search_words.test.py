import unittest
from search_words import TrieTree, construct_trie_tree, parse_input, select_valid_words


class TestWordsCombination(unittest.TestCase):
    def test_file_not_found_error(self):
        self.assertRaises(FileNotFoundError, construct_trie_tree, 'none_exist_file.txt')

    def test_trie_tree_is_constructed_successfully(self):
        trie = TrieTree()
        self.assertEqual(trie.search('apple'), False)
        trie.insert('apple')
        trie.insert('banana')
        self.assertEqual(trie.search('apple'), True)
        self.assertEqual(trie.search('banana'), True)
        self.assertEqual(trie.search('orange'), False)

    def test_parse_input_to_set(self):
        trie = TrieTree()
        trie.insert('app')
        trie.insert('ban')
        candidate_words = parse_input('appl', trie)
        expected = {
            'a', 'p', 'l',
            'ap', 'al', 'pa', 'pl', 'la', 'lp', 'pp',
            'apl', 'alp', 'pal', 'pla', 'lap', 'lpa',
            'app', 'pap', 'ppa', 'lpp', 'plp', 'ppl',

        }
        self.assertEqual(candidate_words, expected)

    def test_select_valid_words(self):
        trie = TrieTree()
        trie.insert('app')
        trie.insert('a')
        trie.insert('ban')
        candidate_words = parse_input('appl', trie)
        valid_words = select_valid_words(trie, candidate_words)
        self.assertEqual(valid_words, {'a', 'app'})


if __name__ == '__main__':
    unittest.main()
