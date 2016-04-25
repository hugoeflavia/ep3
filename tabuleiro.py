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
        botãox.config( height = 10,width = 20)
        botãox.grid(row = botão.row,column = botão.column)
        botãox.configure(bg = "white")
        botõesx.append(botãox)
        botãox.configure(command= lambda: tabuleiro.rodar(botão.row,botão.column))
        a = Base.verifica_ganhador()
        if jogo.matriz[botão.row][botão.column] == -1:
            botãox.configure(text="X")
            if a == 1:
                printar.configure(text="Jogador X ganhou!")
                printar.grid(row=1,column=1)
                tabuleiro.tentar_novamente()
                
            elif a == 0:
                printar.configure(text="DEU VELHA")
                printar.grid(row=1,column=1)
                tabuleiro.tentar_novamente()
           
        elif jogo.matriz[botão.row][botão.column]== 1:
            botãox.configure(text="O")
            if a == 2:
                printar.configure(text="Jogador O ganhou!")
                printar.grid(row=1,column=1)
                tabuleiro.tentar_novamente()
            elif a == 0:
                printar.configure(text="DEU VELHA")
                printar.grid(row=1,column=1)
                tabuleiro.tentar_novamente()
                      
    def rodar(i,n):
        Base.recebe_jogada(i,n)
        a = Base.verifica_ganhador()
        if not a == -1:
            for p in botões:
                tabuleiro.criar_tabuleiro(p)
        if a == -1:
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
