class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaCircular:
    
    def __init__(self):
        #punteros de referencia
        self.primero = None
        self.ultimo = None
        self.tamanio = 0
    
    def isVacia(self):
        if self.primero == None:
            return True
        else:
            return False

    def getSize(self):
        return self.tamanio


    def agregarInicio(self, dato):
        if self.isVacia():
            #solo abra un nodo.
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
            self.tamanio = self.tamanio + 1
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            #le pasa la cabecera al nuevo nodo.
            self.primero = aux
            #crea el enlace del ultimo nodo a la cabecera.
            self.ultimo.siguiente = self.primero
            self.tamanio = self.tamanio + 1
            # matrices, filas, columnas
            # matrice > filas
            # filas > columnas
            

    def agregarFinal(self, dato):
        if self.isVacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
            self.tamanio = self.tamanio + 1
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero
            self.tamanio = self.tamanio + 1

    def recorrer(self):
        aux = self.primero
        while aux.siguiente:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero: break
    




    def mostrarNombres(self):
        aux = self.primero
        contador = 1
        print("*********************")
        print(" LISTA DE MATRICES")
        print("*********************")
        while aux.siguiente:
            print(str(contador) + ". " + aux.dato.nombre)
            aux = aux.siguiente
            contador = contador + 1
            if aux == self.primero: break



    def buscarPosicion(self, posicion):
        encontrado = False
        if self.isVacia == True:
            print("No hay elementos en la lista :D")
        else:
            if posicion >= 0 and posicion < self.tamanio:
                aux = self.primero

                for i in range(posicion):
                    aux = aux.siguiente
                encontrado = True
                return aux.dato
            else:
                encontrado = False
                print("El indice no valido, esta fuera del rango.")



    def buscar(self, nombre):
        aux = self.primero
        encontrado = False

        if self.isVacia == None:
            print("No hay elementos en la lista :D")
        else:
            contador = 0
            while aux != None:
                if aux.dato.nombre == nombre:
                    return aux.dato
                    # return aux.dato.nombre
                    encontrado = True
                    break
                else:
                    aux = aux.siguiente
                    contador = contador + 1    
            
            if encontrado == False:
                print("El elemento no se encuentra en la lista.")

    def buscarMatriz(self, nombre):
        aux = self.primero
        encontrado = False

        if self.isVacia == None:
            print("No hay elementos en la lista :D")
        else:
            contador = 0
            while aux != None:
                if aux.dato.nombre == nombre:
                    # return aux.dato.nombre
                    return True
                    break
                else:
                    aux = aux.siguiente
                    contador = contador + 1    
            
            if encontrado == False:
                return False
                print("El elemento no se encuentra en la lista.")


    # def __str__(self):
    #     aux = self.primero
    #     arreglo = []
    #     while aux.siguiente:
    #         arreglo.append(aux.dato)
    #         aux = aux.siguiente
    #         if aux == self.primero:
    #             break
    #     return arreglo


  



# lista = ListaCircular()
# lista.agregarFinal(10)
# lista.agregarFinal(35)
# lista.agregarFinal(20)
# lista.agregarFinal(7)

# lista.agregarInicio(1)

# lista.agregarFinal(100)

# lista.recorrer()
