class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Input: strs = ["act","pots","tops","cat","stop","hat"]
        Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        set -> key?

        so if you have a set, you can use that to id anagrams that belong to a sublist

        ["act","pots","tops","cat","stop","hat"]

        set('t''a''c') -> [act] -> add to list of lists

        first construct your set keys with empty list values

        then search and apply

        then return list of lists
        '''
        organizer = dict()
        for s in strs:
            key = "".join(sorted(s))
            if key not in organizer:
                organizer[key] = []
            organizer[key].append(s)
        
        return list(organizer.values())