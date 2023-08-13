from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time
import re

option = ChromeOptions()
# option.add_argument("--headless")   # 无头模式的选择
option.add_experimental_option("excludeSwitches", ['enable-automation'])   # 关闭Chrome受到自动化测试的提示
option.add_experimental_option('useAutomationExtension', False)   # 关闭开发者模式
option.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')

option.add_argument("--disable-blink-features=AutomationControlled")
option.add_argument('blink-settings=imagesEnabled=false')   # 关闭图片的显示，提升响应速度
browser = webdriver.Chrome(options=option)

with open('./stealth.min.js') as f:   # 隐藏模拟浏览器的指纹特征，避开反爬虫机制
    js = f.read()
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': js
})

# # 反爬虫测试，保存结果截图为bypass_test.png
# browser.get('https://bot.sannysoft.com/')
# browser.save_screenshot("bypass_test.png")

def crawl_link(url_list, origin_link, nums):
    next_list = list()
    browser.get(origin_link)
    j = 0
    while j <= nums:
        time.sleep(1)   # 隐式等待
        lis = browser.find_elements(By.PARTIAL_LINK_TEXT, "截至")
        for i in lis:
            url_list.insert(0, i.get_attribute("href"))
            j += 1
        next_page_link_list = browser.find_elements(By.LINK_TEXT, "下一页")
        if len(next_page_link_list) == 0:
            break
        else:
            next_list.append(next_page_link_list[0].get_attribute("href"))
            browser.get(next_list[-1])

def crawl_content(db, cursor, urls, origin_link, nums):
    crawl_link(urls, origin_link, nums)
    SQL = 'use dslab'
    cursor.execute(SQL)
    for each in urls:
        dailyCrawl(db, cursor, each)

def dailyLink(origin):      # 爬取当日详情页的链接
    browser.get(origin)
    time.sleep(1)
    link_list = browser.find_elements(By.PARTIAL_LINK_TEXT, '截至')
    link = link_list[0].get_attribute("href")   # 取第一项

    return link

def dailyCrawl(db, cursor, Link):   # 爬取详情页内容
    browser.get(Link)
    time.sleep(1)
    # 显式等待
    content_list1 = browser.find_elements(By.XPATH, "/html/body/div[3]/div[2]/div[2]/span[1]")
    content_list2 = browser.find_elements(By.XPATH, "/html/body/div[3]/div[2]/div[3]")
    # 爬取时间，并做正则化处理
    str_tmp = content_list1[0].text
    patt_time = re.compile("\d+?-\d+?-\d+")
    myTime = patt_time.findall(str_tmp)[0]
    # 获取内容
    content = content_list2[0].text
    SQL = "insert into linktable(time, link) values ('%s', '%s')" % (myTime, Link)
    cursor.execute(SQL)
    db.commit()
    SQL = "insert into origincontent(time, content) values ('%s', '%s')" % (myTime, content)
    cursor.execute(SQL)
    db.commit()

    return myTime

if __name__ == '__main__':
    db = pymysql.connect(  # 链接数据库MySQL
        host="localhost",
        port=3306,
        user="root",
        password="5626168a.",
        charset="utf8mb4"
    )
    cursor = db.cursor()  # 创建游标对象

    origin = 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml'
    link = dailyLink(origin)
    print(f'链接为: {link}')
    thisTime = dailyCrawl(db, cursor, link)
    print(f'{thisTime}爬取完毕，成功存入数据库')
