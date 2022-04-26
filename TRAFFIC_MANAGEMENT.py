import mysql.connector
PASSWORD=input('ENTER MYSQL PASSWORD :')

mydb=mysql.connector.connect(host='localhost' ,user='root' ,password=PASSWORD)
curs=mydb.cursor()
print(mydb)

## SQL FUCTIONS ##
# to retrive data from sql #
def show(default=curs):
    count=0
    for i in curs:
        print(i)
        count+=1
    if count==0:
        print('NOT FOUND')
    print()
    
def show2(default=curs):
    for i in curs:
        print(i)

# to execute input command #
def exc1(CD):
    curs.execute(CD)
    mydb.commit()

def exc(CD):
    curs.execute(CD)
    

g='use traffic_manage;'
exc(g)    


# to execute custom command #

def custom():
    while True:
        exccute=input('mysq>')
        exc(exccute)
        show()
        

# To get all data stored in SQL #

def fetch():
    d='use traffic_manage;'
    exc(d)


    d2='select * from vehicle_detail;'
    exc(d2)
    print("%s\t %s\t %s\t %s\t %s\t"%("Veh_no","Status","Type","Model","Poll_cer"))
    for i in curs:        
        print('%s\t '%str(i))
        print()
    print('______________________________________________________________________________')
    print()
    
    d3='select * from own_detail;'
    exc(d3)
    print("%s\t %s\t %s\t"%("Veh_no","Own_name","Regi_date"))
    for i in curs:        
        print('%s\t '%str(i))
        print()
    print('_______________________________________________________________________________')
    print()
    

    d4='select * from work_detl;'
    exc(d4)
    print("%s \t %s\t %s\t %s\t"%("Ser_no","Post","Name","Current_Area"))
    for i in curs:        
        print('%s\t '%str(i))
        print()
    print('______________________________________________________________________________')
    print()

# Insert data into SQL#

def VDE():
    print('          VEHICLE DATA ENTRY   ')
    print()        
    veh_no=input('Enter Vehical no : ')

    own_name=input('Enter Ownner name : ')

    status=input('Enter Status(Active /Inactive) : ')

    regi_date=input('Enter Registration date(YY/MM/DD) :')

    Type=input('Enter vehical type(car/truck/motorcycle) :')

    model=input('Enter model of vehicle(full detail) :')

    poll=input('Enter pollution certificate(Y/N) :')
    
    g1='Insert into Vehicle_detail VALUES("'+veh_no+'" ,"'+status+'" ,"'+Type+'" ,"'+model+'" ,"'+poll+'") ;'

    g2='Insert into Own_detail VALUES("'+veh_no+'" ,"'+own_name+'" ,"'+regi_date+'") ;'     
    exc1(g1)
    exc1(g2)
    print('DATA UPLOADED')
    
def WDE():
    print('         WORKER DATA ENTRY ')
    print()         
    ser_no=input('Enter Service No :')

    name=input('Enter full name :')

    post=input('Enter post :')

    curr_area=input('Enter Current working area :')

    g1='Insert into work_detl VALUES('+ser_no+' ,"'+post+'" ,"'+name+'" ,"'+curr_area+'") ;'
    
    exc1(g1)
    print('DATA UPLOADED')
    
def ADE():
    print('         ACCIDENT DATA ENTRY   ')
    print()
    veh_no=input('Enter Vehicle No. : ')

    DOA=input('Enter Date Of Acident (YY/MM/DD) : ')

    print('Enter detail of Accident :')
    detail=input()

    g1='Insert into ACIDENT_DETAIL VALUES("'+veh_no+'" ,"'+DOA+'" ,"'+detail+'") ;'
    
    exc1(g1)
    print('DATA UPLOADED')

## UPDATE DATA ENTRY ##

def UVD():
    VEH_NO=input('Enter Vehicle NO. to which data has to update :')
    print('          VEHICLE DATA UPDATE   ')
    print('1.Vehical No.')
    print('2.Ownner Name')
    print('3.Status')
    print('4.Registration Date')
    print('5.Vehicle Type')
    print('6.Vehicle Model')
    print('7.Pollution Certificate ')
    print()

    ch=int(input('Enter the serial no of Field in which you want to update Data  : '))
            
    if ch==1:

        veh_no=input('Enter Vehical no : ')
        g1='UPDATE VEHICLE_DETAIL SET VEH_NO="'+veh_no+'" where Veh_no="'+VEH_NO+'";'
        g2='UPDATE OWN_DETAIL SET VEH_NO="'+veh_no+'" where Veh_no="'+VEH_NO+'";'

        exc1(g1)
        exc1(g2)

    elif ch==2:

        own_name=input('Enter Ownner name : ')
        g2='UPDATE OWN_DETAIL SET own_name="'+own_name+'" where Veh_no="'+VEH_NO+'";'
        exc1(g2)

    elif ch==3:

        status=input('Enter Status(Active /Inactive) : ')
        g1='UPDATE VEHICLE_DETAIL SET Status="'+status+'" where Veh_no="'+VEH_NO+'";'
        exc1(g1)
                
    elif ch==4:

        regi_date=input('Enter Registration date(YY/MM/DD) :')
        g2='UPDATE OWN_DETAIL SET Regi_date="'+veh_no+'" where Veh_no="'+VEH_NO+'";'
        exc1(g2)
        
    elif ch==5:

        Type=input('Enter vehical type(car/truck/motorcycle) :')
        g1='UPDATE VEHICLE_DETAIL SET Types="'+Type+'" where Veh_no="'+VEH_NO+'";'
        exc1(g1)                

    elif ch==6:

        model=input('Enter model of vehicle(full detail) :')
        g1='UPDATE VEHICLE_DETAIL SET Model="'+model+'" where Veh_no="'+VEH_NO+'";'
        exc1(g1)

    elif ch==7:

        poll=input('Enter pollution certificate(Y/N) :')
        g1='UPDATE VEHICLE_DETAIL SET Poll_cert="'+poll+'" where Veh_no="'+VEH_NO+'";'
        exc1(g1) 

    else:

        print('!!! PLEASE ENTER FROM ABOVE FIELD ONLY !!!')
                

    print('DATA UPDATED')


def UWD():
    SER_NO=input('ENTER SERVICE NO. OF WORKER :')
             
    print('         WORKER DATA UPDATE ')
    print()
    print('1.Service No')
    print('2.Name')
    print('3.Post')
    print('4.Current Working Area')
    print()

    ch=int(input('Enter the serial no of Field in which you want to update Data  : '))
            
    if ch==1:

        ser_no=input('Enter Service No :')
        g1='UPDATE WORK_DETL SET Ser_no="'+ser_no+'" where Ser_no="'+SER_NO+'";'
        exc1(g1)
                
    elif ch==2:

        name=input('Enter full name :')
        g1='UPDATE WORK_DETL SET Name="'+name+'" where Ser_no="'+SER_NO+'";'
        exc1(g1)
                
    elif ch==3:

        post=input('Enter post :')
        g1='UPDATE WORK_DETL SET Post="'+post+'" where Ser_no="'+SER_NO+'";'
        exc1(g1)
                
    elif ch==4:

        curr_area=input('Enter Current working area :')
        g1='UPDATE WORK_DETL SET Current_Area="'+curr_area+'" where Ser_no="'+SER_NO+'";'
        exc1(g1)

    else:

        print('!!! PLEASE ENTER FROM ABOVE SERIAL NO. ONLY !!!')
    print()
    print('DATA UPLOADED')

def UAD():
    VEH_NO=input('Enter Vehicle No. for which Data has To Update : ')
            
    print('         ACCIDENT DATA UPDATE   ')
    print()
    print('1.Vehicle No. ')
    print('2.Date Of Acident ')
    print('3.Details ')
    print()
    ch=int(input('Enter the serial no of Field in which you want to update Data  : '))

    if ch==1:

        veh_no=input('Enter Vehicle No. : ')
        g1='UPDATE ACIDENT_DETAIL SET Veh_no="'+veh_no+'" where Veh_no="'+VEH_NO+'";'
        exc1(g1)
                
    elif ch==2:

        DOA=input('Enter Date Of Acident (YY/MM/DD) : ')
        g1='UPDATE ACIDENT_DETAIL SET DOA="'+DOA+'" where Veh_no="'+VEH_NO+'";'
        exc1(g1)
                
    elif ch==3:

        print('Enter Details :')
        detail=input()
        g1='UPDATE ACIDENT_DETAIL SET Details="'+detail+'" where Veh_no="'+VEH_NO+'";'
        exc1(g1)
        
    else:

        print('!!! PLEASE ENTER FROM ABOVE SERIAL NO. ONLY !!!')

    print()
    print('DATA UPDATED')

def DVD():
    print()
    print('****WARNING : THIS WILL DELETE ALL DATA RELATED TO VEHICLE AND OWNNER ')
    print()
    VEH_NO=input('Enter Vehicle NO. to which data has TO DELETE :')
    g1='DELETE FROM VEHICLE_DETAIL WHERE VEH_NO="'+VEH_NO+'";'
    g2='DELETE FROM OWN_DETAIL WHERE VEH_NO="'+VEH_NO+'";'

    exc1(g1)
    exc1(g2)
           
    print('DATA DELETED')

def DWD():
    print()
    print('****WARNING : THIS WILL DELETE ALL DATA RELATED TO WORKER')
    print()

    SER_NO=input('ENTER SERVICE NO. OF WORKER TO WHICH DATA HAS TO DELETE :')

    g1='DELETE FROM WORK_DETL WHERE SER_NO="'+SER_NO+'";'
            
    exc1(g1)
    print('DATA DELETED')

def DAD():
    print()
    print('****WARNING : THIS WILL DELETE ALL DATA RELATED TO ACCIDENT OF VEHICLE ')
    print()
    VEH_NO=input('Enter Vehicle No. for which Data has To DELETE ABOUT ACCIDENT: ')

    g1='DELETE FROM ACIDENT_DETAIL WHERE VEH_NO="'+VEH_NO+'";'
            
    exc1(g1)
    print('DATA DELETED')

#############################################################################################

## GETTING DETAILS SECTOR ##

def VDETAIL():
    no=input('Enter Vehicle No  TO Search : ')

    d='Select VH.VEH_NO ,OWN_NAME ,REGI_DATE ,STATUS ,TYPES ,MODEL ,POLL_CERT from vehicle_detail AS vh,own_detail as ow where vh.veh_no = ow.veh_no and ow.veh_no="'+no+'";'
      
    exc(d)
    show()
    
def WDETAIL():
    no=input('Enter Service No TO Search : ')

    d='Select * from work_detl where Ser_no="'+no+'";'

    exc(d)
    show()
    
def ADETAIL():
    tot='Select count(Veh_no) from acident_detail;'
    
    print('Total no of accident :')
    exc(tot)
    show()

    no=input('Enter Vehicle No To Search : ')

    d='Select * from acident_detail where veh_no="'+no+'";'

    exc(d)
    show()

# secarch details #

def search():
    print('1.Vehical detail')
    print('2.worker detail ')
    print('3.accident detail')
    I=int(input('Which detail you want ? '))

    if I==1:
       print(      '   Vehical Details ') 
       print('Which of the following do you know about vehical ???')
       print('1.vehical no.')
       print('2.owner name')
       print('3.model')
       print('4.Vehicle type')
       print('5.Show all')
       i=int(input('What do you Know about Vehicle ? Enter your Choice :'))
       if i==1:
           en=input('Enter Vehicle No To Search :')
           ex='Select * from vehicle_detail as vh,own_detail as ow where vh.veh_no=ow.veh_no and ow.veh_no="'+en+'"  ;'
           exc(ex)
           show()

       elif i==2:
           en=input('Enter OWNER NAME To Search :')
           ex='Select * from vehicle_detail as vh,own_detail as ow where vh.veh_no=ow.veh_no and ow.Own_name="'+en+'" ;'
           exc(ex)
           show()
       elif i==3:
           en=input('Enter model To Search :')
           ex='Select * from vehicle_detail as vh,own_detail as ow where vh.veh_no=ow.veh_no and vh.model="'+en+'" ;'
           exc(ex)
           show()

       elif i==4:
           en=input('Enter Vehicle Type To Search :')
           ex='Select * from vehicle_detail as vh,own_detail as ow where vh.veh_no=ow.veh_no and vh.types="'+en+'" ;'
           exc(ex)
           show()
       elif i==5:
           ex='Select * from vehicle_detail as vh,own_detail as ow where vh.veh_no=ow.veh_no;'
           exc(ex)
           show()

       else:
           print('!!! PLEASE SELECT FROM ABOVE SERIAL ONLY !!!')

    elif I==2:
        print('1.Service No. ')
        print('2.Post')
        print('3.Name')
        print('4.Current Working Detail')

        i=int(input('What do you Know about Worker ? Enter your Choice :'))

        if i==1:
            no=input('Enter Service No TO Search : ')
            d='Select * from work_detl where Ser_no='+no+' ;'
            exc(d)
            show()

        elif i==2:
            post=input('Enter POST TO Search : ')
            d='Select * from work_detl where Post="'+post+'" ;'
            exc(d)
            show()

        elif i==3:
            name=input('Enter NAME TO Search : ')
            d='Select * from work_detl where name="'+name+'" ;'
            exc(d)
            show()

        elif i==4:
            CWA=input('Enter Current Working Area TO Search  : ')
            d='Select * from work_detl where Current_Area="'+CWA+'" ;'
            exc(d)
            show()

        else:
            print('!!! PLEASE SELECT FROM ABOVE SERIAL ONLY !!!')

    elif I==3:
        print('1.VEHICLE NO. ')
        print('2.Date Of Accident(DOA) ')

        i=int(input('What do you Know about Accident ? Enter your Choice :'))

        if i==1:
            ADETAIL()

        elif i==2:
            DOA=input('Enter Date Of Accident(DOA) TO Search :')
            ex="Select * from vehicle_detail as vh,acident_detail as ad where vh.veh_no=ad.Veh_no and ad.DOA='"+DOA+"' ;"
            exc(ex)
            show()

        else:
            print('!!! PLEASE SELECT FROM ABOVE SERIAL ONLY !!!')

    else:
        print('!!! ENTER FROM ABOVE SERIAL NO ONLY !!!  ')

################################################################################################################################################################################################
def MSECTOR():
    
    print('                     WELCOME TO MANAGEMENT SECTOR ')
    print()
    print('1.Add Data ')
    print('2.Update Data ')
    print('3.Delete Data ')
    print('4.Show All Data')
    print()
    IN=int(input('Enter your choice :'))

    if IN==1:
        print('                DATA ENTRY SECTOR ')
        input()
        print('1.Vehical detail ')
        print('2.worker detail ')
        print('3.accident detail ')
        print()

        print('Enter the serial no of sector in which you want to ADD Data :')
        pk=int(input())
        if pk==1:
            VDE()

        elif pk==2:
            WDE()

        elif pk==3:
            ADE()

        else:
             print('PLEASE ENTER FROM ABOVE SERIAL NO.')
            


    elif IN==2:
        print('    DATA UPDATING SECTOR')
        
        print('1.Vehical detail ')
        print('2.worker detail ')
        print('3.accident detail ')
        print()

        print('Enter the serial no of sector in which you want to update Data : ')

        pk=int(input())

        if pk==1:
            UVD()
                
        elif pk==2:
            UWD()

        elif pk==3:
            UAD()

        else:
            print(' PLEASE ENTER FROM ABOVE SERIAL NO. ')

    elif IN==3:
        print('    DATA DELETING SECTOR ')
            
        print('1.Vehical Detail ')
        print('2.Worker Detail ')
        print('3.Accident Detail ')
        print()

        print('Enter the serial no of sector in which you want to update Data : ')

        pk=int(input())

        if pk==1:
            DVD()

        elif pk==2:
            DWD()

        elif pk==3:
            DAD()

        else:
            print(' PLEASE ENTER FROM ABOVE SERIAL NO. ')
                

    elif IN==4:
        fetch()


######################################################################################
#                                                                                   ##                      
#           INITIATING PROGRAM                                                      ##
#                                                                                   ##
######################################################################################        
def main():
    print()
    print('     welcome  to  Traffic Management              ')
    print()

    print('1.Vehicle Details ')
    print()
    print('2.Worker Details  ')
    print()
    print('3.Accient Details  ')
    print()
    print('4.Search Details  ')
    print()
    print('5.Management Sector(For ADMINS)  ')
    print()


    c=int(input('Enter your choice :'))

    if c==1:
        while True:
            VDETAIL()
            print('DO YOU WANT TO GO TO PREVIOUS MENU?(YES/NO) :')
            ch=input()
            if ch in ('yes','YES','y'):
                break

        
    elif c==2:
        while True:
            WDETAIL()
            print('DO YOU WANT TO GO TO PREVIOUS MENU?(YES/NO) :')
            ch=input()
            if ch in ('yes','YES','y'):
                break
        
    elif c==3:
        while True:
            ADETAIL()
            print('DO YOU WANT TO GO TO PREVIOUS MENU?(YES/NO) :')
            ch=input()
            if ch in ('yes','YES','y'):
                break

        
    elif c==4:
        while True:
            search()
            print('DO YOU WANT TO GO TO PREVIOUS MENU?(YES/NO) :')
            ch=input()
            if ch in ('yes','YES','y'):
                break

        
    elif c==5:
        P=input('Enter password : ')
        CP='LEGENDS'
        if P==CP:
            while True:
                MSECTOR()
                print('DO YOU WANT TO GO TO PREVIOUS MENU?(YES/NO) :')
                ch=input()
                if ch in ('yes','YES','y'):
                    break
        else:
            print('WRONG PASSWORD')
  

while True:
    main()
    print('DO YOU WANT EXIT?(YES/NO) :')
    ch=input()
    if ch in ('yes','YES','y'):
        exit()


###########################################################################################################################################################################################################################################################################################
##                 TTTTTT  HH  HH   EEEEEE         EEEEEE  NN   NN  DDDDD                                       ###
##                   TT    HH  HH   EE             EE      NNN  NN  DD  DD                                      ###
##                   TT    HHHHHH   EEEE           EEEE    NN N NN  DD   DD                                     ###
##                   TT    HH  HH   EE             EE      NN  NNN  DD  DD                                      ###
##                   TT    HH  HH   EEEEEE         EEEEEE  NN   NN  DDDDD                                       ###
###########################################################################################################################################################################################################################################################################################
