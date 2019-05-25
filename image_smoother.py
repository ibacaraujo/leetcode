class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        result = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for i in range(len(M)):
            for j in range(len(M[0])):
                temp = M[i][j]
                count_entries = 1
                for d in directions:
                    if 0 <= i+d[0] < len(M) and 0 <= j+d[1] < len(M[0]):
                        temp += M[i+d[0]][j+d[1]]
                        count_entries += 1
                result[i][j] = temp/count_entries
        return result
