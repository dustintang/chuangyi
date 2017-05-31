#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 22:57:56 2017
读取好租数据库并分析
@author: dustin
"""
import pandas as pd
import pymysql
import matplotlib as mpl
custom_font = mpl.font_manager.FontProperties(fname='/Users/dustin/Documents/study/Database/test/jieba/字体/Lantinghei.ttf') 

conn = pymysql.connect(host='127.0.0.1',
                       port=3306, 
                       user='root', 
                       passwd='123456', 
                       db='haozu',
                       charset='utf8')
sql='select * from 写字楼'
df = pd.read_sql(sql , con=conn)
df.describe(include=all)


def counts(col1,value1,col2,df=df):
    count = df[df[col1]==value1][col2].value_counts()
    return count

counts('城市','上海','区域')
counts('城市','北京','区域')
counts('城市','深圳','区域')
counts('城市','成都','区域')
counts('城市','武汉','区域')


'''
df.dtypes
df.index
df.columns
df.T
df.sort(columns='参考价')
df.sort_values(by=['参考价','房源数'])
df.groupby('参考价')['参考价'].agg([('ADSL','count')])
df.写字楼等级.describe()
df.写字楼等级.unique()
df.写字楼等级.value_counts()
a='区域'
df[df['城市']=='北京']['区域'].value_counts()
'''






'''
cur.execute("SELECT 品牌,空间名,地址 FROM 空间")
r = cur.fetchall()
for i in r:
    a=i[2].split('区',1)
    try:
        sql = 'update 空间 set 地址="'+a[1]+'" where 品牌 ="'+i[0]+'"and 空间名 ="'+i[1]+'"'
    except:
        sql = 'update 空间 set 地址="'+a[0]+'" where 品牌 ="'+i[0]+'"and 空间名 ="'+i[1]+'"'
    cur.execute(sql)  
'''








#提交修改——————————————————————
conn.commit()
#关闭连接
cur.close()
conn.close()