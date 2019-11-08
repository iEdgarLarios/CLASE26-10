"""
Nombre: SolucionEjercicio.py
Objetivo: Resolver ejercicio 2
Autor: Edgar Ulises Larios Diaz
Fecha: 26 de octubre de 2019
"""
def main():
    a = int(input("Ingresa sueldo de trabajador:"))
    b = int(input("Que categoria es?"))
    if int(b)== 1:
        sueldo= ((a*.15)+a)
        print(str(sueldo)+ " nuevo sueldo")
    elif int(b)==2:
        sueldo= ((a*.10)+a)
        print(str(sueldo)+ " nuevo sueldo")
    elif int(b)==3:
        sueldo= ((a*.8)+a)
        print(str(sueldo)+ " nuevo sueldo")
    elif int(b)==4:
        sueldo= ((a*.7)+a)
        print(str(sueldo)+ " nuevo sueldo")
    else:
        print("Sin categoria")
    print("Adios..")
        
if __name__ == "__main__":
    main()