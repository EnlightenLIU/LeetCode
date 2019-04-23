'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-04-23 15:25:40
@LastEditTime: 2019-04-23 15:42:25
'''


# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         result = {}
#         for i in ransomNote:
#             if i in result.keys():
#                 result[i] += 1
#             else:
#                 result[i] = 1
#         for j in magazine:
#             if j in result.keys():
#                 result[j] -= 1

#         for i in result.keys():
#             if result[i] > 0:
#                 return False

#         return True

# 最优解
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if not ransomNote:
            return True
        temp = set(ransomNote)

        for i in temp:
            if i in magazine and magazine.count(i) >= ransomNote.count(i):
                continue
            else:
                return False
        return True
