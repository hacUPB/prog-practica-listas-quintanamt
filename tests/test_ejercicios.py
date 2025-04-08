# test_ejercicios.py

from src.ejercicios import suma_matriz, maximo_matriz, es_primo, transponer_matriz, filtrar_pares
from src.ejercicios import contar_palabras, tabla_multiplicar, contar_negativos, lista_ordenada, cifrado_cesar

def test_suma_matriz():
    assert suma_matriz([[1, 2], [3, 4]]) == 10
    assert suma_matriz([[0, 0], [0, 0]]) == 0
    assert suma_matriz([[-1, -2], [-3, -4]]) == -10

def test_maximo_matriz():
    assert maximo_matriz([[1, 2], [3, 4]]) == 4
    assert maximo_matriz([[5, 2], [1, 0]]) == 5
    assert maximo_matriz([[-1, -2], [-3, -4]]) == -1

def test_es_primo():
    assert es_primo(7) == True
    assert es_primo(4) == False
    assert es_primo(1) == False
    assert es_primo(13) == True

def test_transponer_matriz():
    assert transponer_matriz([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert transponer_matriz([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

def test_filtrar_pares():
    assert filtrar_pares([1, 2, 3, 4]) == [2, 4]
    assert filtrar_pares([1, 3, 5]) == []
    assert filtrar_pares([2, 4, 6]) == [2, 4, 6]

def test_contar_palabras():
    assert contar_palabras("Hola Mundo") == 2
    assert contar_palabras("Python es genial") == 3
    assert contar_palabras("") == 0

def test_tabla_multiplicar():
    assert tabla_multiplicar(2) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    assert tabla_multiplicar(5) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

def test_contar_negativos():
    assert contar_negativos([-1, 0, 1, 2, -3]) == 2
    assert contar_negativos([0, 1, 2, 3]) == 0
    assert contar_negativos([-1, -2, -3]) == 3

def test_lista_ordenada():
    assert lista_ordenada([1, 2, 3, 4]) == True
    assert lista_ordenada([1, 3, 2, 4]) == False
    assert lista_ordenada([4, 3, 2, 1]) == False

def test_cifrado_cesar():
    assert cifrado_cesar("abc", 1) == "bcd"
    assert cifrado_cesar("xyz", 3) == "abc"
    assert cifrado_cesar("hello", 5) == "mjqqt"
