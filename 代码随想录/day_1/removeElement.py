# 27. 移除元素
# https://leetcode.cn/problems/remove-element/ 
# https://programmercarl.com/0027.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.html
# https://www.bilibili.com/video/BV12A4y1Z7LP

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # # 暴力解法
        # # 经典错误
        # for num in nums:
        #     if num == val:
        #         nums.pop(num)
        # return len(nums)
        nums_len = len(nums)
        for i in range(nums_len):
            if nums[i] == val:
                for j in range(i+1, nums_len):
                    if nums[j] != val:
                        nums[i], nums[j] = nums[j], nums[i]
        ans = 0
        for i in range(nums_len):
            if nums[i] == val:
                break
            ans += 1
        return ans

        # # 对撞双指针
        # # left从左往右找val值
        # # right从右往左找非val值
        # nums_len = len(nums)
        # left, right = 0, nums_len-1
        # while left <= right:
        #     if nums[left] != val:
        #         left += 1
        #     else:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         right -= 1
        # return left
        
        # # 快慢双指针
        # left从左往右停留在val值
        # right从左往右寻找非val值
        # nums_len = len(nums)
        # left, right = 0, 0
        # while right < nums_len:
        #     if nums[right] != val:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1
        #         right += 1
        #     else:
        #         right += 1
        # return left
                