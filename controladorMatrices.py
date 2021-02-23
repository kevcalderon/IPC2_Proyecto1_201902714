from xml.dom import minidom
import xml.etree.cElementTree as ET

from listacircularsimple import ListaCircular
from listasimple import ListaSimpleEnlazada 

class Matriz:
    def __init__(self, nombre, fila, columna, datos):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.datos = datos
        

listaMatriz  = ListaCircular()
listaGeneral = ListaSimpleEnlazada()

def getText(nodeList):
    rc = []
    for node in nodeList:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return "".join(rc)


def validacionDatos(posicionX,posicionY,n,m):
    if (posicionX > n) or (posicionY > m):
        return False
    else:
        return True


def cargarArchivo():
    nombre = input("Escribe la ruta del archivo: ")
    archivo = minidom.parse(nombre)
    matriz = archivo.getElementsByTagName("matriz")
    contador = 0
    

    for i in matriz:        
        # conteoDatos = list()
   
        nombre = i.getAttribute('nombre')
        n = int(i.getAttribute('n'))
        m = int(i.getAttribute('m'))
        #accede a la etiqueta hija de la matriz
        dato = i.getElementsByTagName("dato")
        tamanio = n*m
        contador = 0
        ingresada = True

        print("nombre: ", nombre)
        print("tamanioN: ", n)
        print("tamanioM: ", m)
        print("")
        
        #conteo de datos que hay en la matriz
        for x in dato:
            contador = contador + 1

        if contador == tamanio:
            for posicion in dato:
                
                posicionX = int(posicion.getAttribute('x'))
                posicionY = int(posicion.getAttribute('y'))
                valor = int(getText(posicion.childNodes))
                #valor = dato[contador-1].childNodes[0].data
     
                if validacionDatos(posicionX, posicionY, n, m) == False:
                    print("La posición en X o Y son mayores al tamaño de la matriz.")
                    print("")
                    ingresada = False
                    break
                else:
                    #agregar posiciones a lista
                    print("posicionX: ", posicionX)
                    print("posicionY: ", posicionY)
                    print("dato: ", valor)
                    listaMatriz.agregarFinal(valor)
                    print("*********")
                    contador = 0
                    tamanio = 0
                    
                
            if ingresada == True:
                matriz = Matriz(nombre, n, m, listaMatriz)
                listaGeneral.agregarUltimo(matriz)
                print("Matriz ingresada correctamente :D")
                print("")
                print("-----------------") 
                print("*********") 
                #agregar objeto!

        elif contador < tamanio:
            print("")
            print("Error con la matriz: ",  nombre)
            print("La matriz es de tamaño: ", str(tamanio) + " Y los datos son menores al tamaño :D")
            print("")
            nombre = None
            tamanio = 0
        elif contador > tamanio:
            print("")
            print("Error con la matriz: ", nombre)
            print("La matriz es de tamaño:", str(tamanio) + " Y los datos son mayores al tamaño :D")
            print("")
            nombre = None
            tamanio = 0
               
    listaGeneral.recorrido()


def procesarArchivo():
    pass


def archivoSalida():
    pass

def generarGrafica():
    pass