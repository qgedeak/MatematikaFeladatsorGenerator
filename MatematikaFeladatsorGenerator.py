
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
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
from matplotlib.widgets import Button
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

fuggvenyfajtak.append([([-3,3]),'exp', np.exp])
fuggvenyfajtak.append([([-3,3]),'x^2', xnegyzet])
fuggvenyfajtak.append([([-3,3]),'x^3', xkob])
fuggvenyfajtak.append([([-3,3]),'lineáris', linearis])
def fuggvenygen():
    return random.sample(fuggvenyfajtak ,4 )
    
#pl.ion()    #külön szálra rakja a kirajzolót

negy = fuggvenygen()
kiv=random.choice(negy)
class Index(object):
    def gomb1(self, event):
        joe(0)       
    def gomb2(self, event):
        joe(1)
    def gomb3(self, event):
        joe(2) 
    def gomb4(self, event):
        joe(3)
def joe(valasz):
        if kiv==negy[valasz]: #megnézzük, hogy jó választ adott-e
            pl.suptitle('Melyik a '+kiv[1]+' függvény?  Helyes a válasz!')
        else:
            pl.suptitle('Melyik a '+kiv[1]+' függvény?  Gondold át újra!')
            
          
ax=[0,0,0,0]
f, ((ax[0], ax[1]), (ax[2], ax[3])) = pl.subplots(2, 2) #mindegyikhez tennék tengelyt
f.tight_layout() # automata elhelyezése a subplotoknak
pl.suptitle('Melyik a '+kiv[1]+' függvény? ')  
pl.subplots_adjust(top = 0.9) # a címek miatt kicsit több hely kell

for i in range(4):
    #ax[i].set_title(str(i+1) + " .függvény") #itt elég ha az i-t írjuk
    x = np.linspace(negy[i][0][0], negy[i][0][1], 1000)
    ax[i].plot(x, negy[i][2](x),color='r')
   
callback = Index()
ax1 = pl.axes([0.4, 0.55, 0.1, 0.05])
ax2 = pl.axes([0.4, 0.050, 0.1, 0.05])
ax3 = pl.axes([0.8, 0.55, 0.1, 0.05])
ax4 = pl.axes([0.8, 0.050, 0.1, 0.05])

b1 = Button(ax1, 'a')
b1.on_clicked(callback.gomb1)
b2 = Button(ax2, 'b')
b2.on_clicked(callback.gomb2)
b3 = Button(ax3, 'c')
b3.on_clicked(callback.gomb3)
b4 = Button(ax4, 'd')
b4.on_clicked(callback.gomb4)
pl.show()   

'''
pl.pause(0.001) #azért kell, hogy frissítse a kirajzolt képet
kiv=random.choice(negy) #elraktuk a kiválasztott függvényt
valasz = int(input('Melyik a '+kiv[1]+' függvény? (1,2,3,4)'))-1 #a bekért választ eltettük
if valasz>3 or valasz<0:
    print ("A válasz 1 és 4 közötti szám lehet!")
elif kiv==negy[valasz]: #megnézzük, hogy jó választ adott-e
    print ("Helyes a válasz!")
else:
    print ("Gondold át újra!")
'''