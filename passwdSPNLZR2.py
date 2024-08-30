import random

# Diccionario con las letras originales y las correspondientes letras que se utilizan en un teclado español
cambio_letras = {
    'n': 'ñ',
    'a': 'á',
    'e': 'é',
    'i': 'í',
    'o': 'ó',
    'u': 'ú',
    'A': 'Á',
    'E': 'É',
    'I': 'Í',
    'O': 'Ó',
    'U': 'Ú',
    'N': 'Ñ',
    '!': '¡'
}

def cambiar_contrasena(contrasena, num_cambios=2):
    # Convertir la contraseña en una lista para poder modificarla
    contrasena_lista = list(contrasena)
    
    # Encontrar las posiciones de las letras que pueden ser cambiadas
    posiciones_cambiables = [i for i, letra in enumerate(contrasena_lista) if letra in cambio_letras]
    
    # Si hay menos letras cambiables que el número de cambios solicitado, ajustamos el número de cambios
    if len(posiciones_cambiables) < num_cambios:
        num_cambios = len(posiciones_cambiables)
    
    # Seleccionar aleatoriamente las posiciones a cambiar
    posiciones_a_cambiar = random.sample(posiciones_cambiables, num_cambios)
    
    # Realizar los cambios
    for posicion in posiciones_a_cambiar:
        letra_original = contrasena_lista[posicion]
        contrasena_lista[posicion] = cambio_letras[letra_original]
    
    # Unir la lista en una cadena nuevamente
    nueva_contrasena = ''.join(contrasena_lista)
    return nueva_contrasena

# Pedir al usuario que introduzca una contraseña
contrasena = input("Introduce tu contraseña: ")

# Pedir al usuario cuántas letras quiere cambiar (opcional, por defecto 2)
num_cambios = input("¿Cuántas letras quieres cambiar? (Presiona Enter para cambiar 2): ")
num_cambios = int(num_cambios) if num_cambios.isdigit() else 2

# Cambiar la contraseña
nueva_contrasena = cambiar_contrasena(contrasena, num_cambios)

# Mostrar la nueva contraseña
print(f"Tu nueva contraseña es: {nueva_contrasena}")