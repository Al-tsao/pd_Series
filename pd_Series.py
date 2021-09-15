#載入Pandas模組
import pandas as pd

#使用list建立Series
list = [1,2,3,4]
pd_list = pd.Series(list)
# print("list", pd_list)

#將Series反轉成list
list_r = pd_list.to_list()

#使用Dictionary建立Series
dic = {'A':1, 'B':2, 'C':3, 'D':4} #index會變為dic中的key
pd_dic = pd.Series(dic)
# print("list", pd_dic)

#將Series反轉成Dictionary
dic_r = pd_dic.to_dict()
# print(dic_r)

#自訂index
indexList = [1,2,3,4]
data = pd.Series(indexList, index=['A','B','C','D'])

#查找Value
find = {'A':1, 'B':2, 'B':2, 'C':3, 'C':3, 'C':3, 'D':4, 'D':4, 'D':4, 'D':4} #index會變為dic中的key，而且因為Key值有重複，所以只會留下一組
pd_find = pd.Series(find)
print(data['D']) #用Key來找value
print(pd_find>2) #條件篩選