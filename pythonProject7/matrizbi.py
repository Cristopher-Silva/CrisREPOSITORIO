# Matriz bidimensional
matriz = [[5, 4, 7],
          [8, 2, 9],
          [1, 3, 6]]
# Seleccionar un valor que se busque
print(f"{matriz[0]} \n{matriz[1]} \n{matriz[2]}")
print ("Valor a buscar: 3")
valor_buscado = 3
posicion = (matriz[1][1], matriz[2][0])
if posicion:
    print(f"El valor {valor_buscado} se encuentra en la posicion {posicion} ")
else:
    print( "El valor colocado no se encuentra en la matriz")