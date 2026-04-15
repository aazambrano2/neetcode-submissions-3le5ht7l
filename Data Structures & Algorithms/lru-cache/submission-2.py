class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity  # Store the max number of items the cache can hold
        self.cache = []           # Initialize empty list to store [key, value] pairs

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):        # Loop through all items in the cache
            if self.cache[i][0] == key:         # Check if current item's key matches
                tmp = self.cache.pop(i)         # Remove item from its current position
                self.cache.append(tmp)          # Re-append to end (mark as recently used)
                return tmp[1]                   # Return the value of the found key
        return -1                               # Key not found, return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):        # Loop through all items to check for duplicates
            if self.cache[i][0] == key:         # Check if key already exists in cache
                tmp = self.cache.pop(i)         # Remove the existing entry
                tmp[1] = value                  # Update the value
                self.cache.append(tmp)          # Re-append to end (mark as recently used)
                return                          # Exit early, no need to check capacity
        if self.capacity == len(self.cache):    # Cache is full, need to evict
            self.cache.pop(0)                   # Remove least recently used (first element)
        self.cache.append([key, value])         # Insert new [key, value] pair at the end