# 239. 滑动窗口最大值
# https://leetcode.cn/problems/sliding-window-maximum/
# https://programmercarl.com/0239.%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.html

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # # 单调递减队列
        # from collections import deque
        # ans = []
        # queue = deque()
        # nums_len = len(nums)
        # # 初始化
        # for i in range(k):
        #     while queue and nums[i] > queue[-1]:
        #         queue.pop()
        #     queue.append(nums[i])
        # ans.append(queue[0])
        # # 滑动窗口
        # for i in range(k, nums_len):
        #     if nums[i-k] == queue[0]:
        #         queue.popleft()
        #     while queue and nums[i] > queue[-1]:
        #         queue.pop()
        #     queue.append(nums[i])
        #     ans.append(queue[0])
        # return ans

        # 优先队列(堆)
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i-k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans


        # 分块+预处理
        n = len(nums)
        prefixMax, suffixMax = [0] * n, [0] * n
        for i in range(n):
            if i % k == 0:
                prefixMax = nums[i]
            else:
                prefixMax[i] = max(prefixMax[i-1], nums[i])
        for i in range(n-1, -1, -1):
            if (i == n-1) or (i+1) % k == 0:
                suffixMax[i] = nums[i]
            else:
                suffixMax[i] = max(suffixMax[i+1], nums[i])
        ans = [max(suffixMax[i], prefixMax[i+k-1]) for i in range(n-k+1)]
        return ans