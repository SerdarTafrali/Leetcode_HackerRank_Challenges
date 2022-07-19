""" Given an integer numRows, return the first numRows of Pascal's triangle. 
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]] """

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        
        for i in range(2,numRows+1):
            temp = [1]
            for j in range(1,i-1):
                temp.append(pascal[-1][j]+pascal[-1][j-1])
            temp.append(1)
            pascal.append(temp)
            
        return pascal
