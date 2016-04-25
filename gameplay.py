# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:25:57 2016

@author: Jean Walper
"""
import numpy as np

class Base:
    def __init__(self,matriz,turno,vezes):
        self.matriz = matriz
        self.turno = turno
        self.vezes = vezes
    
    def recebe_jogada(i,n):
        if jogo.matriz[i][n] == 0:
            jogo.vezes +=1
            if jogo.turno == 1:
                jogo.matriz[i][n] = -1
                jogo.turno += 1
            else:
                jogo.matriz[i][n] = 1
                jogo.turno -= 1
            
    def check_linha(i):
        x = 0
        for a in jogo.matriz[i]:
            x += a
        return x
        
    def check_coluna(n):
        x = 0
        for a in jogo.matriz[:,n]:
            x += a
        return x
    
    def check_diagonal(m):
        x = 0
        if m == 1:
            for i in np.diag(jogo.matriz):
                x += i
        if m == 2:
            matriz_flipped = np.fliplr(jogo.matriz)
            for i in np.diag(matriz_flipped):
                x += i
        return x
        
    def verifica_ganhador():
        for l in range (0,3):
            i= 0
            n = 0
            m = 0
            i = Base.check_linha(l)
            n = Base.check_coluna(l)
            m = Base.check_diagonal(l)
            if i == 3 or n == 3 or m == 3:
                print("O ganhou")
                return 2
            if i == -3 or n == -3 or m == -3:
                print ("X ganhou")
                return 1
        if jogo.vezes == 10:
            print("velha")
            return 0
        return -1
    def reset():
        for i in range (3):
            for n in range (3):
                 print (i)
                 print (n)
                 jogo.matriz[i][n] = 0
                 
    

        
matriz =np.zeros([3,3])

#exemple 1:

#matriz[0][2] = 1
#matriz[1][1] = 1
#matriz[2][0] = 1

#exemple 2:

#matriz[0][2] = -1
#matriz[1][1] = -1
#matriz[2][0] = -1

#exemple 3:

matriz[0][0] = 0
matriz[0][1] = 0
matriz[0][2] = 0

matriz[1][0] = 0
matriz[1][1] = 0
matriz[1][2] = 0

matriz[2][0] = 0
matriz[2][1] = 0
matriz[2][2] = 0


jogo = Base(matriz,1,1)

while True:
    x = int(input("cordenadas x de X"))
    y = int(input("cordenada y de X"))
    
    Base.recebe_jogada(x,y)
    Base.verifica_ganhador()
    
    x = int(input("cordenadas x de O"))
    y = int(input("cordenada y de O"))
    
    Base.recebe_jogada(x,y)
    Base.verifica_ganhador()
    