
import json




def registrar_habitos():
    habitos = []
    nombre = input("Registre sus hábitos (0 para finalizar): ")

    while True:
        if nombre == "":
            print("No se puede registrar un nombre vacío")

        elif nombre == "0":
            if len(habitos) == 0:
                print("Debe registrar al menos un hábito")
            else:
                break

        else:
            habitos.append(nombre)

        nombre = input("Registre sus hábitos (0 para finalizar): ")

    return habitos

    
def crear_matriz(habitos):
    MP = []
    for i in range(0,30):
        fila = []
        for j in range(len(habitos)):
            fila.append(None)
        MP.append(fila)
    return MP

    


def menu(habitos, MP):
    opcion = input("Seleccione una opción:\n1. Marcar hábitos\n2. Ver progreso\n3. Ver estadísticas\n4. Salir\n")
    while opcion != "4":
        if opcion == "1":
            marcar_habitos(habitos, MP)
        elif opcion == "2":
            progreso_diario(habitos, MP)
        elif opcion == "3":
            estadisticas(habitos, MP)
        else:
            print("Opción inválida")
        opcion = input("Seleccione una opción:\n1. Marcar hábitos\n2. Ver progreso\n3. Ver estadísticas\n4. Salir\n")
    print("Gracias por usar el programa. ¡Hasta luego!")


def marcar_habitos(habitos, MP):
    i = 0
    dia = int(input("Ingrese el día del mes (1-30): "))
    while dia<1 or dia >30:
        print("Día inválido. Por favor, ingrese un día entre 1 y 30.")
        dia = int(input("Ingrese el día del mes (1-30): "))
    while i < len(habitos): 
        respuesta = input(f"¿Ha cumplido con el hábito '{habitos[i]}'? (s/n): ")
        while respuesta.lower() not in ["s", "n"]:
            print("Respuesta inválida. Por favor, ingrese 's' para sí o 'n' para no.")
            respuesta = input(f"¿Ha cumplido con el hábito '{habitos[i]}'? (s/n): ")
        if respuesta.lower() == "s":
            MP[dia-1][i] = True
        else:
            MP[dia-1][i] = False
        i += 1
        guardar_datos(habitos, MP)


def progreso_diario(habitos, MP):
    dia = int(input("Ingrese el día del mes para ver el progreso (1-30): "))
    while dia<1 or dia >30:
        print("Día inválido. Por favor, ingrese un día entre 1 y 30.")
        dia = int(input("Ingrese el día del mes para ver el progreso (1-30): "))
    print(f"Progreso para el día {dia}:")
    for i in range(len(habitos)):
        if MP[dia-1][i] is True:
            print(f"  - {habitos[i]}: Cumplido")
        elif MP[dia-1][i] is False:
            print(f"  - {habitos[i]}: No cumplido")
        else:
            print(f"  - {habitos[i]}: Pendiente")


def estadisticas(habitos, MP):
    contador = 0
    print("Estadísticas de hábitos:")
    for i in range(len(habitos)):
        for j in range(30):
            if MP[j][i] is True:
                contador += 1
            elif MP[j][i] is False:
                continue
        porcentaje = (contador / 30) * 100
        print(f"  - {habitos[i]}: {contador} días cumplidos ({porcentaje:.2f}%)")
        contador = 0        
    return



def guardar_datos(habitos, MP):
    datos = {"habitos": habitos,"matriz": MP}
    with open("datos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)



def cargar_datos():
    try:
        with open("datos.json", "r") as archivo:
            datos = json.load(archivo)
            habitos = datos["habitos"]
            MP = datos["matriz"]
            return habitos, MP
    except FileNotFoundError:
        print("No se encontraron datos guardados. Se creará un nuevo registro.")
        return None
 
    


datos = cargar_datos()
if datos is None:
    habitos = registrar_habitos()
    print(f"{habitos}")
    MP = crear_matriz(habitos)
    menu(habitos, MP)
else:
    habitos, MP = datos
    menu(habitos, MP)


