import sys
from controladorMatrices import cargarArchivo

def menuPrincipal():
    while True:
        print("")
        print("********************************")
        print("          MENU PRINCIPAL        ")
        print("********************************")
        print("1.Cargar archivo")
        print("2.Procesar archivo")
        print("3.Escribir archivo salida")
        print("4.Mostrar datos del estudiante")
        print("5.Genenar grafica")
        print("0.SALIR")
        try:
            print("")
            opcion = int(input("Elige una opcion: "))
        except ValueError:
            opcion = 7

        if opcion in range (0,6):
            if opcion == 1:
                cargarArchivo()
            elif opcion == 2:
                print("In progress procesar archivo...")
            elif opcion == 3:
                print("In progress escribir archivo salida...")
            elif opcion == 4:
                datosEstudiante()        
            elif opcion == 5:
                print("In progress generar grafica...")
            elif opcion == 0:
                sys.exit()
            else:
                print("")
                print("Opcion invalida, intente de nuevo :D")        
                print("")




def datosEstudiante():
    print("")
    print("KEVIN JOSUÉ CALDERÓN PERAZA")
    print("201902714")
    print("INTRODUCCION A LA PROGRAMACIÓN Y COMPUTACIÓN 2 SECCION 'E'")
    print("INGENIERIA EN CIENCIAS Y SISTEMAS")
    print("4TO. SEMESTRE")
    print("")


if __name__ == "__main__":
    menuPrincipal()

    