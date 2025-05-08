# 1. 两数之和
# https://leetcode.cn/problems/two-sum/
# https://programmercarl.com/0001.%E4%B8%A4%E6%95%B0%E4%B9%8B%E5%92%8C.html

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # 暴力解法
        # nums_len = len(nums)
        # for i in range(nums_len-1):
        #     for j in range(i+1, nums_len):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # 哈希表
        hash_map = dict()
        nums_len = len(nums)
        for i in range(nums_len):
            tmp = target-nums[i]
            if tmp in hash_map:
                return [i, hash_map[tmp]]
            else:
                hash_map[nums[i]] = i