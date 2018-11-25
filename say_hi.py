# coding=utf-8
import pymssql

msg ="Hi"
print(msg)
connect_ = pymssql.connect(server='localhost',\
                            port = '1433',\
        user='si_test', \
        password='si_test',\
        database='test',\
        timeout=0,\
        login_timeout=60, \
        charset='UTF-8',\
        autocommit=False)

cursor = connect_.cursor()

try:
    for i in range(10):
        print(i)
        cursor.execute('INSERT INTO  test.dbo.test_tab VALUES  (%d)',(i,))
        
        #print(cursor.)
except pymssql.Error as ex_:
    
     print(ex_)
else:
    try:
        connect_.commit()
        connect_.close()
    except pymssql.Error as ex_:
     connect_.rollback()
     print(ex_)
