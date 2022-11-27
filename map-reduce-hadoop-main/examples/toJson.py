import json
import sys


dicc = {} 
mat= list() 
fl = True  
arr = [0,0,0,0,0]
for line in sys.stdin:
    if(fl):
        fl = False
        continue
    else:
        info = line.strip().split()
        if(len(info) == 3):
            info[1] = info[1].replace('(','') 
            info[1] = info[1].replace(',','')
            info[2] = info[2].replace(')','')
            dicc[info[0]] = {'text':int(info[1]), 'count':int(info[2])}
        else:
            tmp = list()
            for values in info: 
                if (values == info[0]):
                    continue
                else:
                    values = values.replace('(','')
                    values = values.replace(')','')
                    values = values.replace(',','')
                    tmp.append(values)
            imp = 0
            count = 1
            texto = 0
            for datos in tmp:
                if(count%2 != 0):
                    texto = datos # valor en el que estoy parado
                    count = 2
                else:
                    contador = datos
                    dicaux = {'text':int(texto), 'count':int(contador)}
                    dicc.setdefault(info[0],[]).append(dicaux)
                    count = 1 


outf = open('bdd.json', 'w')
json.dump(dicc, outf , indent= 3 , sort_keys= False)
outf.close()

        
