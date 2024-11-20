def same_characters(list):
  result = []
  groups = {}

  for word in list:
  # Ordenar los caracteres de la palabra para crear una "clave"
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

# Solicitar al usuario que ingrese una lista de palabras
entry = input("Ingresa una lista de palabras separadas por comas: ")

chains_list = [chain.strip() for chain in entry.split(",")]

result = same_characters(chains_list)

# Mostrar el resultado
print("Los elementos que tienen los mismos caracteres son:", result)
