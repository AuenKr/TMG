## Sql with python
passd=input('enter MySql password :')

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root' , passwd=passd)
curs=mydb.cursor()
print(mydb)
print()

#########################################

'''  TO SHOW COMMANDS  '''

def show(default=curs):
    for i in curs:
        print(i)


#########################################

def exc(CD):
    curs.execute(CD)
        
#########################################

''' to execute command '''
def custom():
    exccute=input('mysq>')
    exc(exccute)
    show()

    

##################################################################################################################

#create table Vehicle_detail,Own_detail ,Worker_detail ,Acident_detail

def create():
    
    Vehicle_detail='create table Vehicle_detail(Veh_no char(12) primary key ,Status char(8) NOT NULL ,Types varchar(12) ,Model varchar(40) ,Poll_cert varchar(40));'
    exc(Vehicle_detail)

    Own_detail='create table Own_detail(Veh_no char(12) primary key ,own_name varchar(45) not null ,Regi_date DATE NOT NULL);'
    exc(Own_detail)

    Work_detl='Create table Work_detl(Ser_no VARCHAR(12) Primary key ,Post char(10) ,Name varchar(40) NOT Null ,Current_Area varchar(30) NOT Null);'
    exc(Work_detl)

    Acident_detail='Create table Acident_detail(Veh_no char(12) primary key ,DOA DATE NOT NULL ,Details varchar(200));'
    exc(Acident_detail)

    USER='Create table user(USER_ID varchar(30) primary key ,PASSWD varchar(30) NOT NULL ,RANK varchar(15) NOT NULL ,NAME varchar(40) NOT NULL ,CONTACT_NO varchar(15) NULL ,ADDRESS varchar(60) NULL);'
    exc(USER)


##################################################################################################################

def GK():
    exc('use Traffic_manage;')
    gk='insert into user values("GOLDEN" ,"781048" ,"CAPTAIN" ,"GOLDEN KUMAR" ,"1234456789" ,"XYZ");'
    exc(gk)
    mydb.commit()

##################################################################################################################

#  create database Traffic_mangement  

try:
    exc('create database Traffic_manage;')
    exc('use Traffic_manage;')
    create()
    print('Installation Completed!!!')
    GK()
except:
    print('Do you want to reset database of Traffic Management.As database already exist??(Y/N)')
    a=input('-->')
    a=a.lower()
    if a in('yes','y'):
        exc('drop database Traffic_manage;')
        exc('create database Traffic_manage;')
        exc('use Traffic_manage;')
        create()
        GK()
    
        print('RESET COMPLETED!!!')
        
    elif a in ('no','n'):
        print('OK.......')

    else:
        print('Invalid Commanad')
    


input('Press any key to exit')
