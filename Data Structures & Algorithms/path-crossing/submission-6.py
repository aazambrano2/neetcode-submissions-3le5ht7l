class Solution:
    def isPathCrossing(self, path: str) -> bool:
        '''
        nesww
        (1,0)
        (1,1)
        (1,0)
        (0,0)
        (-1,0)
        keep track of visited coordiantes
        '''
        gps = (0,0)
        visited = set()
        for direction in path:
            if gps not in visited:
                print(gps)
                visited.add(gps)
                lst = list(gps)
                if direction == 'N':
                    lst[0] += 1
                if direction == 'S':
                    lst[0] -= 1
                if direction == 'E':
                    lst[1] += 1
                if direction == 'W':
                    lst[1] -= 1
                gps = tuple(lst)

            else:
                return True
        if gps in visited:
            return True
        return False
            

                

        