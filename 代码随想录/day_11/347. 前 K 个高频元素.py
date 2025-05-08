# 347. 前 K 个高频元素
# https://leetcode.cn/problems/top-k-frequent-elements/
# https://programmercarl.com/0347.%E5%89%8DK%E4%B8%AA%E9%AB%98%E9%A2%91%E5%85%83%E7%B4%A0.html

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 回家等通知
        # from collections import Counter
        # num2count = Counter(nums)
        # num_count = sorted(num2count.items(), key=lambda item: item[1], reverse=True)
        # ans = []
        # for i in range(k):
        #     ans.append(num_count[i][0])
        # return ans

        # 优先队列(小顶堆)
        import heapq
        num2count = {}
        for i in range(len(nums)):
            num2count[nums[i]] = num2count.get(nums[i], 0) + 1
        small_heap = []
        for num, count in num2count.items():
            heapq.heappush(small_heap, (count, num))
            if len(small_heap) > k:
                heapq.heappop(small_heap)
        ans = []
        for i in range(k):
            ans.append(heappop(small_heap)[1])
        return ans