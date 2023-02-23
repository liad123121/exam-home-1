import mysql.connector
from flask import Flask


mydb = mysql.connector.connect(
    host="db",
    user="root",
    passwd = "123456"
)

def init_db(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/exam_test'

    cur = mydb.cursor()
    cur.execute("SHOW DATABASES")
    fdbs = cur.fetchall()

    dbs = [db[0] for db in fdbs]

    if('exam_test') not in dbs:
        cur.execute("CREATE DATABASE exam_test")
    
    mydb.database = 'exam_test'
    
    cur.execute('SHOW TABLES')
    ftables = cur.fetchall()

    tables = [t[0] for t in ftables]

    if('access_log') not in tables:
        cur.execute('CREATE TABLE access_log (id INT PRIMARY KEY AUTO_INCREMENT, date DATE, clientIP VARCHAR(255), internalIP VARCHAR(255))')
        mydb.commit()
    cur.close()

