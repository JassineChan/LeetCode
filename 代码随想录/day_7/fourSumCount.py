# 454. 四数相加 II
# https://leetcode.cn/problems/4sum-ii/
# https://programmercarl.com/0454.%E5%9B%9B%E6%95%B0%E7%9B%B8%E5%8A%A0II.html

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 分组+哈希表
        ans = 0
        n = len(nums1)
        # 记录两组元素和
        group_12, group_34 = {}, {}
        for i in range(n):
            for j in range(n):
                count = nums1[i] + nums2[j]
                group_12[count] = group_12.get(count, 0) + 1
                count = nums3[i] + nums4[j]
                group_34[count] = group_34.get(count, 0) + 1
        for key_12, value_12 in group_12.items():
            if -key_12 in group_34:
                ans += value_12 * group_34[-key_12]
        return ans