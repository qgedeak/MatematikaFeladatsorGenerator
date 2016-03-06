
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 12:43:42 2016

@author: Csaba


Ez egy feladat generátor lenne.
A feladatok vegyessek , de mind a matematika témaköreiből
- Egyik feladat a függvény kitalálása
"""

#függvény kirajzó
import numpy as np
from matplotlib import pyplot as pl
import random
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
fuggvenyfajtak.append([([-3,3]),'x*x', xnegyzet])
fuggvenyfajtak.append([([-3,3]),'x*x*x', xkob])
fuggvenyfajtak.append([([-3,3]),'lineáris', linearis])
def fuggvenygen():
    return random.sample(fuggvenyfajtak ,4 )
    

pl.ion()    #külön szálra rakja a kirajzolót
pl.show()   #így nem akasztja meg a kirajzolás a programot

negy = fuggvenygen()
ax=[0,0,0,0]
f, ((ax[0], ax[1]), (ax[2], ax[3])) = pl.subplots(2, 2) #mindegyikhez tennék tengelyt
f.tight_layout() # automata elhelyezése a subplotoknak
pl.subplots_adjust(hspace = 0.3) # a címek miatt kicsit több hely kell
for i in range(4):
    ax[i].set_title(str(i+1) + " .függvény") #itt elég ha az i-t írjuk
    x = np.linspace(negy[i][0][0], negy[i][0][1], 1000)
    ax[i].plot(x, negy[i][2](x),color='r')

pl.draw()
pl.pause(0.001) #azért kell, hogy frissítse a kirajzolt képet
kiv=random.choice(negy) #elraktuk a kiválasztott függvényt
valasz = int(input('Melyik a '+kiv[1]+' függvény? (1,2,3,4)'))-1 #a bekért választ eltettük
if valasz>3 or valasz<0:
    print ("A válasz 1 és 4 közötti szám lehet!")
elif kiv==negy[valasz]: #megnézzük, hogy jó választ adott-e
    print ("Helyes a válasz!")
else:
    print ("Gondold át újra!")
