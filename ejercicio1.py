def es_palindromo(frase):
    frase = frase.lower()
    frase = frase.replace(' ', '')
    longitud = len(frase)
    if longitud % 2 == 0:
        izquierda = frase[:longitud // 2]
        derecha = frase[longitud // 2:]
    else:
        izquierda = frase[:longitud // 2]
        derecha = frase[longitud // 2 + 1:]
    
    return izquierda == derecha[::-1]