import pymysql as ms

conn = ms.connect(host='localhost', user='root', password='', database='student')

mysql = conn.cursor()

setname = input('Enter your name for update: ')
update = f"UPDATE studentrecord SET st_name = '{setname}' WHERE st_name = 'Abdul'"

try:
    mysql.execute(update)
    conn.commit()
    print('Record has been updated')

except ms.Error as e:
    print(f'Error: {e}')

finally:
    conn.close()
    mysql.close()
