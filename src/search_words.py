import codecs
import itertools

full_words_file_dir = "../usr/share/dict/words.txt"


class TrieTree:
    def __init__(self):
        self.head = {}
        self.max_len = 0

    def insert(self, word):
        current = self.head
        for character in word:
            if character not in current:
                current[character] = {}
            current = current[character]
        current['*'] = True
        self.max_len = max(self.max_len, len(word))

    def search(self, word):
        if len(word) > self.max_len:
            return False
        current = self.head
        for character in word:
            if character not in current:
                return False
            current = current[character]
        if '*' in current:
            return True
        return False


def construct_trie_tree(filename):
    try:
        with codecs.open(filename, 'r', 'utf-8') as full_data:
            word = full_data.readline()
            trie_tree = TrieTree()
            print('initializing...')
            while word:
                word = word.replace('\n', '')
                trie_tree.insert(word.lower())
                word = full_data.readline()
        return trie_tree
    except FileNotFoundError:
        msg = "Sorry, the file " + full_words_file_dir + " does not exist."
        raise FileNotFoundError(msg)


def parse_input(inputs, trie):
    max_len = trie.max_len
    if inputs is '#':
        return '#'
    characters = []
    candidate_words = set()
    for char in inputs:
        if char.isalpha():
            characters.append(char)
    for length in range(min(len(characters), max_len)):
        combinations = itertools.permutations(characters, length + 1)
        for comb in combinations:
            word = ''.join(comb)
            if word not in candidate_words:
                candidate_words.add(word)
    return candidate_words


def get_input():
    user_input = input(
        "\nEnter characters (case-insensitive):"
        "\nExample1: a p p l e"
        "\nExample2: apple"
        "\n(type # to exit)\n"
    )
    return user_input


def select_valid_words(trie, words):
    valid_words = set()
    for word in words:
        if trie.search(word):
            valid_words.add(word)
    return valid_words


if __name__ == "__main__":
    trie = construct_trie_tree(full_words_file_dir)
    parsed_input = parse_input(get_input(), trie)
    while parsed_input is not '#':
        print('Valid words:')
        all_words = parsed_input
        valid_words = select_valid_words(trie, all_words)
        for valid_word in valid_words:
            print(valid_word)
        print('Total of', len(valid_words), 'valid word' + ('s' if len(valid_words) > 1 else ''))
        parsed_input = parse_input(get_input(), trie)

