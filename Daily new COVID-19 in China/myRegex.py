import re

patta = list()
patta.append("（.*?福建(\d+)例")
patta.append("（.*?浙江(\d+)例")
patta.append("（.*?江苏(\d+)例")
patta.append("（.*?广东(\d+)例")
patta.append("（.*?广西(\d+)例")
patta.append("（.*?江西(\d+)例")
patta.append("（.*?安徽(\d+)例")
patta.append("（.*?湖南(\d+)例")
patta.append("（.*?湖北(\d+)例")
patta.append("（.*?四川(\d+)例")
patta.append("（.*?陕西(\d+)例")
patta.append("（.*?河南(\d+)例")
patta.append("（.*?云南(\d+)例")
patta.append("（.*?贵州(\d+)例")
patta.append("（.*?青海(\d+)例")
patta.append("（.*?山东(\d+)例")
patta.append("（.*?山西(\d+)例")
patta.append("（.*?黑龙江(\d+)例")
patta.append("（.*?吉林(\d+)例")
patta.append("（.*?辽宁(\d+)例")
patta.append("（.*?内蒙古(\d+)例")
patta.append("（.*?宁夏(\d+)例")
patta.append("（.*?新疆(\d+)例")
patta.append("（.*?西藏(\d+)例")
patta.append("（.*?上海(\d+)例")
patta.append("（.*?北京(\d+)例")
patta.append("（.*?天津(\d+)例")
patta.append("（.*?重庆(\d+)例")
patta.append("（.*?海南(\d+)例")
patta.append("（.*?河北(\d+)例")
patta.append("（.*?甘肃(\d+)例")
patta.append("（.*?兵团(\d+)例")

patt_province_num = list()
patt_province_name = list()
for k in range(0, 32):
    tmp1 = re.compile(patta[k])
    patt_province_num.append(tmp1)
num_total = list()

def cope_confirm(text_list, prov_list):   # 处理确诊病例的函数
    patt_first_para = re.compile(".*?\n")
    # 存储第一段内容
    first_para = patt_first_para.findall(text_list)[0]
    patt_cf_all = re.compile("新增确诊病例(\d+)例")
    ls_cf_all = patt_cf_all.findall(first_para)
    if len(ls_cf_all) == 0:   # 全国无新增确诊病例
        num_total.append(0)
        num_total.append(0)
        for j in range(0, 32):
            prov_list[j].append(0)
    else:
        num_total.append(int(ls_cf_all[0]))

        # 新增本土确诊
        patt_cf_overseas = re.compile("新增确诊病例.+?均为境外输入.+?新增死亡病例")  # 判断是否均为境外输入
        ls_cf_overseas = patt_cf_overseas.findall(first_para)
        if len(ls_cf_overseas) == 0:  # 存在本土病例
            patt_cf_domestic1 = re.compile("新增确诊病例.+?本土病例(\d+)例")
            if len(patt_cf_domestic1.findall(first_para)) == 0:  # 格式二
                patt_cf_domestic2 = re.compile("新增确诊病例\d+?例.+?(\d+)例为境外输入病例")
                if len(patt_cf_domestic2.findall(first_para)) == 0:
                    patt_cf_domestic3 = re.compile("新增确诊病例\d+?例.+?(\d+)例为本土病例")
                    if len(patt_cf_domestic3.findall(first_para)) > 0:
                        numa = int(patt_cf_domestic3.findall(first_para)[0])
                    else:
                        numa = num_total[0]
                else:
                    numa = num_total[0] - int(patt_cf_domestic2.findall(first_para)[0])
            else:
                numa = int(patt_cf_domestic1.findall(first_para)[0])
            # 用cf_province来存储本土新增确诊内容，用于找出省份数据
            patt_cf_province = re.compile("新增确诊病例.+?本土病例.*?(（.+?）)")
            cf_province_list = patt_cf_province.findall(first_para)
            if len(cf_province_list) > 0:
                cf_province = cf_province_list[0]
                for j in range(0, 32):  # 遍历各个省份/地区的数据，遍历参数j
                    prov_tmp = patt_province_num[j].findall(cf_province)
                    if len(prov_tmp) == 0:  # 未找到该省份的新增确诊
                        prov_list[j].append(0)
                    else:
                        prov_list[j].append(int(prov_tmp[0]))
            else:
                numa = num_total[0]
                patt_t = re.compile("新增确诊病例.*?(（.+\d*.*?例）)，.*重症病例")
                str_tlist = patt_t.findall(first_para)
                if len(str_tlist) > 0:
                    str_t = str_tlist[0]
                    patt_t_t = re.compile("湖北.*?(\d+)例")
                    num_hubei_list = patt_t_t.findall(str_t)
                    if len(num_hubei_list) > 0:
                        num_hubei = int(patt_t_t.findall(str_t)[0])
                        for j in range(0, 8):
                            prov_list[j].append(0)
                        prov_list[8].append(num_hubei)
                        for j in range(9, 32):
                            prov_list[j].append(0)
                    else:
                        for j in range(0, 32):
                            prov_list[j].append(0)
                else:
                    for j in range(0, 32):
                        prov_list[j].append(0)
        else:  # 均为境外输入
            numa = 0
            for j in range(0, 32):
                prov_list[j].append(0)
        num_total.append(numa)

    return prov_list

def cope_asypmptom(text_list, prov_list):   # 处理无症状病例的函数
    patt_no_all = re.compile("新增无症状感染者(\d+)例")
    ls_no_all = patt_no_all.findall(text_list)
    if len(ls_no_all) > 0:   # 存在无症状感染者
        num_total.append(int(ls_no_all[0]))
        # 新增本土无症状
        # 用no_para存储无症状段落的字符串
        patt_no_para = re.compile("新增无症状感染者.+?\n")
        no_para = patt_no_para.findall(text_list)[0]   # 截取该段落
        patt_no_overseas = re.compile("新增无症状感染者.+?境外输入")
        ls_no_overseas = patt_no_overseas.findall(no_para)
        if len(ls_no_overseas) > 0:
            patt_no_all_overseas = re.compile("均为境外输入")
            ls4_no_all_overseas = patt_no_all_overseas.findall(ls_no_overseas[0])

            if len(ls4_no_all_overseas) == 0:  # 存在本土病例
                patt_none_overseas = re.compile("无境外输入")
                ls3_no_overseas = patt_none_overseas.findall(ls_no_overseas[0])
                if len(ls3_no_overseas) > 0:
                    num_total.append(int(ls_no_all[0]))
                else:
                    patt_no_domestic = re.compile("新增无症状感染者.+?境外输入.*?(\d+)例")
                    numb = num_total[2] - int(patt_no_domestic.findall(no_para)[0])  # 本土 = 全国 - 境外输入
                    num_total.append(numb)
                # 统计各省份本土新增无症状
                patt_no_province = re.compile("新增无症状感染者.+?境外输入.*?本土.*?(（.+）)")
                no_province = patt_no_province.findall(no_para)
                if len(no_province) > 0:
                    for j in range(0, 32):
                        prov_no_tmp = patt_province_num[j].findall(no_province[0])
                        if len(prov_no_tmp) == 0:
                            prov_list[j].append(0)
                        else:
                            prov_list[j].append(int(prov_no_tmp[0]))
                else:
                    for j in range(0, 32):
                        prov_list[j].append(0)
            else:
                num_total.append(0)
                for j in range(0, 32):
                    prov_list[j].append(0)
        else:
            num_total.append(0)
            for j in range(0, 32):
                prov_list[j].append(0)
    else:
        num_total.append(0)
        num_total.append(0)
        for j in range(0, 32):
            prov_list[j].append(0)

    return prov_list

def wash(myTime, prov_list):
    dictionary = dict()
    dictionary["日期"] = myTime
    dictionary['数据'] = list()
    for j in range(0, 31):  # 先不读取新疆生产兵团的数据
        dictionary["数据"].append({})
        dictionary["数据"][j]["name"] = prov_list[j][0]
        dictionary["数据"][j]["news"] = dict()
        dictionary["数据"][j]["news"]["新增确诊"] = prov_list[j][1]
        dictionary["数据"][j]["news"]["新增无症状"] = prov_list[j][2]
    # 合并新疆和生产兵团的数据
    dictionary["数据"][22]["news"]["新增确诊"] += prov_list[31][1]
    dictionary["数据"][22]["news"]["新增无症状"] += prov_list[31][2]

    return dictionary

def regex(myTime, myString):
    prov_list = [["福建"], ["浙江"], ["江苏"], ["广东"], ["广西"], ["江西"], ["安徽"], ["湖南"], ["湖北"], ["四川"],
                 ["陕西"], ["河南"], ["云南"], ["贵州"], ["青海"], ["山东"], ["山西"], ["黑龙江"], ["吉林"], ["辽宁"],
                 ["内蒙古"], ["宁夏"], ["新疆"], ["西藏"], ["上海"], ["北京"], ["天津"], ["重庆"], ["海南"], ["河北"],
                 ["甘肃"], ["兵团"]]
    cope_confirm(myString, prov_list)
    cope_asypmptom(myString, prov_list)
    myDict = wash(myTime, prov_list)
    return myDict
