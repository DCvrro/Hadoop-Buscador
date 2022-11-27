import json
import os

def isBigger(str):
    cont = False
    for caracter in str:
        if caracter ==  ' ':
            cont = True
    return cont
def sortSecond(arr):
    return arr[1]

def isSingular(dicc):
    bol = True
    dic = {}
    arr = []
    if(len(dicc) > 1 and type(dicc) == type(arr)):
        bol = False
    elif(len(dicc) == 2 and type(dicc) == type(dic)):
        bol = True
    return bol
def is_valid(f):
    try:
        print(f)
    except KeyError:
        return False


def buscar():
    texto = input('Ingrese lo que desea buscar:')
    big = False

    if(isBigger(texto)):
        big = True
    relevance= []
    pathresult = []
    print('Buscado:',texto)
    with open('bdd.json') as file:
        f = json.load(file)
        
        if(big):
            texto = texto.split()
            for palabras in texto:
                try: 
                    if(isSingular(f[palabras])):
                        tmp = []
                        tmp.append(f[palabras]['text'])
                        tmp.append(f[palabras]['count'])
                        relevance.append(tmp)
                        relevance.sort(key=sortSecond, reverse = True)
                        print(palabras,relevance)
                        get_path(texto,relevance)
                        relevance.clear()
                        continue

                    for duplas in f[palabras]:
                        tmp = []
                        tmp.append(duplas['text'])
                        tmp.append(duplas['count'])
                        relevance.append(tmp)
                        relevance.sort(key=sortSecond, reverse = True)
                    print(palabras, relevance)
                    get_path(texto,relevance)
                    relevance.clear()
                except:
                    print("La palabra ", palabras, 'no está en nuestra base.')
                    continue
        else:
            try:
                if(isSingular(f[texto]) == False):
                    for duplas in f[texto]:
                        try:
                            tmp = []
                            tmp.append(duplas['text'])
                            tmp.append(duplas['count'])
                            relevance.append(tmp)
                            relevance.sort(key=sortSecond, reverse = True)
                        except:
                            print("La palabra ", texto, 'no está en nuestra base.')
                            continue
                else:
                        tmp = []
                        tmp.append(f[texto]['text'])
                        tmp.append(f[texto]['count'])
                        relevance.append(tmp)
                        relevance.sort(key=sortSecond, reverse = True)
                print(texto,relevance)
                get_path(texto,relevance)
            except KeyError:
                print("La palabra ", texto, 'no está en nuestra base.')
    ##################  MENU  ##########

    urls = save_path()
    while(True):
        print('¿Que texto desea abrir? Escriba exit para salir')
        inp = input('Ingrese numero:')

        if(inp == 'exit'):
            break
        elif(inp.isnumeric()):
            path = str(urls[int(inp)-1])
            print(path)
            arc = open(path,'r',encoding='utf8')
            print(arc.read())
            arc.close()            
        else:
            print('Entrada como el pico, reinicia')
        

def get_path(texto, relevance):
    path = save_path()
    for values in relevance: 
        print(values)
        tex = values[0]
        print('url', tex  , ':',path[tex-1]) 


def save_path():
    dir = {}
    i = 0
    for root,dirs,  files in os.walk(r'Wikipedia/Wikipedia/Documentos1'):
        for i in range(i, len(files)) :
            dir[i] = (os.path.abspath(os.path.join(root,files[i])))

    for root, dirs , files in os.walk(r'Wikipedia/Wikipedia/Documentos2'):
        for j in range(0, len(files)) :
            dir[j+i+1] = (os.path.abspath(os.path.join(root,files[j])))
    return dir

buscar()