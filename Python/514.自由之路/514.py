import collections


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dic = collections.defaultdict(list)
        # enumerate返回枚举类型
        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
        for i, ch in enumerate(ring):
            dic[ch].append(i)
        l = len(ring)
        past = [(0, 0)]
        for ch in key:
            # 找出要查找的字符
            cur = []
            # 遍历存在该值的字典数组
            for curIndex in dic[ch]:
                # 设置一个最小次，在下面循环时得出的值需要与这个最小值比较
                this_min = float('inf')#这里是正无穷
                for pastIndex, m in past:  # 此次m表示上一次最小的距离
                    # 当前位置与前1位置距离最近的点
                    temp = abs(curIndex - pastIndex)
                    this_min = min(this_min, m + temp, m + l - temp)  #此处一直是求遍历后最小的min值
                # 添加当前的索引和最值
                cur.append((curIndex, this_min))
            past = cur
        # past最后为一个数组，其中m为除最终移动的距离，然后取最小的返回
        return min([n[1] for n in past]) + len(key)

sf=Solution()
ring = "godding"
key = "gd"
a=sf.findRotateSteps(ring,key)
print(a)