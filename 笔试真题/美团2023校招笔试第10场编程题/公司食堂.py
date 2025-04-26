import sys

# # 暴力破解（运行超时，6/12 组用例通过）
# T = int(sys.stdin.readline().strip())
# # 各组分开处理
# for _ in range(T):    
#     N = int(sys.stdin.readline().strip())
#     line = sys.stdin.readline().strip()
#     tables = []
#     for i in range(N):
#         tables.append(int(line[i]))
#     M = int(sys.stdin.readline().strip())
#     people = []
#     line = sys.stdin.readline().strip()
#     for i in range(M):
#         people.append(line[i])
#     for person in people:
#         # 男职员：先坐1人，否则0人
#         if person == "M":
#             # 记录遇到的第一个0
#             first_zero = 500000
#             found = 0
#             for i in range(N):
#                 if tables[i] == 0:
#                     first_zero = min(i, first_zero)
#                 elif tables[i] == 1:
#                     tables[i] = 2
#                     found = 1
#                     print(i+1)
#                     break
#             if found == 0:
#                 tables[first_zero] = 1
#                 print(first_zero+1)
#         # 女职员：先坐0人，否则1人
#         else:
#             # 记录遇到的第一个1
#             first_one = 500000
#             found = 0
#             for i in range(N):
#                 if tables[i] == 0:
#                     tables[i] = 1
#                     found = 1
#                     print(i+1)
#                     break
#                 elif tables[i] == 1:
#                     first_one = min(i, first_one)
#             if found == 0:
#                 tables[first_one] = 2
#                 print(first_one+1)
            
# 优化：使用最小堆（运行超时，11/12 组用例通过）
import heapq
T = int(sys.stdin.readline().strip())
# 各组分开处理
for _ in range(T):    
    N = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    tables = []
    for i in range(N):
        tables.append(int(line[i]))
    M = int(sys.stdin.readline().strip())
    people = []
    line = sys.stdin.readline().strip()
    for i in range(M):
        people.append(line[i])
    # 维护两个最小堆
    zero_heap = []
    one_heap = []
    for i in range(N):
        if tables[i] == 0:
            heapq.heappush(zero_heap, i)
        elif tables[i] == 1:
            heapq.heappush(one_heap, i)
    for person in people:
        # 男职员：先坐1人，否则0人
        if person == "M":
            while one_heap and tables[one_heap[0]] != 1:
                heapq.heappop(one_heap)
            if one_heap:
                idx = heapq.heappop(one_heap)
                tables[idx] = 2
                print(idx + 1)
            else:
                while zero_heap and tables[zero_heap[0]] != 0:
                    heapq.heappop(zero_heap)
                idx = heapq.heappop(zero_heap)
                tables[idx] = 1
                heapq.heappush(one_heap, idx)
                print(idx + 1)
        # 女职员：先坐0人，否则1人
        else:
            while zero_heap and tables[zero_heap[0]] != 0:
                heapq.heappop(zero_heap)
            if zero_heap:
                idx = heapq.heappop(zero_heap)
                tables[idx] = 1
                heapq.heappush(one_heap, idx)
                print(idx + 1)
            else:
                while one_heap and tables[one_heap[0]] != 1:
                    heapq.heappop(one_heap)
                idx = heapq.heappop(one_heap)
                tables[idx] = 2
                print(idx + 1)
            