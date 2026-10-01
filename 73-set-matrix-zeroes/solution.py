class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m=len(matrix) #строки (для себя, я не гпт)
        n=len(matrix[0]) #cтолбцы
        rows=set()
        colomns=set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0: 
                    rows.add(i)
                    colomns.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in rows or j in colomns:
                    matrix[i][j]=0

