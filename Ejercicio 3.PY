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
      
