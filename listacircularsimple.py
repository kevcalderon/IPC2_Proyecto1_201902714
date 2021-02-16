class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        #punteros de referencia
        self.primero = None
        self.ultimo = None
    
    def isVacia(self):
        return self.primero == None

    def agregarInicio(self, dato):
        if self.isVacia():
            #solo abra un nodo.
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            #le pasa la cabecera al nuevo nodo.
            self.primero = aux
            #crea el enlace del ultimo nodo a la cabecera.
            self.ultimo.siguiente = self.primero
            

    def agregarFinal(self, dato):
        if self.isVacia():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero

    def recorrer(self):
        aux = self.primero
        while aux.siguiente != self.primero:
            print(aux.dato)
            aux = aux.siguiente
        #saliendo del bucle queda pendiente el ultimo nodo volvemos imprimir aux
        print(aux.dato)



lista = ListaCircular()
lista.agregarFinal(10)
lista.agregarFinal(35)
lista.agregarFinal(20)
lista.agregarFinal(7)

lista.agregarInicio(1)

lista.agregarFinal(100)

lista.recorrer()
