class Solution:
    '''
        Input: numbers = [1,2,3,4], target = 3

        Output: [1,2]

        [1,2,3,4]
        t
        t - numbers[0] = 2 : 0
        ....
        t - numbsers[3] = -1: 3

        if t - numbers[0] in dict():
            return [i, dict[3 - numbers[0]]]
        
        No hashmap
         3-1=2
         x y
         compare x < y and numbers[x] + numbers[y] = target
             return [x+1,y+1]
         else:
            y += 1
        if y = len(numbers):
            update x
            x += 1
            y = 0
        while conditions will be if x < len(numbers)

        [1,2,3,4]



    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x=0
        y=1
        
        while(x < len(numbers)):
            if x < y and x != y and numbers[x] + numbers[y] == target:
                return [x+1,y+1]
            else:
                y += 1
            
            if y == len(numbers):
                x += 1
                y = 0
        
        return []

        