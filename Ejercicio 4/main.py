from pila import Pila

if __name__ == "__main__":
    cant = int(input('\nIngrese la cantidad de elementos de las pilas:'))
    unaPila1 = Pila(cant)
    unaPila2 = Pila(cant)
    arreP = [unaPila1, unaPila2]
    opcion = 0
    while opcion != '3':
        print('\n1.Cargar las Pilas:')
        print('2.Mostrar las Pilas:')
        print('3.Salir')
        opcion = input('Ingrese la opcion a realizar:')

        if opcion == '1':
            for i in range(len(arreP)):
                if not (arreP[i].lleno()):
                    print('\nIngrese los elementos para la pila {}'.format(i+1))
                    elem = input('Ingrese el valor a ingresar:')
                    j = arreP[i].retTope()
                    while ((elem != '-1') and (j != cant)):
                        arreP[i].insertar(elem)
                        if j != cant-1:
                            elem = input('Ingrese el valor a ingresar, -1 para finalizar:')
                        j+=1
                else:
                    print('\nLa pila {} esta llena'.format(i+1))
            
        
        if opcion == '2':
            for i in range(len(arreP)):
                print('\nLos componentes de la pila {} son:'.format(i+1))
                arreP[i].mostrar()