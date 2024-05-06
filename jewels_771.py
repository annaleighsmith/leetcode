

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        # O(n+m) solution
        jewels_dict = {}
        for j in J:
            jewels_dict[j] = 0
        
        print(jewels_dict)
        
        ct = 0
        for s in S:
            if s in jewels_dict:
                ct += 1

        return ct



if __name__ == '__main__':
    solution = Solution()
    J = "aA"
    S = "aAAbbbb"
    print(solution.numJewelsInStones(J, S))  # 3

