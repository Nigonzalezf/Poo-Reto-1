# Poo-Reto-1
Mi nombre es Nicole Gonzalez Fajardo, y en este repositorio se hallaran las soluciones propuestas para los diferentes ejercicios del Reto 1 de POO.

## Ejercicio #1: Operaciones básicas.
Para la solución se emplea una función con tres entradas: a(primer numero), b(segundo numero), y operator(operación). Para la tercera las entradas posibles son +, -, *, /, y dependiendo de esto, se realiza una suma, una resta, una multiplicación o una división, la cual tiene un condicional para evitar que la consola de error, debido a que la división por cero no es posible. El programa cuenta con una entrada para que el usuario sea quien elija los operandos y el operador.

```python
def basic_operations (a,b,operator):
  if operator == '+':
    return a+b
  elif operator == '-':
    return a-b
  elif operator == '*':
    return a*b
  elif operator == '/':
    if b == 0:
      return "No es posible hacer la división entre cero" #Sirve para que no se muestre el error en la consola 
    else:
      return a/b

#Se le pide al usuario que ingrese los numeros y el operador
operation = input("Ingrese la operacion: ")
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

print("El resultado es:",  a, operation, b, "=", basic_operations(a,b,operation))
```

## Ejercicio #2: Verificador de palidromos.
Para realizar el verificador, primero se convierten todas las letras en minúsculas y se le eliminan los espacios en caso de tener, se invierte la palabra y esta se compara con la original, y de esta manera se confirma o niega que la palabra sea un palindromo.

```python
def palindromo(palabra):
# Se convierte a minusculas y se eliminan espacios
  palabra = palabra.lower().replace(" ", "")
# Comparar la palabra con su reverso
  return palabra == palabra[::-1]

# Se solicita al usuario ingresar una palabra
entrada = input("Ingresa una palabra: ")

# Se verifica si es palindromo
if palindromo(entrada):
  print(entrada, "es un palíndromo.")
else:
  print(entrada, "no es un palíndromo.")
```

## Ejercicio #3: Numeros Primos.
En este caso fue propuesto el uso de dos funciones, la primera utilizada para la verificación de que cada numero es o no es primo, y la segunda es utilizada para crear una lista con los numeros que si cumplen con la condición.
```python
def prime_numbers(n):
#Verificion de si el numero es primo o no
  if n < 2:
    return False 
  for i in range(2,n):
    if n % i == 0:
      return False 
      break
  return True
def select_primes(list):
  primes= [n for n in list if prime_numbers(n)]
  return primes

#Le pedimos al usuario los numeros a evaluar
entry = input("Ingresar la lista de numeros separados por espacios: ")

num_list = list(map(int, entry.split()))

# Seleccionar los números primos
primes_list = select_primes(num_list)

# Mostrar los resultados
print("Lista original:", num_list)
print("Números primos:", primes_list)
```
## Ejercicio #4: Mayor suma de dos numeros consecutivos.
En este ejercicio es importante verificar inicialmente, si la lista cuenta con mas de dos elementos para poder efectuar una suma, en ese caso, el programa imprime un mensaje que aclara que no es posible seguir con el proceso. Seguido de esto se realizan diversas sumas de todos los pares consecutivos encontrados en la lista, y se comparan entre si para encontrar el resultado mas grande. 
```python
def higher_consecutive_add(list):
  if len(list) < 2:
    return False  # No hay suficientes elementos para sumar

  higher_add: float = 0

  for i in range(len(list) - 1):
      add = list[i] + list[i + 1]
      if add > higher_add:
          higher_add = add

  return higher_add
# Solicitar al usuario que ingrese una lista de números
entry = input("Ingrese la lista de numeros separados por espacios: ")

num_list = list(map(int, entry.split()))

result = higher_consecutive_add(num_list)

# Mostrar el resultado
if result is not False:
  print("La mayor suma entre dos elementos consecutivos es:", result)
else:
  print("La lista debe tener al menos dos elementos.")
```

## Ejercicio #5: Selector de cadenas con los mismos caracteres.
Cada candena (palabra) es ordenada para asi crear claves y compararlas entre si. Las cadenas que cuenten con la misma clave, son seleccionadas para la creacion de una lista que es mostrada en la salida del programa.
```python
def same_characters(list):
  result = []
  groups = {}

  for word in list:
      # Ordenar los caracteres de la palabra para crear una clave
      key = ''.join(sorted(word))

      # Agrupar palabras que tienen la misma clave
      if key in groups:
          groups[key].append(word)
      else:
          groups[key] = [word]

  # Filtrar solo los grupos que tienen más de un elemento
  for group in groups.values():
      if len(group) > 1:
          result.extend(group)

  return result

# Solicitar al usuario que ingrese una lista de cadenas
entry = input("Ingresa una lista de cadenas separadas por comas: ")

# Convertir la entrada en una lista de strings
chains_list = [chain.strip() for chain in entry.split(",")]

# Obtener los anagramas
result = same_characters(chains_list)

# Mostrar el resultado
print("Los elementos que tienen los mismos caracteres son:", result)

```
