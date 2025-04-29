# 18. 四数之和
# https://leetcode.cn/problems/4sum/
# https://programmercarl.com/0018.%E5%9B%9B%E6%95%B0%E4%B9%8B%E5%92%8C.html

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 排序+对撞双指针
        n = len(nums)
        ans = []
        nums.sort()
        for a in range(n):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, n):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                c, d = b+1, n-1
                while c < d:
                    if nums[a] + nums[b] + nums[c] + nums[d] > target:
                        d -= 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] < target:
                        c += 1
                    else:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
        return ans                  