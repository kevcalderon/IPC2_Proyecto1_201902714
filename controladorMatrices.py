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
        
class MatrizFrecuencia:
    def __init__(self, nombre, n, m, g, datos):
        self.nombre = nombres
        self.n = n
        self.m = m
        self.g = g
        self.datos = datos

class MatrizBinaria:
    def _init__(self, dato):
        self.dato = dato

listaFrecuencia = ListaSimpleEnlazada()
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
            if ingresada == True:
                matriz = Matriz(nombre, n, m, listaTemp)
                listaGeneral.agregarFinal(matriz)
                print("---------------------------------")
                print("Nombre: " + nombre)
                print("Matriz ingresada correctamente :D")
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


def procesarArchivo():
    if listaGeneral.isVacia() == True:
        print("La lista esta vacia no se puede realizar la operacion :D")
    else:
        listaDatos = ListaSimpleEnlazada()
        listaTemp = [] #lista auxiliar
        listaTemp2 = [] 
        # listaTemp2 = ListaSimpleEnlazada()
        listaBinaria = [] #lista binaria
        temp = 1
        noFila = 0
        # print(listaGeneral.getSize())

        # recorre cada matriz
        for x in range(listaGeneral.getSize()):
            # obtengo cada matriz en cada x.
            matriz = listaGeneral.buscarPosicion(x)
            # parametros
            nombre = matriz.nombre + "_Salida"
            noColumna = matriz.columna
            # recorre cada dato de la matriz para obtener la binaria
            for dato in range(0,(int(matriz.fila)*int(matriz.columna))):
                valor = matriz.datos.buscarPosicion(dato)
                
                listaTemp2.append(valor)
                if valor >= 1:
                    listaTemp.append(1)
                elif valor == 0:
                    listaTemp.append(0)
                if temp == matriz.columna:
                    # CREAR LA LISTA BINARIA
                    listaBinaria.append(listaTemp)
                    # AGREGA LISTA DENTRO DE LISTA CIRCULAR
                    listaDatos.agregarUltimo(listaTemp2)
                    noFila += 1
                    temp=0
                    listaTemp = []
                    listaTemp2 = []
                temp+=1

            print("")
            print("Nombre: " + matriz.nombre)
            print("Matriz de patrones de acceso realizada :D")
            print(listaBinaria)
            # listaBinaria = []
            #vaciar lista binaria!!!!!  
            
            lista1temp = []
            lista2temp = []
            listaCircular = []
            listaCirculartemp = []
            listaCirculartemp2 = []
            contador=0
            listReducida = ListaSimpleEnlazada() 

            for x in range(0,len(listaBinaria)):
                lista1temp.append(listaBinaria[x])
                for j in range(contador+1,len(listaBinaria)):
                    lista2temp.append(listaBinaria[j])
                    if lista1temp == lista2temp:
                        listaCircular.append(x)
                        listaCircular.append(j)
                        listaCirculartemp2 = listaCirculartemp2 + listaDatos.buscarPosicion(j)
                        listaCirculartemp = listaCirculartemp + listaDatos.buscarPosicion(j)
                        print("fila " + str(x) + " suma con fila: " + str(j))

                    else:
                        print("fila no coincide:" + str(x))
                        # listReducida.agregarUltimo(listaDatos.buscarPosicion(x))
                    lista2temp = []
                contador +=1
                lista1temp = []

            print("")
            print("**************************")

            listaBinaria.clear()
            listaCircular.clear()
            listaCirculartemp.clear()
            listaCirculartemp2.clear()
            

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
        
        nombre = "Nombre = " + matriz.nombre
        tamanio = int(matriz.fila * matriz.columna)
        n = "Fila = " + str(matriz.fila)
        m = "Columna = " + str(matriz.columna)

        data = nombre + "\n"
        data = data + n + "\n"
        data = data + m 

        dot.node(data, shape='component')


        # dot.node(name=str(matriz.datos.buscarPosicion(x)), shape='circle')
        # creacion de nodos!
        for x in range(tamanio):
            # El primer nodo es un nombre o id, el segundo es un valor, y el tercero es una forma
            dot.node(str(x), label=str(matriz.datos.buscarPosicion(x)), shape="circle")
       

        for i in range(int(matriz.fila)):
            for j in range(int(matriz.columna)):
                # si la columna es igual a tama;io de la columna crea otra union hacia el nodo siguiente.
                if j<int(matriz.columna)-1:
                    dot.edge(str(i+(int(matriz.columna)*j)), str(i+(int(matriz.columna)*(j+1))))


        dot.render(matriz.nombre, format='png', view=True)
        print("")
        print("Grafica generada con exito :D")
        print("")
    