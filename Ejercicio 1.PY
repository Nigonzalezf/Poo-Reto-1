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

