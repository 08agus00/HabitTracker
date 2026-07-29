import tkinter as tk
from tkinter import messagebox
import json
#frame menú
def guardar_datos():
    datos = {"habitos": habitos, "matriz": MP}
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
    
    
def crear_matriz(habitos):
    MP = []
    for i in range(0,30):
        global fila
        fila = []
        for j in range(len(habitos)):
            fila.append(None)
        MP.append(fila)
    return MP
    
datos = cargar_datos()
if datos is None:
    habitos = []
    MP = crear_matriz()
else:
    habitos, MP = datos

variables_check = []
ventana_menú = tk.Tk()
ventana_menú.title("Menú Principal")
ventana_menú.geometry("400x300")
frame_menú = tk.Frame(ventana_menú)
frame_menú.pack(pady=10)
label_título = tk.Label(frame_menú, text="Menú Principal", font=("New Roman", 18))
label_título.pack(pady=10)


def volver_menú():
    frame_registro.pack_forget()
    frame_menú.pack(fill="both", expand=True)
    
def volver_menú_dos():
    frame_dia.pack_forget()
    frame_menú.pack(fill="both", expand=True)

def volver_menu_tres():
    frame_marcar.pack_forget()
    frame_dia.pack(fill="both", expand=True)
    
    
def volver_menu_cuatro():
    frame_progreso.pack_forget()
    frame_menú.pack(fill="both", expand=True)
    
def volver_menu_cinco():
    frame_estadisticas.pack_forget()
    frame_menú.pack(fill="both", expand=True)
    
    
    
    
def guardar_habitos():
    nombre = entrada.get()
    if nombre != "":
        if nombre in habitos:
            tk.messagebox.showinfo("Error", "El hábito ya ha sido registrado.")
            entrada.delete(0, tk.END)
        else: 
            habitos.append(nombre)
            for fila in MP:
                fila.append(None)
            lista_habitos.insert("end", nombre)
            entrada.delete(0, tk.END)
            guardar_datos()
    
def registrar_habitos():
    frame_menú.pack_forget()
    global frame_registro
    frame_registro = tk.Frame(ventana_menú)
    frame_registro.pack(fill="both", expand=True)
    ventana_menú.title("Registrar hábito")
    lbl_titulo = tk.Label(frame_registro, text="Registrar hábitos", font=("New Roman", 18))
    lbl_titulo.pack(pady=10)
    global entrada
    entrada = tk.Entry(frame_registro)
    entrada.pack(pady=30)
    btn_agregar = tk.Button(frame_registro, text="Agregar hábito", command=guardar_habitos, bg = "grey")
    btn_agregar.pack(pady=5)
    lbl_habitos = tk.Label(frame_registro, text="Lista de hábitos registrados:")
    lbl_habitos.pack(pady=5)
    global lista_habitos
    lista_habitos = tk.Listbox(frame_registro, width=20, height=10)
    lista_habitos.pack(pady=10) 
    for habito in habitos:
        lista_habitos.insert("end", habito)
    btn_volver = tk.Button(frame_registro, text="Volver al menú", command=volver_menú)
    btn_volver.pack(pady=5)
    


    
    
    
    
def guardar_check():
    global dia
    for i, var in enumerate(variables_check):
        MP[dia - 1][i] = variables_check[i].get()
    print(MP[dia - 1])
        
def guardar_progreso():
    guardar_check()
    guardar_datos()
    tk.messagebox.showinfo("Completado", "Los datos han sido guardados con éxito")
    frame_marcar.pack_forget()
    frame_menú.pack()    
        
    
def check_habitos():
    variables_check.clear()
    global frame_marcar
    frame_marcar = tk.Frame(ventana_menú)
    frame_dia.pack_forget()
    frame_marcar.pack(fill="both", expand=True)
    print(habitos)
    print(type(habitos))
    for habito in habitos:
        var = tk.IntVar()
        check = tk.Checkbutton(frame_marcar, text=f"{habito}", variable=var)
        check.pack(pady=5)
        variables_check.append(var)
    btn_guardar = tk.Button(frame_marcar, text="Guardar", command=guardar_progreso)
    btn_guardar.pack(pady=30)
    btn_volver_tres = tk.Button(frame_marcar, text="Volver", command=volver_menu_tres)
    btn_volver_tres.pack(pady=10)
  
   
    
def boton_dia():
    global dia
    try:
        dia = int(entrada_día.get())
        dia_int = int(dia)
        if dia_int in range(1, 31):
            check_habitos()
        else:
            tk.messagebox.showinfo("Error", "Ingrese un número del 1 al 30")
            entrada_día.delete(0, tk.END)
    except:
        tk.messagebox.showinfo("Error", "Debe ingresar un número")
        entrada_día.delete(0, tk.END)
        return None
            
            
            
            
            
        
        
    
def marcar_habito():
    frame_menú.pack_forget()
    global frame_dia
    frame_dia = tk.Frame(ventana_menú)
    frame_dia.pack(fill="both", expand=True)
    ventana_menú.title("Marcar hábito")
    lbl_titulo = tk.Label(frame_dia, text="Marcar hábitos", font=("New Roman", 18))
    lbl_titulo.pack(pady=10, padx=30)
    lbl_entry = tk.Label(frame_dia, text="Ingrese el día del mes (1-30):")
    lbl_entry.pack(pady=5)
    global entrada_día
    entrada_día = tk.Entry(frame_dia)
    entrada_día.pack(pady=5)
    btn_dia = tk.Button(frame_dia, text="Comprobar", command=boton_dia)
    btn_dia.pack(pady=10)
    btn_volver_dos = tk.Button(frame_dia, text="Volver", command=volver_menú_dos)
    btn_volver_dos.pack(pady=10)
    
    
    
    
def habitos_cumplidos():
    try:
        dia = int(dia_progreso.get())
        lbl_progreso = tk.Label(frame_progreso, text="El día de hoy a cumplido con los siguientes hábitos: ", font=("Montserrat", 14))
        lbl_progreso.pack(pady=5)
        cuadro_progreso = tk.Listbox(frame_progreso, width=15, height=10)
        cuadro_progreso.pack(pady=10)
        if dia in range(1, 31):
            cuadro_progreso.delete(0, "end")
            for i, estado in enumerate(MP[dia - 1]):
                if estado == 1:
                    cuadro_progreso.insert("end", habitos[i])
        else:
            tk.messagebox.showinfo("Error", "Ingrese un número del 1 al 30")
            dia_progreso.delete(0, tk.END)
    except ValueError:
        tk.messagebox.showinfo("Error", "Debe ingresar un número")
        dia_progreso.delete(0, tk.END)
        
    
    
def ver_progreso():
    frame_menú.pack_forget()
    global frame_progreso
    frame_progreso = tk.Frame(ventana_menú)
    frame_progreso.pack(fill="both", expand=True)
    lbl_dia_progreso = tk.Label(frame_progreso, text="Ingrese el día para ver su progreso: ", font=("Arial", 18))
    lbl_dia_progreso.pack(pady=5)
    global dia_progreso
    dia_progreso = tk.Entry(frame_progreso)
    dia_progreso.pack(pady=10)
    btn_progreso = tk.Button(frame_progreso, text="Comprobar", command=habitos_cumplidos)
    btn_progreso.pack(pady=10)
    btn_volver_cuatro = tk.Button(frame_progreso, text="Volver", command = volver_menu_cuatro)
    btn_volver_cuatro.pack(pady=10)
    
    
def estadisticas():
    frame_menú.pack_forget()
    global frame_estadisticas
    frame_estadisticas = tk.Frame(ventana_menú)
    frame_estadisticas.pack(fill="both", expand=True)
    for i, habito in enumerate(habitos):
        cumplidos = 0
        incumplidos = 0
        registrados = 0
        for fila in MP:
            if fila[i] == 1:
                cumplidos += 1
                registrados += 1
            elif fila[i] == 0:
                incumplidos += 1
                registrados +=1
        porcentaje = (cumplidos / registrados) * 100
        lbl_estadisticas_habito = tk.Label(frame_estadisticas, text=f"{habito}:\n {cumplidos}/{registrados} días  ({porcentaje}%) ")
        lbl_estadisticas_habito.pack(pady=10)
    btn_volver_cinco = tk.Button(frame_estadisticas, text="Volver", command=volver_menu_cinco)
    btn_volver_cinco.pack(pady=15)
                
                
                
            
        
+

boton_registrar_habito = tk.Button(frame_menú, text="Registrar hábito", command=registrar_habitos, bg = "grey")
boton_registrar_habito.pack(pady=5)
boton_marcar_habito = tk.Button(frame_menú, text="Marcar hábito", command=marcar_habito, bg = "grey")
boton_marcar_habito.pack(pady=5)
boton_ver_progreso = tk.Button(frame_menú, text="Ver progreso", bg = "grey", command=ver_progreso)
boton_ver_progreso.pack(pady=5)
boton_estadísticas = tk.Button(frame_menú, text="Ver estadísticas", bg = "grey", command=estadisticas)
boton_estadísticas.pack(pady=5)
boton_salir = tk.Button(frame_menú, text="Salir", command=ventana_menú.destroy, bg = "red", font=("New Roman", 12, "bold"))
boton_salir.pack(pady=5)


ventana_menú.mainloop()

