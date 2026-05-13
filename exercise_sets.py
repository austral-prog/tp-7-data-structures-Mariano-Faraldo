ALCOHOLS = {
    "whiskey", "whisky", "white rum", "dark rum", "bourbon", "rye", "scotch",
    "vodka", "tequila", "gin", "dry vermouth", "sweet vermouth", "prosecco",
    "aperol", "brandy", "mezcal", "triple sec", "coffee liqueur",
    "almond liqueur", "champagne", "orange curacao", "rum"
}


def clean_ingredients(nombre_plato, ingredientes):
    """
    Elimina ingredientes duplicados.
    """

    ingredientes_limpios = set(ingredientes)

    return (nombre_plato, ingredientes_limpios)


def check_drinks(nombre_bebida, ingredientes):
    """
    Clasifica una bebida como Cocktail o Mocktail.
    """

    for ingrediente in ingredientes:

        if ingrediente in ALCOHOLS:
            return nombre_bebida + " Cocktail"

    return nombre_bebida + " Mocktail"


def unique_chars(texto):
    """
    Retorna un set con los caracteres únicos del string.
    """

    return set(texto)


def sum_set(numeros):
    """
    Suma todos los números de un set.
    """

    total = 0

    for numero in numeros:
        total = total + numero

    return total


def common_elements(set_a, set_b):
    """
    Retorna los elementos presentes en ambos sets.
    """

    comunes = set()

    for elemento in set_a:

        if elemento in set_b:
            comunes.add(elemento)

    return comunes