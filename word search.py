#TC - O(N*3^L)
#SC - O(L)
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.backtrack(i,j,0,word): return True
        return False
        
    def backtrack(self,i,j,idx,word):
        if idx == len(word):
            return True
        if i<0 or i>=len(self.board) or j<0 or j>=len(self.board[0]) or self.board[i][j]== '#':
            return False

        if self.board[i][j] == word[idx]:
            self.board[i][j] = '#'
            for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                nr = dx+i
                nc = dy+j

                if self.backtrack(nr,nc,idx+1,word):
                    return True
            
            #backtrack
            self.board[i][j] = word[idx]

        return False