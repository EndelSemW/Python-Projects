import os
import sqlite3
from sqlite3 import Error

def Dbconnection():
    path="C:\\Users\\Reinaldo\\Documents\\Curso Python\\Aulas\\banco\\agenda.db"
    con=None
    try: 
        con=sqlite3.connect(path)
    except Error as ex:
        print(ex)
    return con

vcon=Dbconnection()

def Query(connection,sql):
    try:
        c=connection.cursor()
        c.execute(sql)
        connection.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operation has done sucessfully")
        #connection.close()

def Consult(connection, sql):
        c=connection.cursor()
        c.execute(sql)
        res=c.fetchall()
        #connection.close()
        return res
        
def MainMenu():
    os.system("cls")
    print("1 - Insert new registry")
    print("2 - Delete registry") #Preciso criar o ID do registro que eu quero deletar
    print("3 - Update registry")
    print("4 - Consult registry")
    print("5 - Consult registry name")
    print("6 - Exit")

def MenuInsert():
    os.system("cls")
    vname=input("Enter name: ")
    vnumber=input("Enter phone number: ")
    vemail=input("Enter email: ")
    vsql="INSERT INTO tb_contacts (T_CONTACTNAME, T_CONTACTNUMBER, T_CONTACTEMAIL) VALUES ('"+vname+"','"+vnumber+"','"+vemail+"')"
    Query(vcon,vsql)

def MenuDelete():
    os.system("cls")
    vID=input("Enter registry ID to be delete: ")
    vsql="DELETE FROM tb_contacts WHERE N_IDCONTACT="+vID
    Query(vcon,vsql)

def MenuUpdate():
    os.system("cls")
    vID=input("Enter registry ID to be update: ")
    r=Consult(vcon, "SELECT * FROM tb_contacts WHERE N_IDCONTACT="+vID)
    rname=r[0][1]
    rnumber=r[0][2]
    remail=r[0][3]
    vname=input("Enter name: ")
    vnumber=input("Enter phone number: ")
    vemail=input("Enter email: ")
    if(len(vname)==0):
        vname=rname
    if(len(vnumber)==0):
        vnumber=rnumber
    if(len(vemail)==0):
        vemail=remail
    vsql="UPDATE tb_contacts SET T_CONTACTNAME='"+vname+"', T_CONTACTNUMBER='"+vnumber+"', T_CONTACTEMAIL='"+vemail+"' WHERE N_IDCONTACT="+vID
    Query(vcon,vsql)

def MenuConsult():
    vsql="SELECT * FROM tb_contacts"
    res=Consult(vcon, vsql)
    vlim=10
    vcount=0
    for r in res:
         print("ID:{0:_<3} Name:{1:_<30} Phone:{2:_<14} E-mail:{3:_<30}".format(r[0],r[1],r[2],r[3]))
         vcount+=1
         if(vcount>=vlim):
             vcount=0
             os.system("pause")
             os.system("cls")
    print("End of list")
    os.system("pause")

def MenuConsultname():
    vname=input("Enter name: ")
    vsql="SELECT * FROM tb_contacts WHERE T_CONTACTNAME LIKE '%"+vname+"%'"
    res=Consult(vcon, vsql)
    vlim=10
    vcount=0
    for r in res:
         print("ID:{0:_<3} Name:{1:_<30} Phone:{2:_<14} E-mail:{3:_<30}".format(r[0],r[1],r[2],r[3]))
         vcount+=1
         if(vcount>=vlim):
             vcount=0
             os.system("pause")
             os.system("cls")
    print("End of list")
    os.system("pause")

opt=0
while opt !=6:
    MainMenu()
    opt=int(input("Type an option: "))
    if opt==1:
        MenuInsert()
    elif opt==2:
        MenuDelete()
    elif opt==3:
        MenuUpdate()
    elif opt==4:
        MenuConsult()
    elif opt==5:
        MenuConsultname()
    elif opt==6:
        os.system("cls")
        print("Finished program")
    else:
        os.system("cls")
        print("Invalid option")
        os.system("pause")
vcon.close
os.system("pause")

