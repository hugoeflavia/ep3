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
            

