# 暴力解法
# class Solution(object):
#     def largestRectangleArea(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: int
#         """
#
#         l=len(heights)
#         if l==0:
#             return 0
#         if l==1:
#             return heights[0]
#         max_area=[0 for _ in range(l)]
#         for i in range(1,l):
#             max_area[0]=heights[0]
#             for j in range(i+1):
#                 min_l=min(heights[i-j:i+1])
#                 area=min_l*(j+1)
#                 # print(area)
#                 if area>max_area[i]:
#                     max_area[i]=area
#             if max_area[i]<max_area[i-1]:
#                 max_area[i]=max_area[i-1]
#         return max_area[-1]
#
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        largest = 0
        stack = [-1]
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                i_know = stack.pop()
                area = (i - stack[-1] - 1) * heights[i_know]
                if area > largest:
                    largest = area
            stack.append(i)
        return largest

s=Solution()
heights=[2,1,5,6,2,3]
area=s.largestRectangleArea(heights)
print('最大',area)


