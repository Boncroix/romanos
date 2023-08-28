class RomanNumber:
    def __init__(self, entrada):
        if isinstance(entrada, int):
            self.valor = entrada
            self.cadena = self.convertir_romano()
        elif isinstance(entrada, str):
            self.cadena = entrada
            self.valor = self.romano_a_entero()
        else:
            raise TypeError('Solo acepto enteros o cadenas')

    def convertir_romano(self):  # entrada tiene que ser una cadena
        numero = str(self.valor)
        millares = ['', 'M', 'MM', 'MMM']
        centenas = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        decenas = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        unidades = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        lista = list(numero)
        for numero in range(len(lista), 4):
            lista.insert(0, 0)

        romano = millares[int(lista[0])] + centenas[int(lista[1])] + \
            decenas[int(lista[2])] + unidades[int(lista[3])]

        return romano

    def romano_a_entero(self):
        romanos = self.cadena
        romanos.upper()
        digitos_romanos = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Comprobamos que la letra no está repetida más de 3 veces y que todas las letras estan en el diccionario
        for letra in romanos:
            letra_repetida = romanos.count(letra)
            if letra_repetida > 3:
                raise ValueError(
                    f'ERROR: Numero romano no valido la letra {letra} repetida más de 3 veces')

            if letra not in digitos_romanos:
                raise ValueError(
                    f'ERROR: {letra} no es un dígito romano válido (I, V, X, L, C, D, M)')

        lista_romanos = list(romanos)   # Convierto la entrada en una lista
        lista_romanos.reverse()         # Giramos la lista
        resultado = 0                   #
        # Inicializamos variables que vamos a utilizar en le while
        numero_anterior = 0
        resta = False                   #

        # Comprobamos si resta o suma o si la resta no es posible
        while len(lista_romanos) != 0:
            numero = digitos_romanos[lista_romanos[0]]

            if numero >= numero_anterior:
                resultado += numero
                numero_anterior = numero
                resta = False
            elif (numero_anterior // numero == 5 or numero_anterior // numero == 10) and not resta:
                resultado -= numero
                resta = True
            else:
                raise ValueError('ERROR: Numero romano no valido')

            lista_romanos.remove(lista_romanos[0])
        return resultado

    def __str__(self):
        return self.cadena

    def __repr__(self):
        return f'Objeto: {self.__str__()}'

    def __eq__(self, otro):
        return self.valor == otro or self.cadena == otro


numero = RomanNumber(1123)
print(numero.valor)
print(numero.cadena)
