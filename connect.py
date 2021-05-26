import mysql.connector

# mydb = mysql.connector.connect(user='root', password='19841993',
#                               host='127.0.0.1', database='twitter_db',
#                               auth_plugin='mysql_native_password')

# mycursor = mydb.cursor()

# sql = "insert into post_table (user_name,post_date,post) values (%s,%s,%s)"
# val = ('connect_test1','2021-05-25','test test test test')
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")


def insert(array):
    '''
    insert object in list into table
    '''
    mydb = mysql.connector.connect(user='root', password='19841993',
                              host='127.0.0.1', database='twitter_db',
                              auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    for row in array:
        sql = "insert into post_table (user_name,post_date,post) values (%s,%s,%s)"
        val = (row[0],row[1],row[2])
        mycursor.execute(sql, val)
        mydb.commit()

def deleteall():
    mydb = mysql.connector.connect(user='root', password='19841993',
                              host='127.0.0.1', database='twitter_db',
                              auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    sql = "delete from  post_table"
    mycursor.execute(sql)
    mydb.commit()

def read():
    mydb = mysql.connector.connect(user='root', password='19841993',
                              host='127.0.0.1', database='twitter_db',
                              auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM post_table")
    myresult = mycursor.fetchall()
    res = []
    for x in myresult:
        res.append(x)
    return res