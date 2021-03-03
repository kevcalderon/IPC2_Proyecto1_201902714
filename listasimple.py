from listacircularsimple import ListaCircular


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    

class ListaSimpleEnlazada:
    # lista = ListaCircular()
    def __init__(self):
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
    
    def pop(self):
        if self.isVacia() == True:
            print("La lista esta vacia :D")
            
        elif self.primero  == self.ultimo:
            self.primero = None
            self.ultimo = None
            print("Ultimo elemento eliminado, lista vacia :D")
            self.tamanio = self.tamanio - 1
        else:
            validar = True
            temp = self.primero
            while(temp.siguiente != self.ultimo):
                temp = temp.siguiente
            temp.siguiente = None
            self.tamanio = self.tamanio - 1 
            self.ultimo = temp


    def agregarUltimo(self, dato):
        if self.isVacia() == True:
            self.primero = self.ultimo = Nodo(dato)
            self.tamanio = self.tamanio + 1 
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.tamanio = self.tamanio + 1


    def recorrido(self):
        aux = self.primero
        
        while aux != None:
            print(aux.dato)
            # print(aux.dato.datos.__str__())
            aux = aux.siguiente
    


    def buscar(self, nombre):
        aux = self.primero
        encontrado = False

        if self.isVacia == True:
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
        




                

# lista = ListaSimpleEnlazada()
# lista.agregarUltimo(22)
# lista.agregarUltimo(2)
# lista.agregarUltimo(5)
# lista.agregarUltimo(10)

# # lista.recorrido()

# print(lista.buscarPosicion(10))


# # while lista.isVacia() == False:
# #     lista.pop()

# # lista.recorrido()

