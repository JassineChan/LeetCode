# 977. 有序数组的平方
# https://leetcode.cn/problems/squares-of-a-sorted-array/
# https://programmercarl.com/0977.%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E5%B9%B3%E6%96%B9.html
# https://www.bilibili.com/video/BV1QB4y1D7ep 

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 双指针
        nums_len = len(nums)
        ans = [0] * nums_len
        # 最大值只有可能在两端
        cur_index = nums_len-1
        left, right = 0, nums_len-1
        while left <= right:
            left_squre = nums[left] ** 2
            right_squre = nums[right] ** 2
            if left_squre > right_squre:
                ans[cur_index] = left_squre
                cur_index -= 1
                left += 1
            else:
                ans[cur_index] = right_squre
                cur_index -= 1
                right -= 1
        return ans