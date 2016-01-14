# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 20:05:59 2016
For MariaDB(Mysql) process.
@author: sdgtliuwei
version ：Python 3.4
"""
import mysql.connector
import sys

"""初始化"""
def init():
    host = '127.0.0.1'#'localhost'
    user = 'root'
    password = 'admin'
    database = 'hi_db'
    port = 3306
    charset = 'utf8'
    return  host, user, password, database, port, charset

"""连接"""   
def connect(host, user, password, database, port, charset):
    try:
        conn = mysql.connector.connect(host = host, user = user, password = password, database = database, port = port, charset = charset)
        return conn;
    except mysql.connector.Error as err:
        print("Connect Mysql failed.")
        print("Error: {}".format(err.msg))
        sys.exit()

"""查"""      
def query(conn, temp_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(temp_sql)
        data=cursor.fetchall()
        for d in data :
            print(d)
          #  print('name: ' + d[0] + ' psd:' + d[1] + '  email:' + d[2] + ' phone:' + str(d[3]))
#        for (name, psd, email, phone) in cursor:
#            print("name:{}  psd:{}  email:{}  phone:{}".format(name, psd, email, phone))
        cursor.close()
    except mysql.connector.Error as err:
        print("Query Mysql failed.")
        print("Error: {}".format(err.msg))
        sys.exit()

"""增、删、改"""        
def change(conn, temp_sqllist):
    cursor = conn.cursor()
    for i in temp_sqllist:
        cursor.execute(i)
    conn.commit()
    cursor.close()

"""关闭数据库"""   
def close(conn):
    try:
        conn.close()
    except mysql.connector.Error as err:
        print("Close Mysql failed.")
        print("Error: {}".format(err.msg))
        sys.exit()

if __name__ == "__main__":
    host, user, password, database, port, charset = init()
    conn = connect(host, user, password, database, port, charset)
    query_sql = 'select * from user_info_table'
    query(conn, query_sql)
    change_sql = ["insert into user_info_table values('a', 'aa', 'aaa', 1)"]
    change(conn, change_sql)