# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:31:45 2023

@author: RaulA
"""

class Pilha:
    def __init__(self):
        self.items = []
    
    def empilhar(self, valor): 
        self.items.append(valor)
        
    def desempilhar(self):
        return self.items.pop()
    
    def tamanho(self):
        return len(self.items)
    
    def vazia(self):
        return self.items == []
    
    def mostra(self):
        return self.items
   
    def mostra2(self):
        for items in self.items[::-1]:
            print(items)
            
p = Pilha()
p.empilhar(4)
p.empilhar('gato')
p.empilhar(3.1415)
print(p.vazia()) 
print(p.mostra())
item = p.desempilhar()  
print(item)
item = p.desempilhar()  
print(item)
item = p.desempilhar()  
print(item)
print(p.vazia()) 
        
        