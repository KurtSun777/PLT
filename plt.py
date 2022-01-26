#!/usr/bin/env python
# coding: utf-8

# # XGBoost

# In[22]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from xgboost import plot_importance
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import font_manager


# In[23]:


df = pd.read_csv('newlabel.csv')
df.head(3)
# df1 = df.iloc[:1000, :]

df.head(3)


# In[37]:


freq = df['sequel'].value_counts() 
freq


# In[33]:


def MyPie():
    law = ['公然侮辱一', '公然侮辱二', '誹謗一', '誹謗二']
    law_count = [7852, 141, 931, 2513]
    
 
     # 2.創建畫布
    plt.figure(figsize=(10, 5), dpi=100)
 
     # 3,繪製餅圖
    colors = ['b', 'y', 'g', 'r']
     # autopct="%1.2f%%" 保留2位小數
     # shadow=True,startangle=90   是否有陰影
    plt.pie(law_count, labels = law, autopct="%1.2f%%", colors=colors, shadow=True,
    startangle=90)
  
     # 顯示圖例
    plt.legend()
 
     # 爲了讓顯示的餅圖保持圓形，需要添加axis保證長寬一樣
    plt.axis('equal')
 
     # 添加標題
    plt.title("percentage of law")
 
     # 中文防止亂碼
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
     # 4）顯示圖像
    plt.show()
     
MyPie()


# In[ ]:




