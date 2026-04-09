'''

Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false

1) take the problem in a small manner -> 3X3

2) iterate the sub problem and keep in mind of memory (maybe in a set?-> seperate function)
2.1) this set will take in account repetitions

3) if no repetitions then check for column wise and row wise repetitions (two functions?)

4) in total there could be three sub fucntions (grid wise, column wise, and row wise)



'''
# #ATTEMPT with set functions 
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         g = self.grid_wise_check(board)
#         r= self.row_wise_check(board)
#         c= self.column_wise_check(board) 
#         return False
    
#     #check row duplicates
#     def grid_wise_check(self, board: List[List[str]]) -> bool:
#         check = set([1,2,3,4,5,6,7,8,9])
#         grid_check = set()
#         row=0
#         col=0
        
#         for i in range(3):
#             for j in range(3):
#                 grid_check.add(board[row+i][col+j])
            
#             if len(check.intersection(grid_check))!=0:
#                 return False
            
#             col += 3
#             grid_check.clear()
            
#             if col == 9:
#                 row += 3
#                 col = 0
        
#         return True

#     #check row duplicates
#     def row_wise_check(self, board: List[List[str]]) -> bool:
#         check = set([1,2,3,4,5,6,7,8,9])
#         i=0
#         for i in range(len(board[i])):
#             if len(check.intersection(set(board[i])))!=0:
#                 return False
#         return True
    
#     #check col duplicate
#     def column_wise_check(self, board: List[List[str]]) -> bool:
#         check = set([1,2,3,4,5,6,7,8,9])
#         col_set = set()
#         i=0
#         j=0
#         for i in range(len(board[i])):
#             for j in range(len(board[i][j])):
#                 col_set.add(board[i][j])
#             if len(check.intersection(col_set))!=0:
#                 return False
#         return True


###SOLUTION
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) #key = (r/3,c/3)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                #if current element is a duplicate in rows column or sub 3x3 array
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c// 3)]
                ):
                    return False
                
                #update checks
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c// 3)].add(board[r][c])
        return True

        
        
