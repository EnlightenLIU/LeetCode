from collections import Counter
class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # 使用Counter将数组转换成字典key = 数组元素值value = 相同元素的个数对数组按照绝对值大小进行排序
        # 如果x的个数大于2x的个数必定有x无法和2x匹配，返回Flase
        # 更新2x的个数 =（2x - x）的个数直到2x个数为0才返回true
        a = Counter(A)

        for x in sorted(a,key=lambda x:abs(x)):
            if  a[x]>a[2*x]:
                return False
            a[2*x]-=a[x]
        return True

