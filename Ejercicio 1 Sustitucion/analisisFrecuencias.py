
import operator
from colorama import Fore, Back, Style
from colorama import init
init()
file = open('texto.txt',mode='r', encoding="UTF-8")
text=original = file.read()
file.close()
text=text.lower()
print("\n"+text+"\n")
cambiosRealizados={}
letras=["e","a","o","l","s","n","d","r","u","i","t","c","p","m","y","q","b","h","g","f","v","j","ñ","z","x","k","w"]

newtext=""

def estadisticas(texto):#esta funcion sirve para mostrar las palabras de 2, 3 y cuatro letras que mas se repiten
    stats={1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{},10:{},11:{},12:{},13:{},14:{},15:{},16:{},17:{},18:{},19:{},20:{},21:{},22:{},23:{},24:{},25:{},26:{},27:{}}

    texto=texto.split(" ")
    for palabra in texto:
        size=len(palabra)
        if palabra in stats[size]:
            stats[size][palabra]+=1
        else:
            stats[size][palabra]=1
    print("\n____________________________________________")
    print({k: v for k, v in sorted(stats[1].items(), key=lambda item: item[1],reverse=True)})
    print({k: v for k, v in sorted(stats[2].items(), key=lambda item: item[1],reverse=True)})
    print({k: v for k, v in sorted(stats[3].items(), key=lambda item: item[1],reverse=True)})
    print("____________________________________________\n")

def getFrecuencias():
    letrasTexto={}
    total=0
    for caracter in text:
        if caracter.isalpha() or caracter=="ñ":
            total+=1
            #print(caracter)
            if caracter in letrasTexto:
                letrasTexto[caracter]+=1
            else:
                letrasTexto[caracter]=1
    letrasSorted=dict(sorted(letrasTexto.items(), key=operator.itemgetter(1),reverse=True))
    letrasTexto=list(letrasSorted.keys())
    return letrasSorted,letrasTexto

letrasSorted,letrasTexto=getFrecuencias()

seguir=0
print(str(letrasTexto),"letras mas encontradas en el texto")
print(str(letras),"letras mas frecuentes del alfabeto español")
seguir=input("SUSTITUIR letras mas usadas?\n\n").upper()


for caracter in letrasTexto:
    if seguir!="N":
        if caracter.isalpha() or caracter=="ñ" : #se comprueba si el caracter es una letra o una ñ en cuyo caso se procedera a cambiar la letra del por la equivalente mas usada en el idioma español
            if caracter in text:
                indice=letrasTexto.index(caracter)
                text=text.replace(caracter,letras[indice].upper())

                print(text+"|||||"+letras[indice].upper()+caracter+"\n___________")
                seguir=input("seguir? ").upper()
        else:
            newtext=newtext+caracter
    else:
        break
        seguir=""
text2=text
l1=""
while l1!="stop": #aqui comienza el proceso de sustitucion de letras manual
    #print(str(letrasTexto))
    #print(str(letras))
    print(Fore.GREEN+"\n________________________________________________________\n"+Style.RESET_ALL)
    l1=input("letra o letras a cambiar: ")
    l2=input("letra o letras nueva (tienen que tener el mismo tamaño): ")
    if l1=="stop" or l2 =="stop":
        print("asdasd")
        break

    if "." not in l2: #si no hay un punto en el texto se cambia la palabra o letra introducida letra por letra
        letra1=list(l1)
        letra2=list(l2)

        for i in range(0,len(letra1)): #este bucle va sustituyendo cada letra de la palabra metida en el texto
            if letra1[i]!=letra1[i].upper():
                text2=text2.replace(letra1[i],letra2[i].upper())
                cambiosRealizados[letra1[i].lower()]=letra2[i].upper()


    else:#si has puesto un punto en la  se cambia la palabra que metes tal cual la has metido en el texto
        text2=text2.replace(l1,l2.replace(".","").upper())
    estadisticas(text2)
    print(text2)
    #seguir=input("confirmar cambios: ")
    #if seguir!="n":
    #    text=text2
out = open('output.txt',mode='w', encoding="UTF-8")
out.write(str(text2))
out.write(str(cambiosRealizados))


#'y': 8324, 'a': 4765, 'o': 512, 'e': 46,
#'de': 8984, 'la': 4993, 'en': 3956, 'el': 3793, 'no': 2859, 'se': 2380, 'su': 1857, 'le': 1799, 'lo': 1795, 'me': 1153, 'es': 961, 'si': 932, 'un': 893,
#que': 10335, 'los': 2135, 'con': 2046, 'por': 1900, 'las': 1484, 'del': 1117
