import pymysql as ms

conn = ms.connect(host='localhost', user='root', password='', database='student')

mysql = conn.cursor()

insert = "INSERT INTO studentrecord (st_name, st_class, st_email) VALUES ('Abdul Malik', 'Middle', 'ishaq@example.com'), ('Muhammad Ali','Matric','abdulkhaliq@gmail.com')"

try:
    mysql.execute(insert)
    conn.commit()
    print('Record Successfully added')
except:
    conn.close()
    print('Error...')