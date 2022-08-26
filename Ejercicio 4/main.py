from email.errors import InvalidMultipartContentTransferEncodingDefect
from pila import Pila

if __name__ == "__main__":
    unaPila = Pila()
    opcion = 0
    while opcion != 5:
        print('\n1. Ingresar elemento en la pila 1')
        print('2. Ingresar elemento en la pila 2')
        print('3. Mostrar elemento de la pila 1')
        print('4. Mostrar elemento de la pila 2')
        print('5. Salir')
        opcion = input('\nIngrese la opcion a realizar:')

        if opcion == '1':
            cant = int(input('\nIngrese la cantidad de elementos que desea cargar:'))
            for i in range(cant):
                x = input('Ingrese el elemento a ingresar:')
                unaPila.Insertar1(x)
        
        if opcion == '2':
            cant = int(input('\nIngrese la cantidad de elementos que desea cargar:'))
            for i in range(cant):
                x = input('Ingrese el elemento a ingresar:')
                unaPila.Insertar2(x)
        
        if opcion == '3':
            unaPila.Mostrar1()

        if opcion == '4':
            unaPila.Mostrar2()