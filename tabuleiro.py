# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:07:53 2016

@author: Hugo
"""


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
        botõesx.append(botãox)
       
    
        
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
botõesx= []  


for i in botões:
    tabuleiro.criar_tabuleiro(i)
    
def E0():
    botõesx[0].configure(text="x")    
botõesx[0].configure(command=E0)

def E1():
    botõesx[1].configure(text="x")    
botõesx[1].configure(command=E1)

def E2():
    botõesx[2].configure(text="x")    
botõesx[2].configure(command=E2)

def E3():
    botõesx[3].configure(text="x")    
botõesx[3].configure(command=E3)

def E4():
    botõesx[4].configure(text="x")    
botõesx[4].configure(command=E4)

def E5():
    botõesx[5].configure(text="x")    
botõesx[5].configure(command=E5)

def E6():
    botõesx[6].configure(text="x")    
botõesx[6].configure(command=E6)

def E7():
    botõesx[7].configure(text="x")    
botõesx[7].configure(command=E7)

def E8():
    botõesx[8].configure(text="x")    
botõesx[8].configure(command=E8)
    
        
window.title("Jogo da Velha")
window.mainloop()