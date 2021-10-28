import pymssql
#connecting using pymssql
connection=pymssql.connect(host='localhost',user="SA",password="Christopher3698",database="AdventureWorks2019")
#query data
# performing query
query="SELECT * FROM Purchasing.Vendor WHERE CreditRating<3"
#creating cursor
curs=connection.cursor()
#execute query
curs.execute(query)
#fetching data
data=curs.fetchall()
print(data)