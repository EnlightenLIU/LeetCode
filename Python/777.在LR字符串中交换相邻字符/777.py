'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-04-19 13:46:24
@LastEditTime: 2019-04-19 14:32:14
'''
# 这种解法完全无法理解
# class Solution(object):
#     def canTransform(self, start, end):
#         """
#         :type start: str
#         :type end: str
#         :rtype: bool
#         """
#         i, j = 0, 0
#         N = len(start)
#         while i < N and j < N:
#             while i < N - 1 and start[i] == 'X':
#                 i += 1
#             while j < N - 1 and end[j] == 'X':
#                 j += 1
#             if start[i] != end[j]:
#                 return False
#             if start[i] == 'L' and i < j:
#                 return False
#             if start[i] == 'R' and i > j:
#                 return False
#             i += 1
#             j += 1
#         return True


class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if not start or len(start) == 0 or start == end:
            return True
        if len(start) == 1:
            return False

        xl, rx = [], []
        for i in range(len(start)):
            if start[i] == end[i]:
                continue
            elif start[i] == 'X' and end[i] == 'L':
                xl.append('L')
            elif start[i] == 'L' and end[i] == 'X':
                if not xl:
                    return False
                xl.pop()
            elif start[i] == 'R' and end[i] == 'X':
                rx.append('R')
            elif start[i] == 'X' and end[i] == 'R':
                if not rx:
                    return False
                rx.pop()
            else:
                return False
        return not rx and not xl
