"""
Ejercicio 1: Filtrar Números Impares
Dada una lista de números, utiliza una comprensión de listas para filtrar solo los números impares

"""
ex = [1,2,3,4,5,6,7,8,9,0]

no_pair = [item for item in range(len(ex)) if item % 2 == 0]


print(no_pair)

"""
Ejercicio 2: Convertir Palabras a Minúsculas
Dada una lista de palabras, utiliza una comprensión de listas para convertir todas las palabras a minúsculas.

"""

words = ['FeLipE','MorEnO','PoRras','luIs','AndreS', 'lindo']


lower_words = [words[i].lower() for i in range(len(words))]

print(lower_words)


"""
Ejercicio 3: Suma Acumulativa
Utiliza una comprensión de listas para generar una lista que contenga la suma acumulativa de los números de otra lista dada.

"""

ac_sum = [sum(ex[:i] + [ex[i]]) for i in range(len(ex))]

print(ac_sum)

"""
Ejercicio 4: Palabras de Longitud Par
Dada una lista de palabras, utiliza una comprensión de listas para obtener solo aquellas palabras que tengan una longitud par.

"""

pair_words = [lower_words[i] for i in range(len(lower_words)) if len(lower_words[i]) % 2 == 0]

print(pair_words)

matriz_3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

arr_0 = []

new_m = [arr_0[matriz_3x3[j][i], len(matriz_3x3[i][j])]  for i in range(len(matriz_3x3)) for j in range(len(matriz_3x3[i]))]




print(new_m)

