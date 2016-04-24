# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 16:16:43 2016

@author: Hugo
"""

import tkinter as tk

def vez_de_quem(X):
    if X == True:
        X = False
        return "X"
    if X == False:
        X = True
        return "O"
        

#defs de cada botão
def X_O1():
    
        botão1.configure(text="X")
      
def X_O2():
    
        botão2.configure(text="X")
       
def X_O3():
     
        botão3.configure(text="X")
       
def X_O4():
   
        botão4.configure(text="X")
       
def X_O5():
    
        botão5.configure(text="X")
       
def X_O6():
     
        botão6.configure(text="X")
       
def X_O7():
    
        botão7.configure(text="X")
       
def X_O8():
     
        botão8.configure(text="X")
       
def X_O9():
     
        botão9.configure(text="X")
       
window = tk.Tk()

X = True
O = False

#botão 1
botão1 = tk.Button(window)
botão1.configure(command=X_O1)
botão1.config( height = 10, width = 20)
botão1.grid(row=0,column=0)

#botão2
botão2 = tk.Button(window)
botão2.configure(command=X_O2)
botão2.config( height = 10, width = 20)
botão2.grid(row=0,column=1)

#botão3
botão3 = tk.Button(window)
botão3.configure(command=X_O3)
botão3.config( height = 10, width = 20)
botão3.grid(row=0,column=2)

#botão4
botão4 = tk.Button(window)
botão4.configure(command=X_O4)
botão4.config( height = 10, width = 20)
botão4.grid(row=1,column=0)

#botão5
botão5 = tk.Button(window)
botão5.configure(command=X_O5)
botão5.config( height = 10, width = 20)
botão5.grid(row=1,column=1)

#botão6
botão6 = tk.Button(window)
botão6.configure(command=X_O6)
botão6.config( height = 10, width = 20)
botão6.grid(row=1,column=2)

#botão7
botão7 = tk.Button(window)
botão7.configure(command=X_O7)
botão7.config( height = 10, width = 20)
botão7.grid(row=2,column=0)

#botão8
botão8 = tk.Button(window)
botão8.configure(command=X_O8)
botão8.config( height = 10, width = 20)
botão8.grid(row=2,column=1)

#botão9
botão9 = tk.Button(window)
botão9.configure(command=X_O9)
botão9.config( height = 10, width = 20)
botão9.grid(row=2,column=2)

#vez do jogador tal
label = tk.Label(window)
label.configure(text="Vez do Jogador : {0}".format(vez_de_quem(X)))
label.grid(row=3,column=1)

    
    


window.title("Jogo Da Velha Fudidão")
window.mainloop()
