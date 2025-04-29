# 15. 三数之和
# https://leetcode.cn/problems/3sum/
# https://programmercarl.com/0015.%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.html

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 排序+对撞双指针
        ans = []
        nums.sort()
        nums_len = len(nums)
        # 注意不能先跳过重复值
        for i in range(nums_len):
            # 控制指针活动区间
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, nums_len-1
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # 跳过所有重复项
                    while j < k and nums[k+1] == nums[k]:
                        k -= 1
                    # 跳过所有重复项
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
        return ans         