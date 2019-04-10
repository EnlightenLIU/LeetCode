'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-04-10 19:23:31
@LastEditTime: 2019-04-10 19:44:28
'''


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def str2int(num):
            res = 0
            for i in range(len(num)-1, -1, -1):
                res += int(num[i]) * pow(10, len(num)-1-i)
            return res
        return str(str2int(num1) + str2int(num2))
