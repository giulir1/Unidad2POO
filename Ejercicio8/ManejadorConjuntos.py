from conjunto import conjunto


class manejador:
    __conj1 = None
    __conj2 = None
    __conj3 = None

    def __init__(self, c1=[1, 2, 4, 7, 9], c2=[1, 4, 6, 7, 2, 8], c3=[1, 8, 6, 7, 2, 4]):   # Datos de prueba
        self.__conj1 = conjunto(c1)
        self.__conj2 = conjunto(c2)
        self.__conj3 = conjunto(c3)

    def muestraListas(self):
        print('CONJUNTO 1: {}'.format(self.__conj1))
        print('CONJUNTO 2: {}'.format(self.__conj2))
        print('CONJUNTO 3: {}\n'.format(self.__conj3))

    def punto1(self):
        self.muestraListas()
        opcion = input('1 - Sumar CONJUNTO1+CONJUNTO2\n2 - Sumar CONJUNTO1+CONJUNTO3\n3 - Sumar CONJUNTO2+CONJUNTO3\nOpción: ')
        while (opcion != '1') and (opcion != '2') and (opcion != '3'):
            print('ERROR. Ingrese una opción válida.')
            opcion = input('1 - Sumar CONJUNTO1+CONJUNTO2\n2 - Sumar CONJUNTO1+CONJUNTO3\n3 - Sumar CONJUNTO2+CONJUNTO3\nOpción: ')
        if opcion == '1':
            print('Suma CONJUNTO1 + CONJUNTO2 = {}'.format(self.__conj1 + self.__conj2))
        elif opcion == '2':
            print('Suma CONJUNTO1 + CONJUNTO3 = {}'.format(self.__conj1 + self.__conj3))
        elif opcion == '3':
            print('Suma CONJUNTO2 + CONJUNTO3 = {}'.format(self.__conj2 + self.__conj3))

    def punto2(self):
        self.muestraListas()
        opcion = input('1 - Restar CONJUNTO1-CONJUNTO2\n2 - Restar CONJUNTO1-CONJUNTO3\n3 - Restar CONJUNTO2-CONJUNTO3\nOpción: ')
        while (opcion != '1') and (opcion != '2') and (opcion != '3'):
            print('ERROR. Ingrese una opción válida.')
            opcion = input('1 - Restar CONJUNTO1-CONJUNTO2\n2 - Restar CONJUNTO1-CONJUNTO3\n3 - Restar CONJUNTO2-CONJUNTO3\nOpción: ')
        if opcion == '1':
            print('Resta CONJUNTO1 - CONJUNTO2 = {}'.format(self.__conj1 - self.__conj2))
        elif opcion == '2':
            print('Resta CONJUNTO1 - CONJUNTO3 = {}'.format(self.__conj1 - self.__conj3))
        elif opcion == '3':
            print('Resta CONJUNTO2 - CONJUNTO3 = {}'.format(self.__conj2 - self.__conj3))

    def punto3(self):
        self.muestraListas()
        opcion = input('1 - Comparar CONJUNTO1==CONJUNTO2\n2 - Comparar CONJUNTO1==CONJUNTO3\n3 - Comparar CONJUNTO2==CONJUNTO3\nOpción: ')
        while (opcion != '1') and (opcion != '2') and (opcion != '3'):
            print('ERROR. Ingrese una opción válida.')
            opcion = input('1 - Comparar CONJUNTO1==CONJUNTO2\n2 - Comparar CONJUNTO1==CONJUNTO3\n3 - Comparar CONJUNTO2==CONJUNTO3\nOpción: ')
        if opcion == '1':
            if self.__conj1 == self.__conj2:
                print('Los conjuntos 1 y 2 son iguales.')
            else:
                print('Los conjuntos 1 y 2 no son iguales.')
        elif opcion == '2':
            if self.__conj1 == self.__conj3:
                print('Los conjuntos 1 y 3 son iguales.')
            else:
                print('Los conjuntos 1 y 3 no son iguales.')
        elif opcion == '3':
            if self.__conj2 == self.__conj3:
                print('Los conjuntos 2 y 3 son iguales.')
            else:
                print('Los conjuntos 2 y 3 no son iguales.')
