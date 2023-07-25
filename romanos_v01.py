def pedir_numero(mensaje, minimo, maximo):
    numero_correcto = False
    while not numero_correcto:
        numero = input(mensaje)
        numero_correcto = es_numero_entero(numero, minimo, maximo)

    return numero


def es_numero_entero(numero, minimo, maximo):
    try:
        numero = int(numero)
    except:
        print(numero, 'no es un número valido\n')
        return False

    if numero <= minimo:
        print(numero, f'está por debajo del valor mínimo\n')
        return False
    elif numero > maximo:
        print(numero, f'está por encima del valor máximo {maximo}\n')
        return False

    return True


def convertir_romano(numero):
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


print('Programa para convertir a numeros romanos')

numero = pedir_numero('Insertar número a convertir: ', 0, 3999)
romano = convertir_romano(numero)

print(f'{numero} convertido a números romanos es {romano}')
