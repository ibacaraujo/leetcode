class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #rows = []
        #columns = []
        #sub_boxes = []
        #for i in range(len(board)):
        #    row = map(str, board[i])
        #    rows.append(row)
        #    for j in range(len(board[i])):  
        #        if board[i][j] != '.':
        #            print(board[i][j])
        #print(rows)
        board_set = set()
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    row = num + ' in row ' +str(i)
                    col = num + ' in col ' +str(j)
                    blk = num + ' in blk ' + str(i//3) + '-' + str(j//3)
                    if row in board_set or col in board_set or blk in board_set:
                        return False
                    board_set.add(row)
                    board_set.add(col)
                    board_set.add(blk)
        return True
 
