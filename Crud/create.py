import pymysql as ms

conn = ms.connect(host='localhost', user='root', password='', database='student')

mysqlc = conn.cursor()

tc = "CREATE TABLE studentrecord(st_id INT PRIMARY KEY AUTO_INCREMENT, st_name VARCHAR(50), st_class VARCHAR(10), st_email VARCHAR(50))"

try:
    mysqlc.execute(tc)

    conn.commit()
    print("Table 'studentrecord' created successfully.")

except ms.Error as e:
    print(f"Error: {e}")

finally:
    if 'conn' in locals():
        conn.close()
        print("MySQL connection closed.")
