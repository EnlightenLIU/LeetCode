'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-01-14 20:34:12
@LastEditTime: 2019-01-15 11:04:46
'''
import pandas as pd
from pandas import Series, DataFrame
data = {'Chinese': [66, 95, 93, 90, 80],
        'English': [65, 85, 92, 88, 90], 'Math': [None, 98, 96, 77, 90]}
df2 = DataFrame(data, index=['zhangfei', 'guanyu',
                             'zhaoyun', 'huangzhong', 'dianwei'], columns=['English', 'Math', 'Chinese'])
df2 = df2.rename(columns={'Chinese': 'YuWen',
                          'English': 'YingYu', 'Math': 'ShuXue'})

df2.columns = df2.columns.str.upper()
# print(df2)
print(df2.isnull())
print(df2.isnull().any())
