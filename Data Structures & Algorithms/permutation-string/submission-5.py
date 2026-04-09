from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        
        if len1 > len2:
            return False
        
        # Create a frequency map for s1
        s1_count = Counter(s1)
        
        # Create a frequency map for the first window in s2
        window_count = Counter(s2[:len1])
        
        # Check the first window
        if s1_count == window_count:
            return True
        
        # Sliding window approach
        for i in range(len1, len2):
            # Include a new character in the window
            window_count[s2[i]] += 1
            
            # Remove the character that is no longer in the window
            window_count[s2[i - len1]] -= 1
            if window_count[s2[i - len1]] == 0:
                del window_count[s2[i - len1]]
            
            # Compare window with s1's frequency map
            if s1_count == window_count:
                return True
        
        return False
