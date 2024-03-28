# Calcularemos el descuento a un producto en base a un comando y devolveremos el valor con y sin descuento
def calcular_descuento(Total):
    print(f"Tu compra tiene un total de {Total} dolares.")

# Llamada a la función y paso de argumentos
calcular_descuento(17.50)

# Ahora calcularemos el descuento
def descuento_final(Total,tot):
    precio = 17.50
    descuento = precio * 0.15
    tot = precio - descuento
    print(f"El valor a pagar de {Total} es de {tot} con el descuento de {descuento} dolares.")
# Y se llaman los datos de esta otra parte
descuento_final(17.50,"tot" )






