
import sys
import re


class info:
    def __init__(self, texto, rep):
        self.texto = texto
        self.rep = rep

    def getTexto(self): 
        return self.texto

    def getRep(self):
        return self.rep
    
    def setTexto(self, texto):
        self.texto = texto
    
    def setRep(self, rep):
        self.rep = rep
    
    def setTextoRepeticion(self, texto , rep):
        self.texto = texto
        self.rep = rep 
    
    def getData(self):
        return (self.texto , self.rep)


def main():
    dPalabras = dict(list())

    for lineas in sys.stdin: 

        tmp = lineas.replace("\n","").split('\t')
        #print(tmp)
        tmp = tmp[0].split()
        #print(tmp)
        tmp[1] = int(tmp[1])
        tmp[2] = int(tmp[2])
        if tmp[0] in dPalabras.keys():
            if(tmp[1]-1 <= len(dPalabras[tmp[0]])-1):
                dPalabras[tmp[0]][tmp[1]-1].setRep(dPalabras[tmp[0]][tmp[1]-1].getRep() +1 )
            elif(dPalabras[tmp[0]][-1].getTexto() == tmp[1]):
                dPalabras[tmp[0]][-1].setRep(dPalabras[tmp[0]][-1].getRep() +1 )
            else:
                dPalabras[tmp[0]].append(info(tmp[1], tmp[2]))


        else: 
            dPalabras[tmp[0]] = []
            dPalabras[tmp[0]].append(info(tmp[1], tmp[2]))

    arc = open('resultados.txt','w')
    arc.write("Word\t[(Document,Count)\n")
    for key in dPalabras.keys(): 
        count = 0
        for datos in dPalabras[key]:
            if count == 0 :   
                arc.write('%s\t%s '%(key,datos.getData()))
                print('%s\t%s '%(key,datos.getData()),end='',sep='') 
                count = 1
            else:
                arc.write(' (%s, %s) '%(datos.getData()))
                print(' (%s, %s) '%(datos.getData()),end='',sep='')

        arc.write("\n")
        print("\n",end='',sep='') 
 

main()
