import pymysql as ms

conn = ms.connect(host='localhost', user='root', password='', database='student')

mysql = conn.cursor()

deletename = input('Enter your name for delete: ')
delete = f"DELETE FROM studentrecord WHERE st_name='{deletename}'"

try:
    mysql.execute(delete)
    conn.commit()
    print('Record has been Deleted')

except ms.Error as e:
    print(f'Error: {e}')

finally:
    conn.close()
    mysql.close()