# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 23:20:43 2016

@author: Jean Walper
"""

import numpy as np
import random

class jokenpoh:
    def jokenpoh(x):
        y = random.randint(1,3)
        if y == 1:
            comp = "pedra"
        elif y == 2:
            comp = "papel"
        else:
            comp = "tesoura"
            
        print ("random:",y)
        if x == y:
            return -1,"empate"
        elif x == 1:
            if y == 2:
                return 0,comp
            if y == 3:
                return 1,comp
        elif x == 2:
            if y == 1:
                return 1,comp
            if y == 3:
                return 0,comp
        else:
            if y == 1:
                return 0,comp
            if y == 2:
                return 1,comp

class ia_easy:     
    def cpu_play():
        i = random.randint (0,3)
        n = random.randint (0,3)
        Base.recebejogada(i,n)
    
    def jogo_easy():
        ia_easy.cpu_play

class ia_medium:
    def cpu_play():
        if jogo.matriz[1][1] == 0:
            Base.recebe_jogada(1,1)
        else:
            sides = [(0,1),(1,0),(1,2),(2,1)]
            while len(sides) != 0:
                x = random.choice(sides)
                if jogo.matriz == 0:
                    Base.recebe_jogada(x)
                    break
                if not jogo.matriz(x) == 0:
                    sides.remove(x)
            corners = [(0,0),(0,2),(2,0),(2,2)]
            while len(corners) != 0:
                y = random.choice(corners)
                if jogo.matriz(y) == 0:
                    Base.recebe_jogada(y)
                    break
                if not jogo.matriz(y) == 0:
                    corners.remove(y)
        
class ia_hard:
    def hard_play():
        sides = [(0,1),(1,0),(1,2),(2,1)]
        corners = [(0,0),(0,2),(2,0),(2,2)]
        
        