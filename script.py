import pandas as pd
import sqlite3

df = pd.read_csv("banco/BASE FINAL - DADOS CLIMÁTICOS - Cópia.xlsm - Plan1.csv", delimiter = ",", on_bad_lines="skip", encoding='ISO-8859-1')
df.columns = df.columns.str.strip()
connection =sqlite3.connect("sqlite3.db")
df.to_sql('table', connection, if_exists='replace')
print(df)