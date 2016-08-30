# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 09:08:19 2016

@author: Administrator
"""
# 本例子是介绍将对象写入磁盘 的一些操作 
# 参见 《python金融大数据分析》 P156

path = r"C:\Users\Administrator\Desktop\data.pkl"
import numpy as np
from random import gauss
import pickle

a = [gauss(1.5, 2) for i in range(100)]
#%% dump 
# 存取单个文件
pkl_file = open(path, "wb") # 之所以是wb不是w 就是因为这是二进制的

%time pickle.dump(a, pkl_file)
pkl_file

pkl_file.close()


#%% load 
pkl_file = open(path, "rb")
%time b = pickle.load(pkl_file)


#%%
# 存两个对象
pkl_file = open(path,'wb')
%time pickle.dump(np.array(a)**2 ,pkl_file)

%time pickle.dump(np.sqrt(np.array(a)) ,pkl_file)
pkl_file.close()
pkl_file = open(path, "rb")
x = pickle.load(pkl_file)
y = pickle.load(pkl_file)
pkl_file.close()

#%%
#存储字典
pkl_file = open(path,'wb')
pickle.dump({"x":x, 'y':y},pkl_file)
pkl_file.close()

pkl_file = open(path, "rb")
data = pickle.load(pkl_file)
pkl_file.close()

for key in data.keys():
    print(key, data[key][:5])





