from cgitb import text
from tkinter import *
import os
os.system('cls')

a=os.path.dirname(__file__)
filename=a+"\\names.txt"

def writeData():
    file=open(filename,"a")
    file.write("Local........:%s" % vname.get())
    file.write("\nPhone number.:%s" % vphone.get())
    file.write("\nFlavours.....:%s" % vf.get())
    file.write("\nOBS..........:%s" % vt.get("1.0", END))
    file.write("\n")
    file.close()

app=Tk()
app.title("Açaí Endel")
app.geometry("600x400")
app.configure(bg="#dde")

#Anchor=> N=Norte, S=Sul, E=Leste, W=Oeste
#SE=Sudeste, NE= Nordeste, SW=Sudoeste, NW= Noroeste
Label(app,text="Local", bg="#dde", fg="#009", anchor=W).place(x=10, y=10, width=100, height=20)
vname=Entry(app)
vname.place(x=10,y=30, width=200, height=20)

Label(app,text="Phone number", bg="#dde", fg="#009", anchor=W).place(x=10, y=60, width=100, height=20)
vphone=Entry(app)
vphone.place(x=10,y=80, width=200, height=20)

Label(app,text="Flavours", bg="#dde", fg="#009", anchor=W).place(x=10, y=110, width=100, height=20)
vf=Entry(app)
vf.place(x=10,y=130, width=200, height=20)

Label(app,text="OBS", bg="#dde", fg="#009", anchor=W).place(x=10, y=160, width=100, height=20)
vt=Text(app)
vt.place(x=10,y=180, width=200, height=80)

Button(app, text="Print out", command=writeData).place(x=10, y=280, width=100, height=25)

app.mainloop()