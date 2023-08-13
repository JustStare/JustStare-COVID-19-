import pymysql

def connect():
    db = pymysql.connect(  # 链接数据库MySQL
        host="localhost",
        port=3306,
        user="root",
        password="xxxxxxx",
        charset="utf8mb4"
    )

    return db

def disconnect(db, cursor):
    cursor.close()  # 关闭游标
    db.close()  # 断开数据库的链接

def initDBS():
    db = connect()
    cursor = db.cursor()  # 创建游标对象

    SQL = 'create schema if not exists dslab;'  # 创建dsLab模式
    cursor.execute(SQL)

    SQL = 'use dslab'  # 进入dsLab模式
    cursor.execute(SQL)

    SQL = 'create table if not exists linkTable (' \
          '     id int auto_increment primary key,' \
          '     time varchar(15),' \
          '     link varchar(150)' \
          ');'
    cursor.execute(SQL)
    SQL = 'create table if not exists originContent (' \
          '     id int auto_increment primary key,' \
          '     time varchar(15),' \
          '     content text' \
          ');'
    cursor.execute(SQL)
    SQL = 'create table if not exists pandemic (' \
          '     id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,' \
          '     time varchar(15),' \
          '     province varchar(10),' \
          '     new_confirm int default 0,' \
          '     new_asymptom int default 0' \
          ');'
    cursor.execute(SQL)

    disconnect(db, cursor)

# 创建所需的基本表，若已创建则无需运行
if __name__ == '__main__':
    initDBS()
