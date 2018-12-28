#!/usr/bin/env python
#-*-coding:utf-8-*-
#AUTH:mingju.xu
#DATE:18-12-28
from splinter.browser import Browser
from time import sleep
# traceback模块被用来跟踪异常返回信息
import traceback
# 设定用户名、密码
username = input("用户名：")
passwd = input("密码：")
# 起始站点和乘车时间的cookies值要去找；
# 方法：先登录一下12306，输入地点日期什么的查询一下，然后在chrome浏览器中按F12，出现如下页面，在Application选项里找到相应的值。
# 表格中的cookie值：
#_jc_save_fromeStation的值为出发地
#_jc_save_toSatation的值为目的地
#_jc_save_fromDate 出发日期
#_jc_save_toDate返程日期
# 实例中用的是：上海 到 洛阳 2019-01-29
from_station = u"%u4E0A%u6D77%2CSHH"
to_station = u"%u6D1B%u9633%2CLYF"
# 时间格式2018-01-25
from_date = u"2019-01-10"
# 车次，选择第几趟，0则从上之下依次点击
order = 0
# 设定乘客姓名
ticketer = input("乘客：")
# 设定网址
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
login_url = "https://kyfw.12306.cn/otn/login/init"
initmy_url = "https://kyfw.12306.cn/otn/view/index.html"

# 登录网站
def login():
    #点击当前页面的"登录"
#    bwr.find_by_text(u"login").click()
#    sleep(3)
    #fill填充搜索框的内容，username。name=loginUserDTO.user_name的元素。
    bwr.fill("loginUserDTO.user_name", username)
    sleep(1)
    bwr.fill("userDTO.password", passwd)
    sleep(1)
    print(u"等待验证码，自行输入...")
    #登录手动输入验证码，并登录系统
    while True:
        #判断当前的url是否已经进入系统
        if bwr.url != initmy_url:
            sleep(1)
        else:
            break
# 购票
def getTickt():
    global bwr
    # 使用splinter打开chrome浏览器
    bwr=Browser(driver_name="chrome")
    # splinter打开浏览器（返回购票页面）
    bwr.visit(login_url)
    while bwr.is_text_present(u"登录"):
        sleep(1)
        login()
        #判断是否已经进入系统
        if bwr.url == initmy_url:
            break
    try:
        print(u"购票页面...")
        # splinter打开浏览器（跳回购票页面）
        bwr.visit(ticket_url)
        # 加载查询信息
        bwr.cookies.add({"_jc_save_fromStation": from_station})
        bwr.cookies.add({"_jc_save_toStation": to_station})
        bwr.cookies.add({"_jc_save_fromDate": from_date})
        bwr.reload()
        sleep(2)
        count=0
        # 循环点击预订
        if order != 0:
            while bwr.url == ticket_url:
                bwr.find_by_text(u"查询").click()
                count += 1
                print(u"循环点击查询... 第 %s 次" % count)
                sleep(2)
                try:
                    bwr.find_by_text(u"预订")[order - 1].click()
                except:
                    print(u"还没开始预订")
                    continue
        else:
            while bwr.url == ticket_url:
                 bwr.find_by_text(u"查询").click()
                 count += 1
                 print(u"循环点击查询... 第 %s 次" % count)
                 sleep(1)
                 try:
                     for i in bwr.find_by_text(u"预订"):
                         i.click()
                         sleep(1)
                 except:
                     print(u"还没开始预订")
                     continue
        sleep(1.5)
        bwr.find_by_text(ticketer).last.click()
        sleep(1.5)
        bwr.find_by_id(u"submitOrder_id").click()
        sleep(1.5)
        bwr.find_by_id(u"qr_submit_id").click()
        print(u"成功抢到一张宝贵的票")
    except Exception as e:
         print(traceback.print_exc())

if __name__ == "__main__":
    getTickt()