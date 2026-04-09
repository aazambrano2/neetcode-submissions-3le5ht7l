class Solution:

    '''

    Input: strs = ["act","pots","tops","cat","stop","hat"]

    Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

    we can use a hash table to hash same pattern of items

    use a set to have these "set" of char"

    ["act","pots","tops","cat","stop","hat"]

    act : cat
    hat : 
    stop : tops pots

    key will be part of that sub litst

    1nd use ord() to get a hash of a word
    2rd create a hashtable of lists to contain all records of same pattern characters

    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0: return [[""]]

        patterns = defaultdict(list)

        for s in strs:
            count = [0] * 26
            #for every character in string
            for c in s:
                #bit map your string pattern
                count[ord(c) - ord('a')] += 1
            #append list pattern matches to string based on key
            # your key is that pattern
            patterns[tuple(count)].append(s)
        #returns a list of lists
        return patterns.values()
        


        