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
