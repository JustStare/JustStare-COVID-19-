from typing import List
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie, Line
import pyecharts.options as opts

### 需要做的只是更改下 data的格式 也就是注入 data
"""
data = [
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # data是 一个列表 包含多个字典 每天就是一个字典
    {

        # 字典中 时间的对应
        "time": "2020-01-01",
        # 字典中数据的对应 其中 data也是一个列表  此data不是那个data

        "data": [
            #     省份名称            数值      数值百分比（可以不写）   # 数值
            {"name": "广东", "value": [346.0, 10.12, "广东"]},
            {"name": "江苏", "value": [299.0, 8.75, "江苏"]},
            {"name": "山东", "value": [277.0, 8.08, "山东"]},
            {"name": "辽宁", "value": [201.0, 5.87, "辽宁"]},
            {"name": "浙江", "value": [192.0, 5.62, "浙江"]},
            {"name": "河北", "value": [169.0, 4.93, "河北"]},
            {"name": "河南", "value": [166.0, 4.84, "河南"]},
            {"name": "上海", "value": [151.0, 4.43, "上海"]},
            {"name": "四川", "value": [148.0, 4.34, "四川"]},
            {"name": "湖北", "value": [136.0, 3.87, "湖北"]},
            {"name": "湖南", "value": [124.0, 3.63, "湖南"]},
            {"name": "黑龙江", "value": [118.0, 3.5, "黑龙江"]},
            {"name": "福建", "value": [114.0, 3.25, "福建"]},
            {"name": "安徽", "value": [107.0, 3.03, "安徽"]},
            {"name": "北京", "value": [88.0, 2.59, "北京"]},
            {"name": "广西", "value": [87.0, 2.54, "广西"]},
            {"name": "云南", "value": [73.0, 2.28, "云南"]},
            {"name": "江西", "value": [73.0, 2.11, "江西"]},
            {"name": "吉林", "value": [79.0, 2.1, "吉林"]},
            {"name": "山西", "value": [60.0, 1.98, "山西"]},
            {"name": "陕西", "value": [68.0, 1.98, "陕西"]},
            {"name": "重庆", "value": [69.0, 1.78, "重庆"]},
            {"name": "天津", "value": [59.0, 1.57, "天津"]},
            {"name": "内蒙古", "value": [58.0, 1.57, "内蒙古"]},
            {"name": "新疆", "value": [49.0, 1.44, "新疆"]},
            {"name": "贵州", "value": [48.0, 1.22, "贵州"]},
            {"name": "甘肃", "value": [32.0, 1.09, "甘肃"]},
            {"name": "海南", "value": [20.0, 0.76, "海南"]},
            {"name": "青海", "value": [10.0, 0.32, "青海"]},
            {"name": "宁夏", "value": [14.0, 0.3, "宁夏"]},
            {"name": "西藏", "value": [3.0, 0.11, "西藏"]},
            {"name": "香港", "value": [12.0, 0.11, "香港"]},
            {"name": "台湾", "value": [3.0, 0.11, "台湾"]},
        ],
    },
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~·
    # 这是其中一个字典
    
    
    # data是 一个列表 包含多个字典 每天就是一个字典
    {

        # 字典中 时间的对应
        "time": "2020-01-02",
        # 字典中数据的对应 其中 data也是一个列表  此data不是那个data

        "data": [
            #     省份名称            数值      数值百分比（可以不写）   # 数值
            {"name": "广东", "value": [346.0, 10.12, "广东"]},
            {"name": "江苏", "value": [299.0, 8.75, "江苏"]},
            {"name": "山东", "value": [277.0, 8.08, "山东"]},
            {"name": "辽宁", "value": [201.0, 5.87, "辽宁"]},
            {"name": "浙江", "value": [1922.0, 5.62, "浙江"]},
            {"name": "河北", "value": [169.0, 4.93, "河北"]},
            {"name": "河南", "value": [166.0, 4.84, "河南"]},
            {"name": "上海", "value": [1511.0, 4.43, "上海"]},
            {"name": "四川", "value": [148.0, 4.34, "四川"]},
            {"name": "湖北", "value": [136.0, 3.87, "湖北"]},
            {"name": "湖南", "value": [124.0, 3.63, "湖南"]},
            {"name": "黑龙江", "value": [118.0, 3.5, "黑龙江"]},
            {"name": "福建", "value": [1134.0, 3.25, "福建"]},
            {"name": "安徽", "value": [107.0, 3.03, "安徽"]},
            {"name": "北京", "value": [88.0, 2.59, "北京"]},
            {"name": "广西", "value": [87.0, 2.54, "广西"]},
            {"name": "云南", "value": [73.0, 2.28, "云南"]},
            {"name": "江西", "value": [743.0, 2.11, "江西"]},
            {"name": "吉林", "value": [79.0, 2.1, "吉林"]},
            {"name": "山西", "value": [60.0, 1.98, "山西"]},
            {"name": "陕西", "value": [68.0, 1.98, "陕西"]},
            {"name": "重庆", "value": [69.0, 1.78, "重庆"]},
            {"name": "天津", "value": [59.0, 1.57, "天津"]},
            {"name": "内蒙古", "value": [58.0, 1.57, "内蒙古"]},
            {"name": "新疆", "value": [429.0, 1.44, "新疆"]},
            {"name": "贵州", "value": [48.0, 1.22, "贵州"]},
            {"name": "甘肃", "value": [32.0, 1.09, "甘肃"]},
            {"name": "海南", "value": [20.0, 0.76, "海南"]},
            {"name": "青海", "value": [105.0, 0.32, "青海"]},
            {"name": "宁夏", "value": [14.0, 0.3, "宁夏"]},
            {"name": "西藏", "value": [3.0, 0.11, "西藏"]},
            {"name": "香港", "value": [12.0, 0.11, "香港"]},
            {"name": "台湾", "value": [3.0, 0.11, "台湾"]},
        ],
    },
    # data是 一个列表 包含多个字典 每天就是一个字典
    {

        # 字典中 时间的对应
        "time": "2020-01-03",
        # 字典中数据的对应 其中 data也是一个列表  此data不是那个data

        "data": [
            #     省份名称            数值      数值百分比（可以不写）   # 数值
            {"name": "广东", "value": [346.0, 10.12, "广东"]},
            {"name": "江苏", "value": [2939.0, 8.75, "江苏"]},
            {"name": "山东", "value": [277.0, 8.08, "山东"]},
            {"name": "辽宁", "value": [201.0, 5.87, "辽宁"]},
            {"name": "浙江", "value": [192.0, 5.62, "浙江"]},
            {"name": "河北", "value": [169.0, 4.93, "河北"]},
            {"name": "河南", "value": [166.0, 4.84, "河南"]},
            {"name": "上海", "value": [1511.0, 4.43, "上海"]},
            {"name": "四川", "value": [148.0, 4.34, "四川"]},
            {"name": "湖北", "value": [136.0, 3.87, "湖北"]},
            {"name": "湖南", "value": [124.0, 3.63, "湖南"]},
            {"name": "黑龙江", "value": [118.0, 3.5, "黑龙江"]},
            {"name": "福建", "value": [114.0, 3.25, "福建"]},
            {"name": "安徽", "value": [107.0, 3.03, "安徽"]},
            {"name": "北京", "value": [88.0, 2.59, "北京"]},
            {"name": "广西", "value": [87.0, 2.54, "广西"]},
            {"name": "云南", "value": [731.0, 2.28, "云南"]},
            {"name": "江西", "value": [73.0, 2.11, "江西"]},
            {"name": "吉林", "value": [79.0, 2.1, "吉林"]},
            {"name": "山西", "value": [60.0, 1.98, "山西"]},
            {"name": "陕西", "value": [68.0, 1.98, "陕西"]},
            {"name": "重庆", "value": [69.0, 1.78, "重庆"]},
            {"name": "天津", "value": [592.0, 1.57, "天津"]},
            {"name": "内蒙古", "value": [58.0, 1.57, "内蒙古"]},
            {"name": "新疆", "value": [49.0, 1.44, "新疆"]},
            {"name": "贵州", "value": [48.0, 1.22, "贵州"]},
            {"name": "甘肃", "value": [32.0, 1.09, "甘肃"]},
            {"name": "海南", "value": [20.0, 0.76, "海南"]},
            {"name": "青海", "value": [130.0, 0.32, "青海"]},
            {"name": "宁夏", "value": [14.0, 0.3, "宁夏"]},
            {"name": "西藏", "value": [3.0, 0.11, "西藏"]},
            {"name": "香港", "value": [142.0, 0.11, "香港"]},
            {"name": "台湾", "value": [3.0, 0.11, "台湾"]},
        ],
    },
    # data是 一个列表 包含多个字典 每天就是一个字典
    {

        # 字典中 时间的对应
        "time": "2020-01-04",
        # 字典中数据的对应 其中 data也是一个列表  此data不是那个data

        "data": [
            #     省份名称            数值      数值百分比（可以不写）   # 数值
            {"name": "广东", "value": [3146.0, 10.12, "广东"]},
            {"name": "江苏", "value": [299.0, 8.75, "江苏"]},
            {"name": "山东", "value": [277.0, 8.08, "山东"]},
            {"name": "辽宁", "value": [201.0, 5.87, "辽宁"]},
            {"name": "浙江", "value": [192.0, 5.62, "浙江"]},
            {"name": "河北", "value": [1369.0, 4.93, "河北"]},
            {"name": "河南", "value": [166.0, 4.84, "河南"]},
            {"name": "上海", "value": [151.0, 4.43, "上海"]},
            {"name": "四川", "value": [148.0, 4.34, "四川"]},
            {"name": "湖北", "value": [136.0, 3.87, "湖北"]},
            {"name": "湖南", "value": [124.0, 3.63, "湖南"]},
            {"name": "黑龙江", "value": [118.0, 3.5, "黑龙江"]},
            {"name": "福建", "value": [114.0, 3.25, "福建"]},
            {"name": "安徽", "value": [1207.0, 3.03, "安徽"]},
            {"name": "北京", "value": [88.0, 2.59, "北京"]},
            {"name": "广西", "value": [87.0, 2.54, "广西"]},
            {"name": "云南", "value": [732.0, 2.28, "云南"]},
            {"name": "江西", "value": [73.0, 2.11, "江西"]},
            {"name": "吉林", "value": [79.0, 2.1, "吉林"]},
            {"name": "山西", "value": [60.0, 1.98, "山西"]},
            {"name": "陕西", "value": [68.0, 1.98, "陕西"]},
            {"name": "重庆", "value": [69.0, 1.78, "重庆"]},
            {"name": "天津", "value": [539.0, 1.57, "天津"]},
            {"name": "内蒙古", "value": [58.0, 1.57, "内蒙古"]},
            {"name": "新疆", "value": [49.0, 1.44, "新疆"]},
            {"name": "贵州", "value": [48.0, 1.22, "贵州"]},
            {"name": "甘肃", "value": [32.0, 1.09, "甘肃"]},
            {"name": "海南", "value": [20.0, 0.76, "海南"]},
            {"name": "青海", "value": [10.0, 0.32, "青海"]},
            {"name": "宁夏", "value": [14.0, 0.3, "宁夏"]},
            {"name": "西藏", "value": [35.0, 0.11, "西藏"]},
            {"name": "香港", "value": [12.0, 0.11, "香港"]},
            {"name": "台湾", "value": [213.0, 0.11, "台湾"]},
        ],
    },

]
"""
time_list = []
total_num = []

maxNum = 500
minNum = 0
def create_total(data):
    global total_num,time_list
    for one_dic in data:
        num = 0
        time_list.append(one_dic["time"])
        for one_data in one_dic["data"]:
            value = one_data["value"][0]
            num = num+value
        total_num.append(num)



def get_year_chart(day: str,data):
    map_data = [
        [[x["name"], x["value"]] for x in d["data"]] for d in data if d["time"] == day
    ][0]
    min_data, max_data = (minNum, maxNum)
    data_mark: List = []
    i = 0
    for x in time_list:
        if x == day:
            data_mark.append(total_num[i])
        else:
            data_mark.append("")
        i = i + 1

    map_chart = (
        Map()
            .add(
            series_name="",
            data_pair=map_data,
            zoom=1,
            center=[119.5, 34.5],
            is_map_symbol_show=False,
            itemstyle_opts={
                "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                "emphasis": {
                    "label": {"show": Timeline},
                    "areaColor": "rgba(255,255,255, 0.5)",
                },
            },
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="" + str(day) + "当日 数据来源：卫健委",
                subtitle="",
                pos_left="center",
                pos_top="top",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=25, color="rgba(255,255,255, 0.9)"
                ),
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                formatter=JsCode(
                    """function(params) {
                    if ('value' in params.data) {
                        return params.data.value[2] + ': ' + params.data.value[0];
                    }
                }"""
                ),
            ),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="30",
                pos_top="center",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )

    line_chart = (
        Line()
            .add_xaxis(time_list)
            .add_yaxis("", total_num)
            .add_yaxis(
            "",
            data_mark,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="中国每日新冠病毒阳性人数", pos_left="72%", pos_top="5%"
            )
        )
    )
    bar_x_data = [x[0] for x in map_data]
    bar_y_data = [{"name": x[0], "value": x[1][0]} for x in map_data]
    bar = (
        Bar()
            .add_xaxis(xaxis_data=bar_x_data)
            .add_yaxis(
            series_name="",
            y_axis=bar_y_data,
            label_opts=opts.LabelOpts(
                is_show=True, position="right", formatter="{b} : {c}"
            ),
        )
            .reversal_axis()
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                max_=maxNum, axislabel_opts=opts.LabelOpts(is_show=False)
            ),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="10",
                pos_top="top",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )

    pie_data = [[x[0], x[1][0]] for x in map_data]
    pie = (
        Pie()
            .add(
            series_name="",
            data_pair=pie_data,
            radius=["15%", "35%"],
            center=["80%", "82%"],
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=1, border_color="rgba(0,0,0,0.3)"
            ),
        )
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{b} {d}%"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )

    grid_chart = (
        Grid()
            .add(
            bar,
            grid_opts=opts.GridOpts(
                pos_left="10", pos_right="45%", pos_top="50%", pos_bottom="5"
            ),
        )
            .add(
            line_chart,
            grid_opts=opts.GridOpts(
                pos_left="65%", pos_right="80", pos_top="10%", pos_bottom="50%"
            ),
        )
            .add(pie, grid_opts=opts.GridOpts(pos_left="45%", pos_top="60%"))
            .add(map_chart, grid_opts=opts.GridOpts())
    )

    return grid_chart


def run_charts(data):
    create_total(data)
    timeline = Timeline(
        init_opts=opts.InitOpts(width="1530px", height="675px", theme=ThemeType.DARK)
    )
    # print(time_list)

    for y in time_list:
        g = get_year_chart(day=y,data=data)
        timeline.add(g, time_point=str(y))

    timeline.add_schema(
        orient="vertical",
        is_auto_play=True,
        is_inverse=True,
        play_interval=3000,
        pos_left="null",
        pos_right="5",
        pos_top="20",
        pos_bottom="20",
        width="60",
        label_opts=opts.LabelOpts(is_show=True, color="#fff"),
    )

    timeline.render("中国每日新冠病毒阳性人数.html")
# if __name__ == '__main__':
#     run_charts(data)

# 在使用的时候 使用run_charts  这个函数
# 其中参数就是data
# data的具体格式 开始日期 和结束日期都由你注入
# 不一定要全年 可能 有2022-6-01 到现在也是可以
