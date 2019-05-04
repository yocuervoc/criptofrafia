import sys

def generar_clave(key):

    for i in range(len(key)):
        if key[i]=="i" or key[i]=="j":
            key[i]="ij"
    matriz = []
    for i in range(len(key)):
        if not(key[i] in matriz):
            matriz.append(key[i])
    alfabeto = ["a","b","c","d","e","f","g","h","ij","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(len(alfabeto)):
        if not(alfabeto[i] in matriz):
            matriz.append(alfabeto[i])
    return matriz

def codificar(matriz, mensage):
    mensage=mensage.replace(' ','')
    mensage=list(mensage)
    for i in range(len(mensage)):
        if mensage[i]=="i" or mensage[i]=="j":
            mensage[i]="ij"
    mensage_cifrado=""
    n=0
    while n<len(mensage):
        letra1=matriz.index(mensage[n])
        letra2=matriz.index(mensage[n+1])
        fila1=matriz.index(mensage[n])/5
        fila2=matriz.index(mensage[n+1])/5
        columna1=matriz.index(mensage[n])%5
        columna2=matriz.index(mensage[n+1])%5

        if fila1==fila2 and columna1==columna2:
            mensage_cifrado=mensage_cifrado+mensage[n]+mensage[n+1]

        if fila1==fila2 and columna1!=columna2:

            if columna1 == 4:
                mensage_cifrado=mensage_cifrado+matriz[(letra1-4)]
            else:
                mensage_cifrado=mensage_cifrado+matriz[(letra1+1)]

            if columna2 == 4:
                mensage_cifrado=mensage_cifrado+matriz[(letra2-4)]
            else:
                mensage_cifrado=mensage_cifrado+matriz[(letra2+1)]
            #mensage_cifrado=mensage_cifrado+matriz[(letra1+1)]+matriz[(letra2+1)]

        if columna1==columna2 and fila1 != fila2:

            mensage_cifrado=mensage_cifrado+matriz[(letra1+5)%25]+matriz[(letra2+5)%25]

        if columna1!=columna2 and fila1 != fila2:

            if columna1 > columna2:
                mensage_cifrado=mensage_cifrado+matriz[(letra1-(columna1-columna2))]+matriz[(letra2+(columna1-columna2))]
            else:
                mensage_cifrado=mensage_cifrado+matriz[(letra1+(columna2-columna1))]+matriz[(letra2-(columna2-columna1))]
        n+=2
    return mensage_cifrado


def decodificar(matriz, mensage):
    mensage=mensage.replace(' ','')
    mensage=list(mensage)
    for i in range(len(mensage)):
        if mensage[i]=="i" or mensage[i]=="j":
            mensage[i]="ij"
    mensage_cifrado=""
    n=0
    while n<len(mensage):
        letra1=matriz.index(mensage[n])
        letra2=matriz.index(mensage[n+1])
        fila1=matriz.index(mensage[n])/5
        fila2=matriz.index(mensage[n+1])/5
        columna1=matriz.index(mensage[n])%5
        columna2=matriz.index(mensage[n+1])%5

        if fila1==fila2 and columna1==columna2:
            mensage_cifrado=mensage_cifrado+mensage[n]+mensage[n+1]

        if fila1==fila2 and columna1!=columna2:

            if columna1 == 0:
                mensage_cifrado=mensage_cifrado+matriz[(letra1+4)]
            else:
                mensage_cifrado=mensage_cifrado+matriz[(letra1-1)]
            if columna2 == 0:
                mensage_cifrado=mensage_cifrado+matriz[(letra2+4)]
            else:
                mensage_cifrado=mensage_cifrado+matriz[(letra2-1)]
            #mensage_cifrado=mensage_cifrado+matriz[(letra1+1)]+matriz[(letra2+1)]

        if columna1==columna2 and fila1 != fila2:

            mensage_cifrado=mensage_cifrado+matriz[(letra1-5)%25]+matriz[(letra2-5)%25]

        if columna1!=columna2 and fila1 != fila2:

            if columna1 > columna2:
                mensage_cifrado=mensage_cifrado+matriz[(letra1-(columna1-columna2))]+matriz[(letra2+(columna1-columna2))]
            else:
                mensage_cifrado=mensage_cifrado+matriz[(letra1+(columna2-columna1))]+matriz[(letra2-(columna2-columna1))]
        n+=2
    return mensage_cifrado

print "welcome"
print "instrucciones:"

print "oprima 1 para cifrar"
print "oprima 0 para descifrar"
opcion = input()
print(" ingrese la clave:  ")
clave = sys.stdin.readline().strip()
clave=clave.replace(' ', '')
clave= list(clave)
key = generar_clave(clave)
if opcion == 1:
    print("ingrese le mensaje a cifrar")
    mensage = sys.stdin.readline().strip()
    print "texto cifrado"
    print codificar(key, mensage)
if opcion==0:
    print("ingrese le mensaje a descifrar")
    mensage = sys.stdin.readline().strip()
    print "texto claro"
    print decodificar(key, mensage)
