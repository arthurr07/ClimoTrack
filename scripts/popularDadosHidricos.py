import pandas as pd
import sqlite3

fields = ['ESTACAO_ID','T_MED_JAN','T_MED_FEV','T_MED_MAR','T_MED_ABR','T_MED_MAI','T_MED_JUN','T_MED_JUL','T_MED_AGO','T_MED_SET','T_MED_OUT','T_MED_NOV','T_MED_DEZ',
          'PRECIP_MD_JAN','PRECIP_MD_FEV','PRECIP_MD_MAR','PRECIP_MD_ABR','PRECIP_MD_MAI','PRECIP_MD_JUN','PRECIP_MD_JUL','PRECIP_MD_AGO','PRECIP_MD_SET',
          'PRECIP_MD_OUT','PRECIP_MD_NOV','PRECIP_MD_DEZ']
df = pd.read_csv("banco/BASE FINAL - DADOS CLIMÁTICOS - Cópia.xlsm - Plan1.csv", delimiter = ",", on_bad_lines="skip", encoding='ISO-8859-1', usecols=fields)
df.columns = df.columns.str.strip()

connection =sqlite3.connect("db.sqlite3")

df.to_sql('app_dadoshidricos', connection, if_exists='append', index = False)
# df.rename(columns={'T.MED_JAN':'t_med_jan','T.MED_FEV': 't_med_fev','T.MED_MAR':'t_med_mar','T.MED_ABR':'t_med_abr','T.MED_MAI':'t_med_mai','T.MED_JUN':'t_med_jun','T.MED_JUL':'t_med_jul',
#         'T.MED_AGO':'t_med_ago','T.MED_SET':'t_med_set','T.MED_OUT':'t_med_out','T.MED_NOV':'t_med_nov','T.MED_DEZ':'t_med_dez',
#         'PRECIP.MD_JAN':'precip_med_jan','PRECIP.MD_FEV':'precip_med_fev','PRECIP.MD_MAR':'precip_med_mar','PRECIP.MD_ABR':'precip_med_abr','PRECIP.MD_MAI':'precip_med_mai','PRECIP.MD_JUN':'precip_med_jun',
#         'PRECIP.MD_JUL':'precip_med_jul','PRECIP.MD_AGO':'precip_med_ago','PRECIP.MD_SET':'precip_med_set',
#         'PRECIP.MD_OUT':'precip_med_out','PRECIP.MD_NOV':'precip_med_nov','PRECIP.MD_DEZ':'precip_med_dez'})
print(df)