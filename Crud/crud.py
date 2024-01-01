import pymysql as ms

host = 'localhost'
user = 'root'
password = ''

myobj = ms.connect(host=host, user=user, password=password)

cursor = myobj.cursor()

try:
    db = "create database student"
    cursor.execute(db)
    print('Database Created')
except:
    print('Database error...')
