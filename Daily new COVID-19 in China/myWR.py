def myWrite(db, cursor, myDict:dict):
    myTime = myDict['日期']
    for each in myDict['数据']:
        prov = each['name']
        newc = each['news']['新增确诊']
        newa = each['news']['新增无症状']
        SQL = "insert into pandemic(time, province, new_confirm, new_asymptom) value ('%s', '%s', %d, %d);" % (myTime, prov, newc, newa)
        cursor.execute(SQL)
        db.commit()

def myRead(cursor):
    SQL = 'use dslab;'
    cursor.execute(SQL)

    SQL = 'select time, province, new_confirm, new_asymptom from pandemic;'
    cursor.execute(SQL)
    result = cursor.fetchall()  # result是一个嵌套元组，相当于一个二维表

    data = list()
    newDay = dict()
    for j in range(0, len(result)):
        if (j % 31 == 0):  # 每31条数据代表1天
            newDay = dict()
            if (j > 0):
                data.append(newDay)
            time = result[j][0]
            newDay['time'] = time
            newDay['data'] = list()
            SQL = "select sum(new_confirm) from pandemic where time = '%s';" % time  # 查询当日总新增确诊人数，用于计算百分比
            cursor.execute(SQL)
            total = cursor.fetchone()[0]
        name = result[j][1]
        num_confirm = result[j][2]
        # num_asymptom = result[j][3]   # 无症状感染者
        if (total != 0):
            newProv = {
                'name': name,
                'value': [num_confirm, float(num_confirm) / float(total) * 100, name]
            }
        else:
            newProv = {
                'name': name,
                'value': [0, 0, name]
            }
        newDay['data'].append(newProv)

    return data
