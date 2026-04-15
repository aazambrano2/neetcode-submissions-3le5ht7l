class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Input: strs = ["act","pots","tops","cat","stop","hat"]

        Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        act -> act cat, act
        pots ->pots tops stop pots
        hat -> hat

        you could sort them or place in a set?

        act
        aht
        pots

        '''
    

        anagram = {}
        for s in range(len(strs)):
            key = ''.join(sorted(strs[s]))
            if key not in anagram:
                anagram[key]=[strs[s]]
            else:
                anagram[key].append(strs[s])
        
        return [x for x in anagram.values()]