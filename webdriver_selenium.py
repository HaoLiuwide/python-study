from selenium import webdriver
import time
from sendnail_to_me import sendmail_to_me
# import requests
# from PIL import Image, ImageEnhance
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains

# def xcode(fileName):
#    from PIL import Image
#    import pytesseract
#    image = Image.open(fileName)
#    sharp_img = ImageEnhance.Contrast(image).enhance(2.0)
#    sharp_img.load()  # 对比度增强
#    binary=sharp_img.convert('L')
#    threshold=90
#    table=[]
#    for i in range( 256 ):
#        if i < threshold:
#            table.append(0)
#        else :
#            table.append( 1 )
#    b=binary.point(table, "1")
#    b.save(fileName)
#    image_qz = Image.open(fileName)
#    image_qz = image.convert('RGB')
#    vcode = pytesseract.image_to_string(image_qz).strip()
#    return vcode

## 截取大图
# image= browser.find_element_by_xpath('//*[@id="myCode"]')
# browser.save_screenshot('page.png')
## 确定图片距离页面上部和左侧的大小
# left = image.location['x']
# top = image.location['y']
## 确定图片距离页面底部和右侧的大小
# right = left + image.size['width']
# bottom = top + image.size['height']
## 截图小图
# img = Image.open('page.png')
# img = img.crop((left, top, right, bottom))
# img.save('captcha.png')
# yzm=xcode("captcha.png")
# print(yzm)
# coding = utf-8


browser = webdriver.Chrome()
browser.get("http://202.120.126.33/pyxx/login.aspx")

input_user = browser.find_element_by_xpath('//*[@id="ctl00_txtusername"]')
input_user.send_keys("18721884")
time.sleep(1)

input_password = browser.find_element_by_xpath('//*[@id="ctl00_txtpassword"]')
input_password.send_keys("Liuhao123")
time.sleep(1)
yzm = input('请输入验证码：')
input_yzm = browser.find_element_by_xpath('//*[@id="ctl00_txtyzm"]')
input_yzm.send_keys(str(yzm))

button = browser.find_element_by_xpath('//*[@id="ctl00_ImageButton1"]')
button.click()
time.sleep(1)

browser.switch_to.frame("PageFrame")
judge_html_1 = browser.find_element_by_xpath('//*[@id="form1"]/div[3]/table/tbody/tr/td[1]/div/ul/li[3]/a/img')
judge_html_1.click()
judge_html_2 = browser.find_element_by_xpath('//*[@id="MainWork_dgData_LinkButton1_5"]/img')
judge_html_2.click()
for i in range(9):
    xph = '//*[@id="dltm_radlda_' + str(i) + '_0_' + str(i) + '"]'
    browser.find_element_by_xpath(xph).click()
browser.find_element_by_xpath('//*[@id="dltm_txtda_9"]').clear()
browser.find_element_by_xpath('//*[@id="dltm_txtda_9"]').send_keys('100')
time.sleep(1)
# browser.find_element_by_xpath('//*[@id="btnSumbit"]').click()
# # 从html页面切换到alert弹框
# alert = browser.switch_to.alert
# # 获取alert的文本内容
# print(alert.text)
# # 接受--选择“确定”
# alert.accept()
browser.back()
browser.back()


# xpath_of_judge = '//*[@id="MainWork_dgData_LinkButton1_' + str(n) + '"]/img'

# judge_html = browser.find_element_by_xpath('//*[@id="form1"]/div[3]/table/tbody/tr/td[1]/div/ul/li[3]/a/img')
# judge_html.click()
# judge_data = browser.find_elements_by_class_name('GridViewRowStyle')
# for i in range(len(judge_data)):
#     data_if = judge_data[i].text.strip().split(' ')[6]

# grade_html = browser.find_element_by_xpath('//*[@id="form1"]/div[3]/table/tbody/tr/td[1]/div/ul/li[2]/a/img ')
# grade_html.click()
# with open("compare.txt", 'r') as c:
#     existed_grade_number = c.read()
# Grades = browser.find_elements_by_class_name("GridViewRowStyle")
# Average_score = "平均分是" + browser.find_elements_by_id("MainWork_lblxwkpjcj")[0].text + "分"
# if str(len(Grades)) != existed_grade_number:
#     with open("compare.txt", 'w') as f:
#         f.write(str(len(Grades)))
#     data = Average_score + "\n"
#     for i in range(len(Grades)):
#         data = data + Grades[i].text.strip().split(' ')[1] + ' ' + Grades[i].text.strip().split(' ')[5] + '分\n'
#     sendmail_to_me('liuhao', data)
print('666')



