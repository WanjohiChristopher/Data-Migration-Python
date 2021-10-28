import pymssql,psycopg
import time
# create a class for database request
start=time.time()
class Databaserq:
    #creating a constructor 
    def __init__(self):
        #connecting both mssql and postgres
        self.con=pymssql.connect(host='localhost',user="SA",password="Christopher3698",database="AdventureWorks2019")
        self.conn=psycopg.connect(host="localhost", port = 5432, dbname="SsqlAdventureCopies", user="postgres", password="Christopher3698")
        
        #creating a cursor for both databases
        self.cur=self.con.cursor()
        self.cur1=self.conn.cursor()
#  now created a fuction for migartion/execution of the migration pipeline
    def migrate(self):
        self.cur.execute("SELECT * FROM Purchasing.Vendor WHERE CreditRating<3")
        rows=self.cur.fetchall()
        
        return rows
     
    def inserting(self,rows):
        try:
             for row in rows:
                 
                self.cur1.execute("INSERT INTO purchase(businessentityid,accountnumber,fname,creditrating,preferredvendorstatus,activeflag,purchasingwebserviceurl,modifieddate) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",row)
            
                self.conn.commit()
                print("inserted")
        except Exception as e:
            print(e)
result=Databaserq()#object
data = result.migrate()
result.inserting(data)

#getting the time taken to execute the migration
print(f'The time taken to run is:{time.time()-start} seconds')
