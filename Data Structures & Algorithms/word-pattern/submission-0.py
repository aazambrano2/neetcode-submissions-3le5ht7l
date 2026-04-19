class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        '''
        "abba", s = "dog cat cat dog"

        iterate

        a -> dog
        if match -> goes to a
        if new key -> b - cat
        '''
        # split string s into a list of words
        words = s.split()

        # maps each pattern char to an index e.g {'a': 1, 'b': 2}
        charToWord = {}
        # maps each word to an index e.g {'dog': 1, 'cat': 2}
        wordToChar = {}

        # early return if lengths don't match — can't have a valid pattern
        if len(pattern) != len(words):
            return False

        # zip pairs each char in pattern with its corresponding word
        # enumerate gives us the index i
        # e.g pattern="abba", words=["dog","cat","cat","dog"]
        # iteration 1: i=0, c='a', word='dog'
        # iteration 2: i=1, c='b', word='cat'
        for i, (c, word) in enumerate(zip(pattern, words)):

            # check if char and word were previously mapped to the same index
            # .get(key, 0) returns 0 if key not found — default for unseen chars/words
            # if they don't match, the mapping is inconsistent
            # e.g c='a' was mapped to index 1 but word='cat' was mapped to index 2
            if charToWord.get(c, 0) != wordToChar.get(word, 0):
                return False

            # store i+1 as the index (1-based so it never conflicts with default 0)
            charToWord[c] = i + 1       # e.g charToWord['a'] = 1
            wordToChar[word] = i + 1    # e.g wordToChar['dog'] = 1

        return True
        