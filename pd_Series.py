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
# print(data['D']) #用Key來找value
# print(pd_find>2) #條件篩選

#刪除Value
_del = {'A':1, 'B':2, 'C':3, 'D':4} #index會變為dic中的key
pd_del = pd.Series(_del)
pd_del2 = pd_del.pop('B') #單獨把Key值為B的挑出，存到pd_del2中


#篩選條件
filter = [30, 15, 20] #篩選數字
pd_filter = pd.Series(filter)
# condition = [True, False, True] #方法一: 建立與資料數量對應的布林值列表
# filteredData = pd_filter[condition]
condition2 = pd_filter<=15 #方法二: 直接用比較運算建立布林值列表
filteredData2 = pd_filter[condition2]
filterWord = ['C++', 'python', 'JavaScript'] #篩選文字
pd_filterWord = pd.Series(filterWord)
condition3 = pd_filterWord.str.contains('python')

#運算
cal = [30, 15, 20]
pd_cal = pd.Series(cal)
cal2 = [2, 2, 2]
pd_cal2 = pd.Series(cal2)
pd_cal_add = pd_cal.add(pd_cal2)
pd_cal_sub = pd_cal.subtract(pd_cal2)
pd_cal_mul = pd_cal.multiply(pd_cal2)
pd_cal_div = pd_cal.divide(pd_cal2)
