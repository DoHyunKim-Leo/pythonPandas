# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 18:41:45 2022

@author: user
"""

#####누락 데이터 확인
#데이터 불러오기
import seaborn as sns
#titanic 가져오기
df = sns.load_dataset('titanic')
print(df.info())

#deck 열의 NaN 개수 계산하기

