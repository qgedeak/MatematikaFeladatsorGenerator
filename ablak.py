# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 17:10:02 2016

@author: Csaba
"""

from tkinter import *
import random
ablak = Tk()
ablak.title("Szöveges feladat")
ablak.geometry("800x600")

hiba=Label(ablak, text="").grid(row=2, column=1)
ember1=random.randint(2,10)
nap1=random.randint(2,10)
ember2=random.randint(2,10)
nap2=nap1*ember1/ember2
Label(ablak, text="Ha " +str(ember1)+ " ember " +str(nap1)+ " nap alatt ás fel egy kertet, akkor hány nap alatt ása fel " +str(ember2)+ " ember.").grid(row=1, column=0)

def uj_click():
    global ember1
    ember1=random.randint(2,10)
    global nap1
    nap1=random.randint(2,10)
    global ember2
    ember2=random.randint(2,10)
    global nap2
    nap2=nap1*ember1/ember2
    Label(ablak, text="Ha " +str(ember1)+ " ember " +str(nap1)+ " nap alatt ás fel egy kertet, akkor hány nap alatt ása fel " +str(ember2)+ " ember.").grid(row=1, column=0)

def ok_click():
    try:
        hiba=Label(ablak, text="                                                         ").grid(row=0, column=1)
        x=float(valasz.get())
        if x==nap2:
            hiba=Label(ablak, text="Helyes",bg="green").grid(row=2, column=1)
        else :
            hiba=Label(ablak, text="Gondolt át újra!"+str(nap2),bg="red").grid(row=2, column=1)  
    except:
        hiba=Label(ablak, text="Nem számot adtál meg!",bg="red").grid(row=2, column=1)


valasz = Entry(ablak)
valasz.grid(row=2, column=0)
ok=Button(ablak,text="Ok",command=ok_click).grid(row=3, column=1)
uj=Button(ablak,text="új feladat",command=uj_click).grid(row=3, column=0)       
mainloop()