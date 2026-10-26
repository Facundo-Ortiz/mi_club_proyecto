import tkinter as tk #traigo la biblioteca de TKINTER

ventana= tk.Tk() #Este es la variable que es en la ventana

ventana.title('INICIO DE SESION') #.title sirve para darle un titulo a la ventana.

ventana.geometry('300x350') #.geometry le pasa el ancho y alto de la ventana.

ventana.resizable(False,False) #.resizable permite modificar el tamaño de la ventana, En caso de False False, este no se puede modificar.

etiqueta= tk.Label(ventana, text='Ingrese su nombre:') #tk.Label sirve para agregar texto dentro de la pagina

etiqueta.pack #.pack guarda dentro de la ventana.

ingrso_nombre= tk.Entry(ventana) #tk.entry sirve para agregar entrada de texto dentro de la

ingrso_nombre.pack


# Crear una pequeña app con etiqueta de texto 
# que sea un saludo integrando el nombre que ingrese el usuario,
#  entrada para que el usuario ingrese nombre y botón que sea que cuando lo 
# presiones obtenga el nombre y devuelva el saludo completo . 

ventana.mainloop()

