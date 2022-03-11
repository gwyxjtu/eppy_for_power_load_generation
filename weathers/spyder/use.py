import os
from collections import defaultdict

filePath = "./"
for _,d,_ in os.walk(filePath):
	break 
	# 很奇怪为什么是一个迭代对象？难道是迭代打开子目录？
def addtwodimdict(thedict, key_a, key_b, val): 
    if key_a in thedict:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})

main_dic = dict(dict())
for name in d:
	#print(name.split("."))
	province,city = name.split(".")[0][4:],name.split(".")[-2]
	#print(province,city)
	# if province in main_dic.keys():
	#main_dic[province][city] = name
	addtwodimdict(main_dic,province,city,name)

#print(main_dic)
import json
print(json.dumps(main_dic,indent = 4))
