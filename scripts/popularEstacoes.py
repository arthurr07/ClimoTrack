import pandas as pd
import sqlite3

fields = ['ESTACAO']
df = pd.read_csv("banco/BASE FINAL - DADOS CLIMÁTICOS - Cópia.xlsm - Plan1.csv", delimiter = ",", on_bad_lines="skip", encoding='UTF-8', usecols=fields)
df["estado_id"]=1
df.columns = df.columns.str.strip()

connection =sqlite3.connect("db.sqlite3")

df.to_sql('app_cidade', connection, if_exists='append', index = False)
print(df)