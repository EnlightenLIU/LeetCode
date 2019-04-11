'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-04-11 20:54:08
@LastEditTime: 2019-04-11 21:56:55
'''
import operator
f = open('D:/VSCodeProject/Python/192.统计词频/words.txt', 'r')
contexts = f.read()
print(contexts)
contexts = contexts.split()
dic = {}
for word in contexts:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1

# 字典按照value值排序
swd = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
dic = dict(swd)
print(dic)
