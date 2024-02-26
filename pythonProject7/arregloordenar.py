# Matriz bidimensional
matriz = [[9, 1, 6],
          [3, 7, 2],
          [5, 8 ,4]]
print("Matriz desordenada")
print(f"{matriz[0]} \n{matriz[1]} \n{matriz[2]}")
band = False
while band == False:
    band = True
for i in range(len(matriz)-1):
    if matriz[i] > matriz[i+1]:
        aux = matriz[i]
        matriz[i] = matriz[i+1]
        matriz[i + 1] = aux
        band = False

print("Matriz con fila ordenada")
print(print(f"{matriz[0]} \n{matriz[1]} \n{matriz[2]}"))