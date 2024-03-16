from tabulate import tabulate
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="DineshKP@0808", database="dinesh")
res = conn.cursor()
sql = "SELECT * FROM persons"
res.execute(sql)
result = res.fetchall()

# Displaying the result in tabular format
print(tabulate(result, headers=res.column_names))

conn.commit()
conn.close()