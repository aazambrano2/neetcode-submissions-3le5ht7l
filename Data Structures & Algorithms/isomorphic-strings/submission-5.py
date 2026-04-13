class Solution:
    from collections import Counter
    def isIsomorphic(self, s: str, t: str) -> bool:
        # first = Counter(s)
        # second = Counter(t)
        # return sorted(first.values()) == sorted(second.values()) and len(first) == len(second)
        def encode(string):
            mapping = {}
            result = []
            i = 0
            for char in string:
                if char not in mapping:
                    mapping[char] = i
                    i += 1
                result.append(mapping[char])
            return result

        return encode(s) == encode(t)
        