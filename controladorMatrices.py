from xml.dom import minidom
import xml.etree.cElementTree as ET
from graphviz import Digraph
from listacircularsimple import ListaCircular
from listasimple import ListaSimpleEnlazada 

# import os
# os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin'

class Matriz:
    def __init__(self, nombre, fila, columna, datos):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.datos = datos
        

# listaMatriz  = ListaSimpleEnlazada()
listaGeneral = ListaCircular()
# listaDatosGeneral = ListaSimpleEnlazada()


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
    listaTemp = ListaSimpleEnlazada()
    

    for i in matriz:        
        # conteoDatos = list()
   
        nombre = i.getAttribute('nombre')
        n = int(i.getAttribute('n'))
        m = int(i.getAttribute('m'))
        #accede a la etiqueta hija de la matriz
        dato = i.getElementsByTagName("dato")
        # crea la lista enlazada por cada matriz
        listaTemp = ListaSimpleEnlazada()
        tamanio = n*m
        contador = 0
        i = 0
        
        ingresada = True

        # print("nombre: ", nombre)
        # print("tamanioN: ", n)
        # print("tamanioM: ", m)
        # print("")
        
        #conteo de datos que hay en la matriz
        for x in dato:
            contador = contador + 1

        if contador == tamanio:
            for posicion in dato:
                
                posicionX = int(posicion.getAttribute('x'))
                posicionY = int(posicion.getAttribute('y'))

                valor = int(getText(posicion.childNodes))   
                # valor = dato[i-1].childNodes[0].data
     
                if validacionDatos(posicionX, posicionY, n, m) == False:
                    print("La posición en X o Y son mayores al tamaño de la matriz.")
                    print("")
                    ingresada = False
                    break
                else:
                    #agregar posiciones a lista
                    # print("posicionX: ", posicionX)
                    # print("posicionY: ", posicionY)
                    # print("dato: ", valor)
                    # for x in dato[0,4]
                    listaTemp.agregarUltimo(valor)
                    
                    # listaDatosGeneral.agregarUltimo(valor)
                    
                    
                    # print("*********")
   
            if ingresada == True:
                matriz = Matriz(nombre, n, m, listaTemp)
                listaGeneral.agregarFinal(matriz)

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

        # while listaTemp.isVacia() == False: 
        #     listaTemp.pop()  


    # listaGeneral.recorrido()
    # acceder al nodo, con propiedades
    prueba1 = listaGeneral.buscar("Ejemplo1")
    # # prueba1.datos.__str__()

    # # listaGeneral.getSize()
    print(prueba1.nombre)
    prueba1.datos.recorrido()
    # listaGeneral.recorrido()
    
    # listaGeneral.buscar("Ejemplo2")
    # listaGeneral.buscar("Ejemplo4")

    # print(listaMatriz.__str__())
   
    
    # listaGeneral.getSize()
    # listaGeneral.buscar(0).nombre


def procesarArchivo():
    pass


def archivoSalida():
    pass

def generarGrafica():
    if listaGeneral.isVacia() == True:
        print("")
        print("No se puede graficar, no hay elementos en la lista :D")
        print("")
    else:
        listaTemp = []
        listaGeneral.mostrarNombres()
        print("")
        nombre = input("Escribe el nombre de la matriz que quieres graficar: ")

        matriz = listaGeneral.buscar(nombre)

        dot = Digraph(name='dibujo', encoding='UTF-8', format='pdf')
        dot.attr(rankdir='TB', layout='dot', shape='circle')
        
        nombre = matriz.nombre
        tamanio = int(matriz.fila * matriz.columna)
        m = "n=" + str(matriz.fila)
        n = "m=" + str(matriz.columna)

        dot.node(name=nombre, shape='circle')
        dot.node(name=m, shape='doublecircle')
        dot.node(name=n, shape='doublecircle')

        dot.edge(nombre, m)
        dot.edge(nombre, n)
        

        # dot.node(name=str(matriz.datos.buscarPosicion(x)), shape='circle')
        for x in range(tamanio):
            # El primer nodo es un nombre o id, el segundo es un valor, y el tercero es una forma
            dot.node(str(x), label=str(matriz.datos.buscarPosicion(x)), shape="circle")
                

        # for p in range(tamanio):
        #     dot.edge(str(matriz.datos.buscarPosicion(p)), str(matriz.datos.buscarPosicion(p+matriz.fila+1)))

        dot.render(matriz.nombre, format='png', view=True)
        print("")
        print("Grafica generada con exito :D")
        print("")
    