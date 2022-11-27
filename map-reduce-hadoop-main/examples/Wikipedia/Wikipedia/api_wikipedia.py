#Instalar previamente pip install wikipedia
import wikipedia as wiki

def wikipedia():
    #wiki.languages('es') cambiar lenguaje del documento.
    arr = ['Alexis Sanchez','Argentina','Arturo Vidal','Chile','Cristiano Ronaldo',
            'Diego Portales','Espana','Europa','Philippine Army','War']
    count = 1
    for nombres in arr:
        document = wiki.page(nombres)
        name = nombres + ".txt"
        name.replace("0","")
        print(name)
        if count <= 5:
            ub = 'Documentos1/' + name
            arc = open(ub,"w",encoding='utf-8')
            info = str(count) + " START " + document.content
            arc.write(info)
            count = count + 1
        else:
            ub = 'Documentos2/' + name
            arc = open(ub,"w",encoding='utf-8')
            info = str(count) + " START " + document.content
            arc.write(info)
            count = count + 1
wikipedia()

