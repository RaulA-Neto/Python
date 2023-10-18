# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:47:37 2023

@author: joaop
"""

class retangulo():
    def __init__(self,x,y,w,h):
        self.yv = y
        self.xv = x
        self.Altura = h
        self.Largura = w
        
    def getAltura(self):
        return self.Altura
    
    def setAltura(self,h):
        self.Altura = h
        
    def getLargura(self):
            return self.Largura
        
    def setLargura(self,w):
        self.Largura = w
        
    def getXv(self):
        return self.xv
    
    def getYv(self):
        return self.yv
    
    def setXv(self,x):
        self.xv = x
        
    def setYv(self,y):
        self.yv = y
        
    def setCorner(self,x,y):
        self.xv = x
        self.yv = y
        
    def setSize(self,w,h):
        self.Altura = h
        self.Largura = w
        
    def calcArea(self):
        

        
        
        
    