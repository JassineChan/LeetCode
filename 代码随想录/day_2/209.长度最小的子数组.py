# 209.长度最小的子数组
# https://leetcode.cn/problems/minimum-size-subarray-sum/
# https://programmercarl.com/0209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.html
# https://www.bilibili.com/video/BV1tZ4y1q7XE
# 进阶：如果你已经实现 O(n) 的解法，试试 O(n log(n)) 的解法？
# 注意：本题与 209 题相似，题目要求返回的是长度最小的子数组，而不是和最小的子数组。

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # # 滑动窗口(快慢指针)
        # nums_len = len(nums)
        # left, right = 0, 0
        # # count记录区间和
        # count, ans = 0, 10 ** 6
        # while right < nums_len:
        #     count += nums[right]
        #     while count >= target:
        #         ans = min(ans, right-left+1)
        #         count -= nums[left]
        #         left += 1
        #     right += 1
        # return 0 if ans == 10 ** 6 else ans

        # 前缀和+二分查找
        nums_len = len(nums)
        ans = 10 ** 6
        # 因为都是正整数，所以前缀和数组一定是有序的
        pre_sum = [0] * nums_len
        for i in range(1, nums_len):
            pre_sum[i] = pre_sum[i-1] + nums[i-1]
        # 子数组的起始位置
        for i in range(nums_len):
            # 二分查找子数组的终止位置
            left, right = i, nums_len-1
            # nums[j] + pre_sum[j] - pre_sum[i] >= target
            # -> nums[j] + pre_sum[j] >= target + pre_sum[i]
            new_target = target + pre_sum[i]
            while left <= right:
                j = left + (right - left) // 2
                if nums[j]  + pre_sum[j] >= new_target:
                    ans = min(ans, j-i+1)
                    right = j - 1
                else:
                    left = j + 1
        return 0 if ans == 10 ** 6 else ans