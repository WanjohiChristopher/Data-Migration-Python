
import psycopg





conn = psycopg.connect(host="localhost", port = 5432, dbname="movedata", user="postgres", password="Yourpassword")

# Create a cursor object
cur = conn.cursor()

# A sample query of all data from the "vendors" table in the "suppliers" database
cur.execute("""SELECT * FROM custdatademo""")
query_results = cur.fetchall()
print(query_results)

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
conn.close()
