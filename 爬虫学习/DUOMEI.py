from selenium import webdriver
from time import sleep
import re

def baiduyunbaocun(yiyi, page=1, lastnum=100):
    if page == 1:
        first = 7  # 如果是第一页，忽略顶部的几个链接。
        lastnum = lastnum + 7
    else:
        first = 0
    if lastnum==100:  # 如果初始值是100，则使用yiyi长度
        lastnum = len(yiyi)
    else:
        lastnum = lastnum+1
    for web in yiyi[first:lastnum]:

        web.click()
        sleep(3)
        handles = bro.window_handles
        bro.switch_to.window(handles[1])
        sleep(2)
        tiqumafinda = bro.find_element_by_xpath('/html/body/div[8]/div[4]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div[2]/div/div[2]/table/tbody/tr/td').text
        tiquma = tiqumafinda.split('：')[-1]
        sleep(3)

       # 保存百度云网盘
        bro.find_element_by_xpath('/html/body/div[8]/div[4]/div[2]/div[1]/table/tbody/tr[1]/td[2]/div[2]/div/div[2]/table/tbody/tr/td/a').click()
        sleep(2)
        handles = bro.window_handles
        bro.switch_to.window(handles[2])
        try:
            bro.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/ul[1]/li[1]/div/span[1]').click()  # 点击选中所有文件

        except:
            bro.find_element_by_xpath('//*[@id="accessCode"]').send_keys(tiquma) # 输入提取码
            bro.find_element_by_xpath('//*[@id="submitBtn"]/a/span/span').click() # 点击进入
            sleep(2)
        else:
           continue

        finally:
            bro.find_element_by_class_name('zbyDdwb').click()
            sleep(2)
            bro.find_element_by_class_name('text').click() # 点击保存到我的百度网盘
            sleep(2)
            bro.find_element_by_class_name('g-button-blue-large').click()  # 点击确定
            sleep(5)
            bro.close()  # 关闭百度云界面
            print(tiquma)
            bro.switch_to.window(handles[1])
            bro.close()  # 关闭之前的页面
            bro.switch_to.window(handles[0])

# 登录界面url
url = "http://www.dmsy67.com/index.php"   # 此处输入duomei初始网址（就是刚进网站的页面）

option = webdriver.ChromeOptions()
option.add_argument(r'user-data-dir=C:\Users\14433\AppData\Local\Google\Chrome\User Data')  # 此处输入chrome的userdata地址，即你是用的chrome的地址

bro = webdriver.Chrome(executable_path=r'C:\Users\14433\Downloads\chromedriver_win32\chromedriver.exe', options=option)  # 此处填chromedriver.exe所在的地址，填在r''里。
bro.get(url=url) # 打开页面
# Iknow = bro.find_element_by_xpath('//*[@id="mianze_fixed"]/div[2]/a')
# Iknow.click()
sleep(5)
# username = bro.find_element_by_name('username') # 用户名标签定位
# password = bro.find_element_by_name('password') # 密码标签定位
# vdcode = bro.find_elements_by_class_name('px p_fre')[2] # 如果有验证码，验证码标签定位

# username.send_keys('cheshiresnake') # 输入用户名
# sleep(2)
# password.send_keys('WWW.SHIZHIYUAN13') # 输入密码
# login = bro.find_element_by_name('loginsubmit')
# login.click()  # 点击登录
'''模拟登录完成'''
# sleep(10)
# 顺序保存
jingpin = bro.find_element_by_xpath('/html/body/div[8]/div[3]/div[2]/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[1]/dl/dt/a')
jingpin.click()
sleep(2)
# tupianliulan = bro.find_element_by_class_name('chked')
# tupianliulan.click()  # 防止图片排列
# sleep(3)

# 找到当前页面的所有页面链接
pages = input('请输入想要保存的页数。')
lastnum = input('请输入最后一页需要保存的个数。如果最后一页需要全部保存，请输入0。')
pages, lastnum = eval(pages), eval(lastnum)
num = 0
page = 1
sleep(1)
while(page <= pages):

    yiyi = bro.find_elements_by_class_name('s.xst')
    if lastnum != 0 and page == pages:
        baiduyunbaocun(yiyi, page, lastnum)
    else:
        baiduyunbaocun(yiyi, page)

    sleep(2)
    # 点击下一页
    bro.execute_script("arguments[0].click();", bro.find_element_by_class_name('nxt'))
    page += 1  # page记录
    sleep(2)



