import hashlib
import os
def p1():
    for i in range (1,46):
        try:
            a_file = open("imagen"+str(i)+".jpg", "rb")

            content = a_file.read()
            hash=hashlib.md5(content).hexdigest()
            print(str(i)+hash)
            if hash=="e5ed313192776744b9b93b1320b5e268":
                print("Encontrado"+"imagen"+str(i)+".jpg")
        except:
            pass




def p2():
    hashOriginal=input("que hash buscas: ")
    for filename in os.listdir("imagenes"):
        try:
            a_file = open("imagenes/"+filename, "rb")

            content = a_file.read()
            hash=hashlib.md5(content).hexdigest()

            if hash=="e5ed313192776744b9b93b1320b5e268":
                print("Encontrado: "+filename,hash)
        except Exception as e:
            print(e)
            pass

p2()
