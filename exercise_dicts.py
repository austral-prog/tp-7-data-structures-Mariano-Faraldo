def create_inventory(items):
    """
    Crea un inventario contando cuántas veces aparece cada item.
    """

    inventario = {}

    for item in items:

        if item not in inventario:
            inventario[item] = 1

        else:
            inventario[item] = inventario[item] + 1

    return inventario


def add_items(inventario, items):
    """
    Agrega items al inventario.
    """

    for item in items:

        if item in inventario:
            inventario[item] = inventario[item] + 1

        else:
            inventario[item] = 1

    return inventario


def decrement_items(inventario, items):
    """
    Resta items del inventario sin permitir negativos.
    """

    for item in items:

        # verificar que exista
        if item in inventario:

            # verificar stock
            if inventario[item] > 0:

                inventario[item] = inventario[item] - 1

    return inventario





def remove_item(inventario, item):
    """
    Elimina un item del inventario.
    """

    if item in inventario:

        del inventario[item]

    return inventario


def find_max_value(diccionario):
    """
    Retorna la clave con el valor más alto.
    """

    # caso vacío
    if diccionario == {}:
        return ""

    primer = True

    for nombre in diccionario:

        # primera vuelta
        if primer == True:

            mejor_nombre = nombre
            mejor_puntaje = diccionario[nombre]

            primer = False

        # comparar
        elif diccionario[nombre] > mejor_puntaje:

            mejor_puntaje = diccionario[nombre]
            mejor_nombre = nombre

    return mejor_nombre


def reverse_dict(diccionario):
    """
    Invierte claves y valores.
    """

    invertido = {}

    for clave in diccionario:

        valor = diccionario[clave]

        # si todavía no existe
        if valor not in invertido:

            invertido[valor] = clave

        # si ya existe
        else:

            invertido[valor] = invertido[valor] + clave

    return invertido


def word_frequency(palabras):
    """
    Cuenta cuántas veces aparece cada palabra.
    """

    frecuencia = {}

    for palabra in palabras:

        if palabra not in frecuencia:

            frecuencia[palabra] = 1

        else:

            frecuencia[palabra] = frecuencia[palabra] + 1

    return frecuencia


def find_biggest_expense(gastos):
    """
    Retorna la categoría con mayor promedio.
    """

    # caso vacío
    if gastos == {}:
        return ""

    primer = True

    # recorrer categorías
    for categoria in gastos:

        lista = gastos[categoria]

        # sumar gastos
        total = 0

        for gasto in lista:
            total = total + gasto

        # calcular promedio
        promedio = total / len(lista)

        # primera vuelta
        if primer == True:

            mejor_categoria = categoria
            mejor_promedio = promedio

            primer = False

        # comparar
        elif promedio > mejor_promedio:

            mejor_categoria = categoria
            mejor_promedio = promedio

    return mejor_categoria


def sum_expenses(gastos):
    """
    Retorna la suma total de gastos por categoría.
    """

    resultado = {}

    # recorrer categorías
    for categoria in gastos:

        lista = gastos[categoria]

        total = 0

        # sumar gastos
        for gasto in lista:

            total = total + gasto

        # guardar resultado
        resultado[categoria] = total

    return resultado


def sum_expenses_by_type(gastos):
    """
    Suma montos agrupados por tipo.
    """

    resultado = {}

    # recorrer categorias
    for categoria in gastos:

        lista = gastos[categoria]

        # recorrer tuplas
        for tupla in lista:

            tipo = tupla[0]
            monto = tupla[1]

            # si no existe
            if tipo not in resultado:

                resultado[tipo] = monto

            # si ya existe
            else:

                resultado[tipo] = resultado[tipo] + monto

    return resultado
def list_inventory(inventario):
    return [
        (item, cantidad)
        for item, cantidad in inventario.items()
        if cantidad > 0
    ]