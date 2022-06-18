## Sql with python
passd=input('enter password :')
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root' , passwd=passd)
curs=mydb.cursor()
print(mydb)

#BASICS Commands

def exc(CD):
    curs.execute(CD)

''' to execute command '''
def custom():
    exccute=input('mysq>')
    exc(exccute)
    show()

''' To show mysql '''
def show(default=curs):
    for i in curs:
        print(i)
    
''' to create DB  '''
def CTD():
    print('Enter name of database :')
    DBN=input()
    RUN='CREATE DATABASE ' + DBN
    exc(RUN)
    show()

while True:
    try:
        while True:
            custom()
    except:
        print('Some error occur try again')
