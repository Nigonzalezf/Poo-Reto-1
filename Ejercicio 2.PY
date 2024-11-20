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
