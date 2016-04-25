# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:58:36 2016

@author: Hugo
"""
import tkinter as tk
from gameplay import *

class tabuleiro:
    def __init__(self,height,width,row,column):
        self.height = height
        self.width = width
        self.row = row
        self.column = column
    
    def criar_tabuleiro(botão):
        printar = tk.Label(window)
        botãox = tk.Button(window)
#        botãox.config( height = 10,width = 20)
        botãox.grid(row = botão.row,column = botão.column)
        botãox.configure(bg = "gray")
        botõesx.append(botãox)
        a = Base.verifica_ganhador()
        if a == -1:
             botãox.configure(command= lambda: tabuleiro.rodar(botão.row,botão.column))
       
        if a == 1:
                printar.configure(text="Jogador X ganhou!",font=("Helvetica",11),background="white",foreground = "dark blue")
                printar.grid(row=1,column=1)
                tabuleiro.tentar_novamente()
                
        elif a == 0:
                printar.configure(text="DEU VELHA",font=("Helvetica",15),background="black",foreground = "white")
                printar.grid(row=1,column=1)
                tabuleiro.tentar_novamente()
        if a == 2:
                printar.configure(text="Jogador O ganhou!",font=("Helvetica",11),background="black",foreground = "orange")
                printar.grid(row=1,column=1)
                tabuleiro.tentar_novamente()
        elif a == 0:
                printar.configure(text="DEU VELHA",background="black",foreground = "white")
                printar.grid(row=1,column=1)
                tabuleiro.tentar_novamente() 
            
        if jogo.matriz[botão.row][botão.column] == 0 and jogo.turno == 1:
            botãox.configure(text="x",font=("Helvetica",70),background="gray",foreground = "gray")
            
        if jogo.matriz[botão.row][botão.column] == 0 and jogo.turno == 2:
            botãox.configure(text="o",font=("Helvetica",70),background="gray",foreground = "gray")
                        
        if jogo.matriz[botão.row][botão.column] == -1:
            botãox.configure(text="x",font=("Helvetica",70),background="white",foreground="dark blue")

        elif jogo.matriz[botão.row][botão.column]== 1:
            botãox.configure(text="o",font=("Helvetica",69),background="black",foreground="orange")

    def rodar(i,n):
        Base.recebe_jogada(i,n)
        for p in botões:
            tabuleiro.criar_tabuleiro(p)
                
        if jogo.turno == 2:
            label.configure(text="VEZ DO JOGADOR O")
            label.grid(row=3,column=1)
        elif jogo.turno == 1:
            label.configure(text="VEZ DO JOGADOR X")
            label.grid(row=3,column=1)
                                
    def tentar_novamente():
        tente = tk.Button(window)
        tente.configure(text="Recomeçar")
        tente.configure(command=tabuleiro.resetar_tabuleiro)
        tente.grid(row=4,column=1)
    
    def resetar_tabuleiro():
        Base.limpar_jogadas()
        for p in botões:
                tabuleiro.criar_tabuleiro(p)
              
window = tk.Tk() 
label =tk.Label(window)       

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

jogo_is_on = 1

label = tk.Label(window)   
window.title("Jogo da Velha")
    
for p in botões:
    tabuleiro.criar_tabuleiro(p)

label =tk.Label(window)
label.configure(text="VEZ DO JOGADOR X")
label.grid(row=3,column=1)
                
window.mainloop()
