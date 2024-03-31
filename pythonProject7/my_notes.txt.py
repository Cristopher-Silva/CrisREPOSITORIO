# Creamos nuestro archivo de my_notes.txt y colocamos 3 lineas de notas personales
# Comenzamos abriendo nustras notas con el siguiente comando
my_notes = open('my_notes.txt', 'w')

# Utilizaremos 2 metodos para escribir las notas, primero el write ()
my_notes.write("Nota 1: Nuestro primer semestre en la Universidad esta por acabar y espero que todo salga bien.\n")
my_notes.write("Nota 2: Usar Python es mas facil que otros tipos de idiomas de programacion.\n")
my_notes.write("Nota 3: Las clases impartidas durante este semestre sirven como experiencia a futuro. \n")

# El segundo método es writelines()
lineas = [" Final de las notas personales. \n"]
my_notes.writelines(lineas)
# Y cerramos nuestras notas
my_notes.close()

# Volvemos a abrir el archivo my_notes.txt.
my_notes = open('my_notes.txt', 'r')

# Y leemos el archivo linea por linea con cada metodo.

# Método 1. read()
print('Método 1: read()')
print('--------------------')
print(my_notes.read())
my_notes.close()

# Y el método 2. readlines()
my_notes = open('my_notes.txt', 'r')
print('Método 2: readlines()')
print('--------------------')
for linea in my_notes.readlines():
    print(linea.rstrip('\n'))
my_notes.close()