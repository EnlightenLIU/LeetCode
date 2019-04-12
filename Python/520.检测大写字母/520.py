'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-04-12 16:14:11
@LastEditTime: 2019-04-12 16:47:49
'''


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        M = 0
        m = 0
        n = len(word)
        if n < 2:
            return True
        else:
            temp = word[0]
            for i in range(0, n):
                if ord(word[i]) >= ord('A') and ord(word[i]) <= ord('Z'):
                    M += 1
                if ord(word[i]) >= ord('a') and ord(word[i]) <= ord('z'):
                    m += 1
            if (ord(temp) >= ord('A') and ord(temp) <= ord('Z') and M == 1) or M == n or m == n:
                return True
            else:
                return False


# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         # 我了割草大神的解答
#         return word.islower() or word.isupper() or word.istitle()
