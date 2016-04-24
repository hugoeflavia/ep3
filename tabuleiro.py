# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:07:53 2016

@author: Hugo
"""

import numpy as np
import tkinter as tk

class tabuleiro:
    def __init__(self,height,width,row,column):
        self.height = height
        self.width = width
        self.row = row
        self.column = column
    
    def criar_tabuleiro(botão):
        
       
        botãox = tk.Button(window)
        botãox.config( height = 10,width = 20)
        botãox.grid(row = botão.row,column = botão.column)
        
window = tk.Tk()        
      
botão1 = tabuleiro(10,20,0,0)
botão2 = tabuleiro(10,20,0,1)
botão3 = tabuleiro(10,20,0,2)
botão4 = tabuleiro(10,20,1,0)
botão5= tabuleiro(10,20,1,1)
botão6 = tabuleiro(10,20,1,2)
botão7 = tabuleiro(10,20,2,0)
botão8= tabuleiro(10,20,2,1)
botão9 = tabuleiro(10,20,2,2)
 
botões = [botão1,botão2,botão3,botão4,botão5,botão6,botão7,botão8,botão9]

for i in botões:
    tabuleiro.criar_tabuleiro(i)

window.mainloop()