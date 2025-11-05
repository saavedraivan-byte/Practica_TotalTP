def crea_csv(nombre_archivo, columnas):
    file = open(nombre_archivo, "wt")
    csv_line = ",".join(columnas) + "\n"
    file.writelines([csv_line])
    file.close()

def agregar_valores_csv(nombre_archivo):
    file = open(nombre_archivo, "at")
    nombre = input("Ingrese nombre: ")
    while nombre != "":
        apellido = input("Ingrese apellido: ")
        dni = input("Ingrese DNI: ")
        vector = [nombre,apellido,dni]
        fila = ",".join(vector) + "\n"
        file.writelines(fila)
        nombre = input("Ingrese nombre: ")
    file.close()
agregar_valores_csv("dv.csv")





"""
file = open("dv.csv", "wt")
columnas = ["Nombre", "Apellido", "DNI"]
csv_line = ",".join(columnas) + "\n"
file.writelines([csv_line])
nombre = input("Ingrese nombre: ")
while nombre != "":
    apellido = input("Ingrese apellido: ")
    dni = input("Ingrese DNI: ")
    vector = [nombre,apellido,dni]
    fila = ",".join(vector) + "\n"
    file.writelines(fila)
    nombre = input("Ingrese nombre: ")
file.close()
"""


#CLASES
#Transformador de csv a json
#Peluqueria
#Turnos
#Profesionales
#Clientes
#Slot
