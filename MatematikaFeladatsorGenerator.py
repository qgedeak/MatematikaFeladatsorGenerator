# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 12:43:42 2016
@author: Csaba & Vica 

Ez egy feladat generátor lenne.
A feladatok vegyesek, de mind a matematika témaköreiből vannak:
- első feladat: függvény kitalálása
- második feladat: másodfokú egyenlet gyöke és képe.
"""


#függvény kirajzó
import numpy as np
from matplotlib import pyplot as pl
from matplotlib.widgets import Button
import random
from math import sqrt

def xnegyzet(x):
    return x*x
def xkob(x):
    return x*x*x
def linearis(x):
    return x
fuggvenyfajtak=[]
fuggvenyfajtak.append([([-3,3]),'sin', np.sin])
fuggvenyfajtak.append([([-3,3]),'cos', np.cos])
fuggvenyfajtak.append([([-3,3]),'abs', np.abs])
fuggvenyfajtak.append([([-3,3]),'arctan', np.arctan])
fuggvenyfajtak.append([([-3,3]),'tan', np.tan])
fuggvenyfajtak.append([([-3,3]),'exp', np.exp])
fuggvenyfajtak.append([([-3,3]),'x^2', xnegyzet])
fuggvenyfajtak.append([([-3,3]),'x^3', xkob])
fuggvenyfajtak.append([([-3,3]),'lineáris', linearis])
def fuggvenygen():
    return random.sample(fuggvenyfajtak ,4 )

negy = fuggvenygen()
ax=[0,0,0,0]

#%%

f, ((ax[0], ax[1]), (ax[2], ax[3])) = pl.subplots(2, 2) #mindegyikhez tennék tengelyt
f.tight_layout() # automata elhelyezése a subplotoknak
pl.subplots_adjust(hspace = 0.35, top = 0.87, bottom = 0.2) # a címek miatt kicsit több hely kell
for i in range(4):
    ax[i].set_title(str(i+1) + " .függvény") #itt elég ha az i-t írjuk
    x = np.linspace(negy[i][0][0], negy[i][0][1], 1000)
    ax[i].plot(x, negy[i][2](x),color='r')
    
kiv=random.choice(negy) #elraktuk a kiválasztott függvényt
f.suptitle('Melyik a '+kiv[1]+' függvény? (1,2,3,4)',fontsize=18, color='b') #a cím helyén jelenik meg a kérdés és a válasz kiértékelése is.

class Index(object):
    
    def jo(self,valasz):
        if kiv==negy[valasz]:
            f.suptitle('Helyes!',fontsize=20, color='g')
        else:
            f.suptitle('Gondold át újra!',fontsize=20, color='r')

    def egy(self, event):
        self.jo(0)
        pl.draw()

    def ketto(self, event):
        self.jo(1)
        pl.draw()
        
    def harom(self, event):
        self.jo(2)
        pl.draw()
        
    def negy(self, event):
        self.jo(3)
        pl.draw()

callback = Index()
axegy = pl.axes([0.15, 0.05, 0.1, 0.075])
axketto = pl.axes([0.35, 0.05, 0.1, 0.075])
axharom = pl.axes([0.55, 0.05, 0.1, 0.075])
axnegy = pl.axes([0.75, 0.05, 0.1, 0.075])
begy = Button(axegy, '1')
begy.on_clicked(callback.egy)
bketto = Button(axketto, '2')
bketto.on_clicked(callback.ketto)
bharom = Button(axharom, '3')
bharom.on_clicked(callback.harom)
bnegy = Button(axnegy, '4')
bnegy.on_clicked(callback.negy)

pl.show()

#%%
#másodfokú egyenlet
def masodfoku(a,b,c):
    D=b**2-4*a*c
    print("\nA determináns: ", D)
    if D < 0:
       print ("Nincs valós gyök.")
       return []
    elif D==0:
       print ("Kettős valós gyök van.")
       return [-b/2*a]
    else:
       print ("Két eltérő valós gyök van.")
       x1=(-b+sqrt(D))/(2*a)
       x2=(-b-sqrt(D))/(2*a)
       return [x1,x2]
       
print("Add meg a másodfokú egyenlet együtthatóit!\n")
a=0
while a==0:
    a = int(input("Az első együttható: "))
    if a==0:
        print("A másodfokú egyenlet első együtthatója nem lehet 0!")
        print("Add meg újra!")
b = int(input("A második együttható: "))
c = int(input("A harmadik együttható: "))

print("Az egyenlet: ",end="") 
if a==1:
    print("x^2",end="")
else:
    print(str(a)+"x^2",end="")
if b==1:
    print("+x",end="")
elif b>0:
    print("+"+str(b)+"x",end="")
elif b<0:
    print(str(b)+"x",end="")
if c>0:
    print("+"+str(c),end="")
elif c<0:
    print(str(c),end="")
print("=0",end="")

  
megoldasok = masodfoku(a,b,c)

for i,m in enumerate(megoldasok):
    print("x"+str(i),"=",m)

