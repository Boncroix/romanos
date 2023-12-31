class RomanNumber:
    def __init__(self, entrada):
        if isinstance(entrada, int):
            self.valor = entrada
            self.cadena = self.convertir_a_romano()
        elif isinstance(entrada, str):
            self.cadena = entrada
            self.valor = self.romano_a_entero()
        else:
            raise TypeError('Solo acepto enteros o cadenas')

    def convertir_a_romano(self):
        numero = self.valor
        if type(numero) != int:
            raise ValueError(
                f"Error: debes introducir un número entero ({numero})")

        # validar el valor del número
        if not (0 < numero < 4000):
            raise ValueError(
                f"Error: el número debe estar entre 1 y 3999 ({numero})")

        conversores = [
            ["", "M", "MM", "MMM"],
            ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
        ]

        divisores = [1000, 100, 10, 1]

        resultado = ""
        contador = 0

        for divisor in divisores:
            cociente = (numero // divisor)
            numero = numero % divisor
            resultado = resultado + conversores[contador][cociente]
            contador = contador + 1

        return resultado

    def romano_a_entero(self):
        romano = self.cadena
        romano = romano.upper()

        digitos_romanos = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        if not isinstance(romano, str):
            raise TypeError(
                'ERROR: tiene que ser un número romano en formato cadena de texto')

        resultado = 0
        anterior = 0
        super_anterior = 0

        for letra in romano:

            letra_repetida = romano.count(letra)
            if letra_repetida > 3:
                raise ValueError(
                    f'ERROR: Numero romano no valido la letra {letra} repetida más de 3 veces')

            if letra not in digitos_romanos:
                raise ValueError(
                    f'ERROR: {letra} no es un dígito romano válido (I, V, X, L, C, D, M)')

            actual = digitos_romanos[letra]

            if anterior < actual:
                # comprobar que la resta es posible
                # el orden de magnitud no es mayor de uno

                if anterior > 0 and len(str(actual)) - len(str(anterior)) > 1:
                    raise ValueError(
                        f"ERROR: resta no posible (ant: {anterior}, act: {actual})")

                if anterior > 0 and actual > super_anterior > 0:
                    raise ValueError(f'ERROR: dos restas consecutivas')

                # deshacer la suma (que hemos hecho en la iteración anterior)
                # DCI --- DC
                resultado = resultado - anterior
                # DC(IV) 600 + 4 = 600 + (5 - 1) = resultado + (actual - anterior)
                # sumar el valor actual, pero restando el anterior
                resultado = resultado + (actual - anterior)
            else:
                resultado = resultado + actual

            super_anterior = anterior
            anterior = actual

        return resultado

    def __str__(self):
        return self.cadena

    def __repr__(self):
        return f'Objeto: {self.__str__()}'

    # Operadores logicos

    def __eq__(self, otro):  # operador igual
        return self.valor == otro or self.cadena == otro

    def __ne__(self, otro):  # operador desigual
        # Núnero romano
        if isinstance(otro, RomanNumber):
            return self.valor != otro.valor
        # entero
        if isinstance(otro, int):
            return self.valor != otro
        # cadena
        if isinstance(otro, str):
            return self.cadena != otro
        raise ValueError(
            'Solo puedo comparar numeros romanos, enteros o cadenas')

    def __lt__(self, otro):  # menor que
        # Núnero romano
        if isinstance(otro, RomanNumber):
            return self.valor < otro.valor
        # entero
        if isinstance(otro, int):
            return self.valor < otro
        # cadena
        if isinstance(otro, str):
            return self.cadena < otro
        raise ValueError(
            'Solo puedo comparar numeros romanos, enteros o cadenas')

    def __le__(self, otro):  # menor o igual que
        # Núnero romano
        if isinstance(otro, RomanNumber):
            return self.valor <= otro.valor
        # entero
        if isinstance(otro, int):
            return self.valor <= otro
        # cadena
        if isinstance(otro, str):
            return self.cadena <= otro
        raise ValueError(
            'Solo puedo comparar numeros romanos, enteros o cadenas')

    def __gt__(self, otro):  # mayor que
        # Núnero romano
        if isinstance(otro, RomanNumber):
            return self.valor > otro.valor
        # entero
        if isinstance(otro, int):
            return self.valor > otro
        # cadena
        if isinstance(otro, str):
            return self.cadena > otro
        raise ValueError(
            'Solo puedo comparar numeros romanos, enteros o cadenas')

    def __ge__(self, otro):  # mayor o igual
        # Núnero romano
        if isinstance(otro, RomanNumber):
            return self.valor >= otro.valor
        # entero
        if isinstance(otro, int):
            return self.valor >= otro
        # cadena
        if isinstance(otro, str):
            return self.cadena >= otro
        raise ValueError(
            'Solo puedo comparar numeros romanos, enteros o cadenas')

    # Operadores aritméticos __add__ funcion normal para sumar __radd__ igual pero le da la vuelta a los valores

    def __add__(self, otro):  # sumar
        # Núnero romano
        if isinstance(otro, RomanNumber):
            # devolvemos siempre un número romano llamando a RomanNumber
            return RomanNumber(self.valor + otro.valor)
        # entero
        if isinstance(otro, int):
            return RomanNumber(self.valor + otro)
        # cadena
        if isinstance(otro, str):
            return self.valor + RomanNumber(otro).valor
        raise ValueError(
            'Solo puedo sumar RomanNumber, cadena o entero')

    def __radd__(self, otro):   # Suma en orden inverso __radd__ se puede girar por que es conmutativo
        return self.__add__(otro)

    def __sub__(self, otro):    # restar
        resta = 0
        # Núnero romano
        if isinstance(otro, RomanNumber):
            resta = self.valor - otro.valor
        # entero
        elif isinstance(otro, int):
            resta = self.valor - otro
        # cadena
        elif isinstance(otro, str):
            resta = self.valor - RomanNumber(otro).valor
        else:
            raise ValueError(
                'Solo puedo restar RomanNumber, cadena o entero')

        if resta <= 0:
            raise ValueError(
                'Un número romano no puede ser negativo. No puedo hacer la resta.')
        else:
            return RomanNumber(resta)

    def __rsub__(self, otro):   # Restar en orden inverso __rsub__ no se puede girar
        resta = 0
        # Núnero romano
        if isinstance(otro, RomanNumber):
            resta = otro.valor - self.valor
        # entero
        elif isinstance(otro, int):
            resta = otro - self.valor
        # cadena
        elif isinstance(otro, str):
            resta = RomanNumber(otro).valor - self.valor
        else:
            raise ValueError(
                'Solo puedo restar RomanNumber, cadena o entero')

        if resta <= 0:
            raise ValueError(
                'Un número romano no puede ser negativo. No puedo hacer la resta.')
        else:
            return RomanNumber(resta)
