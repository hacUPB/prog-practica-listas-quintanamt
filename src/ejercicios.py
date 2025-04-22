# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
    fil = len(matriz)
    col = len (matriz [0])
    acumulador = 0 
    for i in range (fil): #los indices de las filas
        for j in range(col): #los indices de las columnas
            acumulador += matriz [i][j]
    return acumulador 

    """
    Recibe una lista de listas y devuelve la suma de todos sus elementos.
    Incluir el código aquí para sumar los elementos de la matriz.
    """
    pass

# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):

    fil = len(matriz)          # Número de filas
    col = len(matriz[0])       # Número de columnas (asumiendo matriz no vacía)
    maximo = matriz[0][0]      # Inicializamos con el primer elemento de la matriz
    
    for i in range(fil):       # Recorrer filas (índice i)
        for j in range(col):   # Recorrer columnas (índice j)
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]  # Actualizamos el máximo si encontramos un valor mayor
    return maximo

    """
    Recibe una lista de listas y devuelve el valor máximo.
    Incluir el código aquí para encontrar el valor máximo en la matriz.
    """
    pass

# Ejercicio 3: Verificar si un número es primo
def es_primo(n):
    """
    Recibe un número y devuelve True si es primo, False en caso contrario.
    """
    if n <= 1:
        return False

    i = 2
    while i < n:
        if n % i == 0: # n % i == 0 verifica si n es divisible entre i (si el residuo es 0, entonces i es un divisor de n → n no es primo).

            return False
        i += 1

    return True

    """
    Recibe un número y devuelve True si es primo, False en caso contrario.
    Incluir el código aquí para determinar si un número es primo.
    """
    pass

# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):

    """
    Recibe una lista de listas y devuelve la matriz transpuesta.
    """
    filas = len(matriz)
    columnas = len(matriz[0])

    # Crear matriz vacía con dimensiones invertidas
    transpuesta = []
    #Lista vacía donde se va ir guardando las filas de la matriz traspuesta
    for j in range(columnas):
        #Se recorre cada columna de la matriz original (append agrega un elemento a la lista)
        nueva_fila = []
        for i in range(filas):
            nueva_fila.append(matriz[i][j])
        transpuesta.append(nueva_fila)
    
    return transpuesta

   
    """
    Recibe una lista de listas y devuelve la matriz transpuesta.
    Incluir el código aquí para transponer la matriz.
    """
    pass

# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
    """
    Recibe una lista de números y devuelve una nueva lista con solo los números pares.
    """
    pares = []  # Creamos una lista vacía para guardar los números pares

    for numero in lista:  # Recorremos cada número de la lista original
        if numero % 2 == 0:  # Si el número es divisible entre 2, es par
            pares.append(numero)  # Lo agregamos a la lista de pares

    return pares  # Devolvemos la lista de pares


# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
    contador = 0
    en_palabra = False  # Variable para saber si estamos dentro de una palabra

    for caracter in frase:
        if caracter != ' ' and not en_palabra:
            # Hemos encontrado el inicio de una palabra
            contador += 1
            en_palabra = True
        elif caracter == ' ':
            # Cuando encontramos un espacio, salimos de la palabra
            en_palabra = False

    return contador




# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):

    #Recibe un número y devuelve una lista con su tabla de multiplicar del 1 al 10.

    tabla = []  # Lista vacía donde guardaremos los resultados

    for i in range(1, 11):  # Del 1 al 10 (incluidos)
        resultado = n * i  # Calculamos el producto
        tabla.append(resultado)  # Lo agregamos a la lista

    return tabla  # Devolvemos la lista con los resultados
    pass

# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):

    #Recibe una lista de números y devuelve la cantidad de números negativos.

    contador = 0  # Inicializamos el contador en 0
    
    for numero in lista:  # Recorremos cada número en la lista
        if numero < 0:    # Si el número es negativo
            contador += 1  # Incrementamos el contador
            
    return contador  # Retornamos el total de negativos
    pass

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    """
    Recibe una lista de números y devuelve True si está ordenada de menor a mayor.
    """
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False  # Si un número es mayor que el siguiente, no está ordenada
    return True  # Si no se encontró ningún error en el orden, está ordenada


    """
    Recibe una lista de números y devuelve True si está ordenada de menor a mayor.
    Incluir el código aquí para verificar si la lista está ordenada.
    """
    pass

# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    """
    Recibe un texto y un desplazamiento, y devuelve el texto cifrado usando el cifrado César.
    El cifrado César desplaza cada letra por el número dado en el alfabeto.
    """
    texto_cifrado = ""

    for letra in texto:
        codigo = ord(letra) + 1
        tc = chr(codigo)
        texto_cifrado += tc

    return texto_cifrado


    """
    Recibe un texto y un desplazamiento, y devuelve el texto cifrado usando el cifrado César.
    Incluir el código aquí para cifrar el texto con el cifrado César.
    """
    pass


#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
  #ejercicio1
  lista = [[4,5,6],[7,8,9]]
  resultado = suma_matriz(lista)
  print(f"La suma de todos los elementos es: {resultado}")
  #ejercicio2
  lista = [[4, 5, 6], [7, 8, 9]]
  resultado = maximo_matriz(lista)
  print(f"El valor máximo en la matriz es: {resultado}")
  #ejercicio3

# Definimos algunos números para probar
numeros = [2, 3, 4, 5, 10, 11, 15, 17]

for numero in numeros:
    if es_primo(numero):
            print("El número", numero, "es primo.")
    else:
        print("El número", numero, "no es primo.")


  #ejercicio 4 
matriz = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
print("Matriz original:")
for fila in matriz:
        print(fila)
    
transpuesta = transponer_matriz(matriz)

print("\nMatriz transpuesta:")
for fila in transpuesta:
    print(fila)

#ejercicio 5

    numero = [1, 2, 3, 4, 5, 6, 7, 8]
    solo_pares = filtrar_pares(numero)

    print("Lista original:", numero)
    print("Números pares:", solo_pares)

#ejercicio 6
    frase = "hola mundo"
    cantidad = contar_palabras(frase)
    print("Número de palabras:", cantidad)

#ejercicio 7 

    numero = 2
    resultados = tabla_multiplicar(numero)
    print("Tabla de multiplicar del", numero)
    for valor in resultados:
        print(valor)

#ejercicio 8 
# Programa principal (para probar la función)
    lista_numeros = [4, -2, 0, -7, 1, -3, 5]  # Lista de prueba
    resultado = contar_negativos(lista_numeros)
    
    print(f"Lista original: {lista_numeros}")
    print(f"Cantidad de números negativos: {resultado}")

#ejercicio 9 
    lista = [1, 2, 3, 4]
    resultado = lista_ordenada(lista)
    print("¿La lista está ordenada?:", resultado)

#ejercicio10
    
def main():
    texto = "hola mundo 2025"
    resultado = cifrado(texto)
    print("Texto original:", texto)
    print("Texto cifrado:", resultado)



if __name__ == "__main__":
    main()