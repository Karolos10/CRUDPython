from tkinter import *
from tkinter import messagebox
import sqlite3

# Funciones

def conexionBBDD():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')
        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")

def salirAplicacion():
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    if valor == "yes":
        root.destroy()

root = Tk()
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos")
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")
barraMenu.add_cascade(label="CRUD", menu=crudMenu)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# Campos

miFrame = Frame(root)
miFrame.pack()

cuadroID = Entry(miFrame)
cuadroID.grid(row=0, column=1, padx=10, pady=10)
cuadroID.config(fg="red", justify="center")

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)
cuadroApellido.config(fg="red", justify="center")

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)
cuadroDireccion.config(fg="red", justify="center")

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

# Etiquetas

idLabel = Label(miFrame, text="ID:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Contraseña:")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Dirección:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarioLabel = Label(miFrame, text="Comentarios:")
comentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# Botones

miFrame2 = Frame(root)
miFrame2.pack()

botonCrear = Button(miFrame2, text="Crear")
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer = Button(miFrame2, text="Leer")
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar = Button(miFrame2, text="Actualizar")
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar = Button(miFrame2, text="Borrar")
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)







root.mainloop()