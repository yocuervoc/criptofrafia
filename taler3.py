import numpy as np
import sys
def codificar(key, mensaje):
    alfabeto = ["a","b","c","d","e","f","g","h","i", "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    mensaje=mensaje.replace(' ','')
    mensaje=list(mensaje)
    if len(mensaje)%2 !=0:
        mensaje+="x"
    mensaje_cifrado=""
    n=0
    while n<len(mensaje):

        c1=alfabeto.index(mensaje[n])
        c2=alfabeto.index(mensaje[n+1])
        m= np.dot([c1,c2], key)
        m1=m[0]%26
        m2=m[1]%26
        mensaje_cifrado+=alfabeto[m1]+alfabeto[m2]
        n+=2
    return mensaje_cifrado

def decodificar(key, mensaje):
    alfabeto = ["a","b","c","d","e","f","g","h","i", "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    mensaje=mensaje.replace(' ','')
    mensaje=list(mensaje)
    if len(mensaje)%2 !=0:
        mensaje+="x"
    mensaje_claro=""
    plainText = ""
    detK =  (int(key[0][0] * key[1][1]) - int(key[1][0] * key[0][1])) % 26

    if detK == 0:
        print "Matriz no inverible"
        sys.exit()
    else:
        inversa = [[key[1][1]]]
        inversa[0].append(-key[0][1] % 26)
        inversa.append([-key[1][0] % 26])
        inversa[1].append(key[0][0])
        for i in range(len(inversa)):
			for j in range(len(inversa)):
				inversa[i][j] = inversa[i][j] * (1 / detK)

    n=0
    while n<len(mensaje):
        c1=alfabeto.index(mensaje[n])
        c2=alfabeto.index(mensaje[n+1])
        m= np.dot([c1,c2],inversa)
        m1=m[0]%26
        m2=m[1]%26
        mensaje_claro+=alfabeto[m1]+alfabeto[m2]
        n+=2
    return mensaje_claro

print("bienvenido")
print "Por favor ingrese los datos de llave solicitados a continuacion"
print ("ingrese el elemto 1,1 de la llave")
a= int(input())
print ("ingrese el elemto 1,2 de la llave")
b= int(input())
print ("ingrese el elemto 2,1 de la llave")
c= int(input())
print ("ingrese el elemto 2,1 de la  llave")
d= int(input())
matrix= [[a,b],[c,d]]

print "oprima 0 para encriptar"
print "oprima 1 para desencriptar"
opcion= int(input())
if opcion == 0:
    print("ingrese el mensaje a codificar")
    mensaje = sys.stdin.readline().lower().strip().replace(' ','')
    print codificar(matrix, mensaje)
if opcion == 1:
    print("ingrese el mensaje a decodificar")
    mensaje = sys.stdin.readline().lower().strip().replace(' ','')
    print decodificar(matrix, mensaje)
