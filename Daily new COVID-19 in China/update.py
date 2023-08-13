from charts import *
from myWR import *
from myCrawl import *
from myRegex import *
from DBS import *
import os
import datetime

def getStr(cursor, myTime):
    SQL = "select content from origincontent where time = '%s'" % myTime
    cursor.execute(SQL)
    res = cursor.fetchone()[0]

    return res

def updateTable():
    db = connect()
    cursor = db.cursor()
    SQL = 'use dslab'  # 进入dsLab模式
    cursor.execute(SQL)

    origin = 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml'

    link = dailyLink(origin)       # 获取link，从链接表中
    myTime = dailyCrawl(db, cursor, link)
    # 用myTime去索引原始数据库，得到string
    myString = getStr(cursor, myTime)  # 从原始数据库中获取数据
    myDict = regex(myTime, myString)  # 获取处理后的字典，可转为json
    # j_str = json.dumps(myDict)  # 转为json类型
    myWrite(db, cursor, myDict)  # 插入pandemic数据库

    date = datetime.date.today()
    print(f'{date} 更新成功!')

    disconnect(db, cursor)

def updateChart():
    db = connect()
    cursor = db.cursor()

    os.remove('./中国每日新冠病毒阳性人数.html')
    data = myRead(cursor)
    run_charts(data)

    disconnect(db, cursor)

if __name__ == '__main__':
    updateTable()
    updateChart()
