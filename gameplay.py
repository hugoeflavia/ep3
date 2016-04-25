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
            print ("a =", a)
        print ("linha ", x)
        return x
        
    def check_coluna(n):
        x = 0
        for a in jogo.matriz[:,n]:
            x += a
        print ("coluna" , x)    
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
            i = 0
            n = 0
            m = 0
            i = Base.check_linha(l)
            n = Base.check_coluna(l)
            m = Base.check_diagonal(l)
            if i == 3 or n == 3 or m == 3:
                print ("O ganhou")
                return 2
            if i == -3 or n == -3 or m == -3:
                print ("X ganhou")
                return 1
        if jogo.vezes == 10:
            return 0
        return -1
        
    def limpar_jogadas():
        for i in range (3):
            for n in range (3):
                 jogo.matriz[i][n] = 0
        jogo.vezes = 1
                 
matriz =np.zeros([3,3])

jogo = Base(matriz,1,1)

Base.verifica_ganhador()