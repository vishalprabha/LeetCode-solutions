'''
Source: https://leetcode.com/problems/implement-trie-prefix-tree/
Author: Vishal Prabhachandar
Date: 2021-June-10

Time complexity: O(m) m - average length of the words
Space complexity: O(n)  
'''


from collections import defaultdict

class Trie:
    
    def __init__(self):

        # simpler to create new nodes
        self.children = defaultdict(Trie)
        # used to denote end of the trie
        self.is_word = False

    def insert(self, word):
        '''
        insert a word in trie

        :param  word: string
        '''
        current = self
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        '''
        return if word is present in trie

        :param  word: string
        :return boolean
        '''
        current = self
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        '''
        return if word with the given prefix is present in trie

        :param  prefix: string
        :return boolean
        '''
        current = self
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True
