# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
#f = open(r'F:\record\Exercise\Coursera\Python Obtain_Nanjing University\HW\ml-100k\u.data','r')
path = 'F:\\record\\Exercise\\Coursera\\Python Obtain_Nanjing University\\HW\\ml-100k\\'
f = open(path+'u.data','r')
data_names = ['user_id','item_id','rating','timestamp']
udata =  pd.read_table(path+'u.data',sep = '\t',names = data_names)
#print udata[:5]
user_name = ['user_id','age','gender','occupation','zip_code']
uuser = pd.read_table(path+'u.user',sep = '|',names = user_name)
#print uuser[:5]
item_name = ['movie_id','movie_title' , 'release_date' , 'video_release_date ',
'IMDb_URL ', 'unknown ', 'Action ', 'Adventure' , 'Animation' , 'Children''s',
'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,'Film-Noir' , 'Horror' , 
'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,'Thriller' , 'War' , 'Western']
item = pd.read_table(path+'u.item',sep = '|',names = item_name)
#print item[:5]
data_merge = pd.merge(udata,uuser,how='inner') #将udata与uuser两表关联，默认以user_id为关联字段
#print data_merge[:5]
data_std_1 = pd.pivot_table(data_merge, values='rating', columns='gender', aggfunc='std')
print "use pivot table:\n",data_std_1
data_std_2 = pd.pivot_table(data_merge, index=['gender'], values='rating')
gender_s = pd.DataFrame(data_std_2)
Female_df = gender_s.query("gender==['F']")
Male_df = gender_s.query("gender==['M']")
Female_std = np.std(Female_df)
Male_std = np.std(Male_df)
print 'use np std:\n','F\t%.4f'%Female_std,'\nM\t%.4f'%Male_std
