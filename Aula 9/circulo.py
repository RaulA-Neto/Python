# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 19:57:52 2023

@author: joaop
"""

class circulo():
    def __init__(self,x,y,r):
        self.raio = r
        self.xc = x
        self.yc = y

    def getRaio(self):
        return self.raio

    def setRaio(self,r):
        self.raio = r

    def getXc(self):
        return self.xc
    
    def getYc(self):
        return self.yc

    def setXc(self,x):
        self.xc = x
        
    def setYc(self,y):
        self.yc = y
            
    def setCentro(self,x,y):
        self.xc = x
        self.yc = y
        
    def calcArea(self):
        return 3.1415*self.raio**2
    
    def calcPerim(self):
        return 6.2830*self.raio


c1 = circulo(0,0,1)
c2 = circulo(-2,4,5)
r1 = c1.getRaio()
r2 = c2.getRaio()
print(" o raio do primeiro circulo é: "+str(r1))
print(" o raio do segundo circulo é: "+str(r2))
c1.setRaio(2)
r1 = c1.getRaio()
print(" o raio do primeiro circulo é: "+str(r1))
xc1 = c1.getXc()
yc1 = c1.getYc()
xc2 = c2.getXc()
yc2 = c2.getYc()
print("centro de c1: "+str(xc1)+","+str(yc1))
print("centro de c2: "+str(xc2)+","+str(yc2))
c1.setXc(2)
c1.setYc(2)
c2.setCentro(10,10)
xc1 = c1.getXc()
yc1 = c1.getYc()
xc2 = c2.getXc()
yc2 = c2.getYc()
print("centro de c1: "+str(xc1)+","+str(yc1))
print("centro de c2: "+str(xc2)+","+str(yc2))
area1 = c1.calcArea()
area2 = c2.calcArea()
perim1 = c1.calcPerim()
perim2 = c2.calcPerim()
print("area de c1: "+str(area1))
print("area de c2: "+str(area2))
print("perimetro de c1: "+str(perim1))
print("perimetro de c2: "+str(perim2))
