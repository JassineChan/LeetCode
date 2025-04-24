# 704. 二分查找
# https://leetcode.cn/problems/binary-search/
# https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html
# https://www.bilibili.com/video/BV1fA4y1o715

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # # 左闭右开
        # nums_len = len(nums)
        # left, right = 0, nums_len
        # while left < right:
        #     # 防止溢出
        #     mid = left + (right - left) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return -1
        # 左闭右闭
        nums_len = len(nums)
        left, right = 0, nums_len - 1
        while left <= right:
            # 防止溢出
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
