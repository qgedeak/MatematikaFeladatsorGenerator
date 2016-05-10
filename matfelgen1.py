# -*- coding: utf-8 -*-
"""
Created on Sun May  8 11:45:18 2016

@author: PackardBell
"""
import globval
import numpy as np
from matplotlib import pyplot as pl
from matplotlib.widgets import Button as Bt
import random
from math import sqrt
from decimal import *
from tkinter import *



def fuggvenyes():
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
    begy = Bt(axegy, '1')
    begy.on_clicked(callback.egy)
    bketto = Bt(axketto, '2')
    bketto.on_clicked(callback.ketto)
    bharom = Bt(axharom, '3')
    bharom.on_clicked(callback.harom)
    bnegy = Bt(axnegy, '4')
    bnegy.on_clicked(callback.negy)
    
    pl.show()
    
    #%%
    #másodfokú egyenlet
def masodfokegy():
    
    m_ablak=Tk()
    m_ablak.title("Másodfokú egyenlet")
    #m_ablak.geometry("1000x400")
    
   
    
    def masodfoku(a,b,c):
        D=b**2-4*a*c
        det.delete(0,END)
        det.insert(0,str(D))
        szoveredm.delete(0,END)
        if D < 0:
            szoveredm.insert(0,"Nincs valós gyöke!")
            return []
        elif D==0:
            szoveredm.insert(0,"Kettős valós gyöke van.")
            x1=-b/2*a
            return [x1]
        else:
            szoveredm.insert(0,"Két eltérő valós gyöke van.")
            x1=(-b+sqrt(D))/(2*a)
            x2=(-b-sqrt(D))/(2*a)          
            return [x1,x2]
            
    def mo_gomb_click():
      try:
          hiba1.delete(0,END)
          a=int(valasz_a.get())
          if a==0:
               raise ValueError
      except:
          hiba1.delete(0,END)
          hiba1.insert(0,"Hibás adat!")
          return
      try:
          hiba2.delete(0,END)
          b=int(valasz_b.get())
      except:
          hiba2.delete(0,END)
          hiba2.insert(0,"Hibás adat!")
          return
      try:
          hiba3.delete(0,END)
          c=int(valasz_c.get())
      except:
          hiba3.delete(0,END)
          hiba3.insert(0,"Hibás adat!")
          return
      ki_egyenlet=""
      if a==1:
          ki_egyenlet="x^2"    
      else:
          ki_egyenlet=str(a)+"x^2"
      if b==1:
          ki_egyenlet=ki_egyenlet+"+x"
      elif b>0:
          ki_egyenlet=ki_egyenlet+"+"+str(b)+"x"
      elif b<0:
          ki_egyenlet=ki_egyenlet+str(b)+"x"
      if c>0:
          ki_egyenlet=ki_egyenlet+"+"+str(c)
      elif c<0:
          ki_egyenlet=ki_egyenlet+str(c)
      egyen.delete(0,END)
      egyen.insert(0,ki_egyenlet+"=0")
      gyokok.delete(0,END)
      masodfoku(a,b,c)
      megoldasok = masodfoku(a,b,c)
      ki_gyok=""
      for i,m in enumerate(megoldasok):
          ki_gyok=ki_gyok+"X"+str(i)+"="+str(m)+"    "
      gyokok.insert(0,ki_gyok)
   
      
   #A widgetek létrehozása
    txt1=Label(m_ablak,text="Az első együttható: ",font="Helvetica 16 bold italic",fg="darkolivegreen")
    txt2=Label(m_ablak,text="A második együttható: ",font="Helvetica 16 bold italic",fg="darkolivegreen")
    txt3=Label(m_ablak,text="A harmadik együttható: ",font="Helvetica 16 bold italic",fg="darkolivegreen")
    txt4=Label(m_ablak,text="A egyenlet: ",font="Helvetica 16 bold italic",fg="maroon")
    txt5=Label(m_ablak,text="A determináns értéke: ",font="Helvetica 16 bold italic",fg="maroon")
    txt6=Label(m_ablak,text="Eredmények: ",font="Helvetica 16 bold italic",fg="maroon")
    gomb1=Button(m_ablak,text="MEGOLDÁS",command=mo_gomb_click,font="Helvetica 16 bold italic",fg="peachpuff",bg="darkolivegreen")
    valasz_a=Entry(m_ablak,width=20,font="Helvetica 12 bold italic")
    valasz_b=Entry(m_ablak,width=20,font="Helvetica 12 bold italic")
    valasz_c=Entry(m_ablak,width=20,font="Helvetica 12 bold italic")
    egyen=Entry(m_ablak,width=20,font="Helvetica 12 bold italic")
    det=Entry(m_ablak,width=20,font="Helvetica 12 bold italic")
    szoveredm=Entry(m_ablak,width=50,font="Helvetica 12 bold italic")
    gyokok=Entry(m_ablak,width=50,font="Helvetica 12 bold italic")
    hiba1=Entry(m_ablak,width=20,fg='red',font="Helvetica 12 bold italic")
    hiba2=Entry(m_ablak,width=20,fg='red',font="Helvetica 12 bold italic")
    hiba3=Entry(m_ablak,width=20,fg='red',font="Helvetica 12 bold italic")
   
   #Laptördelés
    txt1.grid(row=1,sticky=W)
    txt2.grid(row=2,sticky=W)
    txt3.grid(row=3,sticky=W)
    txt4.grid(row=5,sticky=W)
    txt5.grid(row=6,sticky=W)
    txt6.grid(row=7,sticky=W,column=0)
    gomb1.grid(row=4,column=1)
    valasz_a.grid(row=1,column=2)
    valasz_b.grid(row=2,column=2)
    valasz_c.grid(row=3,column=2)
    egyen.grid(row=5,column=2)
    det.grid(row=6,column=2)
    szoveredm.grid(row=7,column=2)
    gyokok.grid(row=8,column=2,padx=10,pady=10)
    hiba1.grid(row=1,column=3,padx=10)
    hiba2.grid(row=2,column=3)
    hiba3.grid(row=3,column=3)
   
    mainloop()    
    
    
   
#%%

def szoveges():
    getcontext().prec=3 # decimális jegyek
    ablak = Tk()
    ablak.title("Szöveges feladat")
    
   
    
        
    def uj_click():
        eredm.delete(0,END)
        valasz.delete(0,END)
        globval.ember1=random.randint(2,10)
        globval.nap1=random.randint(2,10) 
        globval.ember2=random.randint(2,10)
        globval.nap2=globval.nap1*globval.ember1/globval.ember2
        globval.nap2=Decimal(globval.nap2)
        szoveg.delete(0,END)
        szoveg.insert(0,"Ha " +str(globval.ember1)+ " ember "+str(globval.nap1)+" nap alatt ás fel egy kertet, akkor hány nap alatt ássa fel "+str(globval.ember2)+" ember?")
        
    def ok_click():
        try:
            eredm.delete(0,END)
            x=float(valasz.get())
            if x==globval.nap2:
                eredm.insert(0,"A válasz helyes!")
            else :
                eredm.insert(0,"Gondolt át újra! A helyes válasz: "+str(globval.nap2)[0:4])
        except:
            eredm.insert(0,"Nem számot adtál meg!")
       
    #A widgetek létrehozása

    txt1=Label(ablak,text="Szöveges feladat: ",font="Helvetica 16 bold italic",fg="darkblue")
    szoveg=Entry(ablak,width=100,font="Helvetica 12 bold italic")
    txt2=Label(ablak,text="Megoldás: ",font="Helvetica 16 bold italic",fg="darkblue")
    valasz=Entry(ablak,width=10,font="Helvetica 12 bold italic")
    ok=Button(ablak,text="OK",command=ok_click,font="Helvetica 12 bold italic",fg="darkblue")
    eredm=Entry(ablak,width=50,font="Helvetica 12 bold italic",fg="red")
    uj=Button(ablak,text="ÚJ FELADAT",command=uj_click,font="Helvetica 12 bold italic",fg="darkblue")
      
    #Laptördelés
    txt1.grid(row=1,sticky=W,column=0)
    szoveg.grid(row=1,sticky=W,column=1,pady=20)
    txt2.grid(row=2,column=0,sticky=W)
    valasz.grid(row=2,column=1,pady=20)
    ok.grid(row=2,column=3,padx=20)
    eredm.grid(row=3,column=1)
    uj.grid(row=4,column=1,pady=20)
    
    globval.ember1=random.randint(2,10)
    globval.nap1=random.randint(2,10)
    globval.ember2=random.randint(2,10)
    globval.nap2=globval.nap1*globval.ember1/globval.ember2
    globval.nap2=Decimal(globval.nap2)
    
    szoveg.insert(0,"Ha "+str(globval.ember1)+" ember "+str(globval.nap1)+" nap alatt ás fel egy kertet, akkor hány nap alatt ássa fel "+str(globval.ember2)+" ember?")
    
    
    
    mainloop()
    
    
szoveges()
masodfokegy()
fuggvenyes()

