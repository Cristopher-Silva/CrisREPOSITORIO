def temperatura_promedio(ciudades_temperaturas):
    # La funcion principal para poder encontrar lo que buscamos
    temperaturas_promedio = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = promedio
    return temperaturas_promedio

# Usamos los datos de el anterior ejemplo, con sus ciudades y temperaturas respectivas
# Para esto usamos un Diccionario el cual contendra los nombres de las Ciudades y sus temperaturas, "nombre clave = {Datos}
# De antemano se saco un promedio de cada semana, ya que si colocamos cada dia serian datos extensos y el punto es hacerlo lo mas corto posible
ciudades_temperaturas = {
    "Puyo": [28, 29, 25, 21],
    "Quito": [17, 16, 16, 17],
    "Guayaquil": [32, 31, 31, 31]
}

# Y ejecutamos a la funcion que calcula el promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Y se muestran los resultados
print("Las Temperaturas promedio de cada ciudad son:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad} : {promedio:.2f}°C")