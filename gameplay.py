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
    