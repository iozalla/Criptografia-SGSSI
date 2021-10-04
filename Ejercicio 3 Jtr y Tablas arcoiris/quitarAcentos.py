#script rapido para quitar acentos en las vocales


file=open("palabrasEspañol.txt",mode="r", encoding='utf-8')
file2=open("palabrasEspañolSinAcento.txt",mode="w", encoding='utf-8')

data=file.read()

data=data.replace("á","a")
data=data.replace("é","e")
data=data.replace("i","i")
data=data.replace("ó","o")
data=data.replace("ú","u")

file2.write(data)
