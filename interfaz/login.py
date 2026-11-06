import tkinter as tk

ventana= tk.Tk()

ventana.title('Inicio de Sesion')

ventana.geometry('300x350')

ventana.resizable(False,False)

user= tk.Label(ventana, text='usuario')

user.pack()

ent_user= tk.Entry(ventana)

ent_user.pack()

contra= tk.Label(ventana, text='Contraseña')

contra.pack()

ent_contra= tk.Entry(ventana)

ent_contra.pack()

usuario= "admin"
contrasena= "python123"

def inicio():
 
    if ent_user==usuario and ent_contra==contrasena:
        correcto= tk.Label(ventana,text="Iniciaste tu sesion. Bienvenido de vuelta")
        correcto.pack

        return correcto
    else:
        incorrecto= tk.Label(ventana, text="Incorrrecto. Intentalo de nuevo")
        incorrecto.pack

        return incorrecto
        
    
boton= tk.Button(ventana, text="Verificar", command= inicio)
boton.pack()

ventana.mainloop()