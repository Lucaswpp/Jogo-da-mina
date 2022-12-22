from os import listdir
import pygame as pyg

size = 8,8
tab_lista = []
cont = 0

for row in range(size[0]):
    row = []
    for col in range(size[1]):
        cont += 1
        row.append(cont)
    tab_lista.append(row)

a = ""
for lista in tab_lista:

    for i in lista:
        a += str(i)+" "
    print(a)
    a = ""

def get_num_tab(line,col):
    return tab_lista[line][col]

def vizinho(line,col):
    vizin = []
    for row in range(line - 1,line + 2):
        for colm in range(col - 1,col + 2):

            decisao = row < 0 or row >= size[0] or colm < 0 or colm >= size[1]
            if row == line and colm == col or decisao:
                continue

            vizin.append((row,colm))
    
    return vizin

pyg.init()

pyg.mixer.music.load("musica/venceu.mpeg")

pyg.mixer.music.play()