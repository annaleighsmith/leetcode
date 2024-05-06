class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        hashy = {}
        answer = []
        for g in groupSizes:
            if g not in hashy:
                hashy[g] = []

        for i, g in enumerate(groupSizes):
            hashy[g].append(i)

        for g, idx in hashy.items():
            group_idx = []
            for i in idx:
                group_idx.append(i)
                if len(group_idx) == g:
                    answer.append(group_idx)
                    group_idx = []

        return answer


solution = Solution()
groupSizes = [3,3,3,3,3,1,3]
res = solution.groupThePeople(groupSizes)
print(res)



        
