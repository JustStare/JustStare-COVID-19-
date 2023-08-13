from update import *

def dailyData(cursor, name, time):
    SQL = "select new_confirm, new_asymptom from pandemic" \
          "     where name = '%s', time = '%s';" % (name, time)
    cursor.execute(SQL)
    res = cursor.fetchone()

    return [res[0], res[1]]   # 返回的列表第一项为新增确诊，第二项为新增无症状
