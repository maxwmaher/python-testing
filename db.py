import psycopg2

#connect to the db
con = psycopg2.connect(
    user="maxmaher",
    password="123",
    host="localhost",
    port="5432",
    database="python_testing"
    )

#cursor
cur = con.cursor()

#execute query
cur.execute('SELECT name, occupation FROM "user"')

rows = cur.fetchall()

for r in rows:
    print (f"name {r[0]}, occupation {r[1]}")

#close the cursor
cur.close()

#close the connection
con.close()
