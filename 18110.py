# from collections import deque
# import math
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# if n == 0:
#     print(0)
#     quit()
#
# else:
#     arr = deque(sorted([int(input()) for i in range(n)]))
#
#     cut =  int(0.15 * n + 0.5)
#
#     for i in range(cut):
#         arr.popleft()
#     for i in range(cut):
#         arr.pop()
#
#     print(int(sum(arr)/len(arr) + 0.5))

