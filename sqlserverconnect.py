from sqlalchemy import create_engine
import pandas as pd
Server='kreezy-HP-ProBook-430-G3'
Database='AdventureWorks2019'
Driver='ODBC Driver 17 for SQL Server'
Username='SA'
Password='Christopher3698'
Database_connection=f'mssql://{Username}:{Password}@{Server}/{Database}?driver={Driver}'
#conneting
engine=create_engine(Database_connection)
connection=engine.connect()
#using pandas to query data from the database
data=pd.read_sql_query("select * FROM Purchasing.Vendor WHERE CreditRating<3",connection)
print(data.head())