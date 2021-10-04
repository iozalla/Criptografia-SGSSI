
import operator
from colorama import Fore, Back, Style
from colorama import init
init()
file = open('texto.txt',mode='r')
text = file.read()
file.close()
text=text.lower()
print("\n"+text+"\n")


letras=["e","a","o","l","s","n","d","r","u","i","t","c","p","m","y","q","b","h","g","f","v","j","ñ","z","x","k","w"]

newtext=""


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

while seguir!="x": #aqui comienza el proceso de sustitucion de letras manual
    #print(str(letrasTexto))
    #print(str(letras))
    print(Fore.GREEN+"\n________________________________________________________\n"+Style.RESET_ALL)
    l1=input("letra o letras a cambiar: ")
    l2=input("letra o letras nueva (tienen que tener el mismo tamaño): ")

    if "." not in l2: #si no hay un punto en el texto se cambia la palabra o letra introducida letra por letra
        letra1=list(l1)
        letra2=list(l2)

        for i in range(0,len(letra1)): #este bucle va sustituyendo cada letra de la palabra metida en el texto
            #if letra2[i] in letras2Cambiadas and letra2=letra2.upper():
            #    continuar=input("esta letra ya la has puesto anteriormente, estas seguro de que quieres volver a hacerlo?")
            text2=text2.replace(letra1[i],letra2[i].upper())
            letras1Cambiadas.append(letra1[i])
            letras2Cambiadas.append(letra2[i])

    else:#si has puesto un punto en la  se cambia la palabra que metes tal cual la has metido en el texto
        text2=text2.replace(l1,l2.replace(".","").upper())

    print(text2)
    #seguir=input("confirmar cambios: ")
    #if seguir!="n":
    #    text=text2

print(text)
