class Solution:
    def markinfinity(self,matrix,row,col):
        r=len(matrix)
        c=len(matrix[0])
        for i in range(0,r):
            if matrix[i][col]!=0:
                matrix[i][col]=float("inf")
        for j in range(0,c):
            if matrix[row][j]!=0:
                matrix[row][j]=float("inf")
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r=len(matrix)
        c=len(matrix[0])
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j]==0:
                    self.markinfinity(matrix,i,j)
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j]==float("inf"):
                    matrix[i][j]=0
        