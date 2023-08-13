from update import *

nums = 400  # 选择400天的数据，可更改
if __name__ == '__main__':
    initDBS()
    db = connect()
    cursor = db.cursor()
    SQL = 'use dslab;'
    cursor.execute(SQL)

    # 爬取链接和原始信息
    origin = 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml'
    urls = list()

    crawl_content(db, cursor, urls, origin, nums)   # 链接存在url里

    # 对已爬取的数据进行正则、整理，并将结果插入到表pandemic中
    SQL = 'select count(*) from origincontent;'
    cursor.execute(SQL)
    count = cursor.fetchone()[0]  # 获得列表的项数
    for i in range(1, count + 1):  # id从1开始计数
        SQL = 'select time, content from origincontent where id = %d;' % i
        cursor.execute(SQL)
        res = cursor.fetchall()
        myDict = regex(res[0][0], res[0][1])
        myWrite(db, cursor, myDict)
