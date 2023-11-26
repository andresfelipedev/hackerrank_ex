"""
1. Crear un Diccionario:
Crea un diccionario que represente información sobre un estudiante. Pide al usuario que ingrese el nombre, 
la edad y la nota del estudiante.
"""
first_dic = {
    'name': 'felipe',
    'last_name': 'moreno',
    'grade': 9,
    'age': 14
}
def print_second(ch):
    if ch == 1:
        choosen = 'crear'
    elif ch == 2:
        choosen = 'editar'
    elif ch == 3:
        choosen = 'leer'
    elif ch == 4:
        choosen = 'borrar'

    print(f'\n Que quieres {choosen}?\n')

def getting_keys(ch):
    keys = first_dic.keys()
    contador = 0
    for key in keys:
        contador += 1
        print(f' {contador}) {key}')

def create(arr, key, value):
    arr[key] = value

def edit(arr, key, value):
    arr[key] = value
"""
def read(arr, key, value):
    print(f'{arr[key]}: {arr[value]}')
"""

def delete(arr, key):
    del arr[key]



def choosing_method(array_1, key_1):
    pass
     
    

def actions(add_dic):
    print(' 1) Crear.\n 2) Editar.\n 3) Leer.\n 4) Borrar.')

    person_action = int(input('\nPon la accion que quieres hacer: \n'))

    print_second(person_action)
    getting_keys(add_dic)

    second_per_act = int(input('\nPon la accion que quieres hacer: \n'))

    delete(first_dic, 'age')

    print(first_dic)

    


    

actions(first_dic)


"""
2. Leer (Mostrar) Información:
Imprime la información almacenada en el diccionario creado en el ejercicio anterior.
"""



"""
3. Actualizar Valor:
Permite al usuario actualizar la nota del estudiante en el diccionario creado en el primer ejercicio.

"""


"""
4. Eliminar un Elemento:
Elimina la información de la edad del estudiante del diccionario y muestra el diccionario actualizado.

"""


"""
5. Iterar con Comprensiones:
Crea un diccionario que represente las notas de varios estudiantes. Luego, utiliza comprensiones de
diccionarios para imprimir los nombres de los estudiantes que aprobaron (notas mayores o iguales a 5).

"""
