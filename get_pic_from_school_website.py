import requests
import time
from processbar import processbar
url = 'http://202.120.126.33/pyxx/' \
      'PageTemplate/NsoftPage/yzm/createyzm.aspx?' \
      'Tue%20Dec%2011%202018%2011:45:39%20GMT+0800%20' \
      '(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)'
for i in range(100):
    fileName = 'C:\\Users\\56942\\Desktop\\验证码\\' + str(i+1) + '.bmp '
    r = requests.get(url)
    with open(fileName, 'wb') as f:
        f.write(r.content)
    time.sleep(0.2)
    processbar(i, 100)
