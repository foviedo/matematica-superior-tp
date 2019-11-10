from tkinter import *
#from newton_gregory import *

#Creo el formulario
window = Tk()
#Defino la tupla y la lista de tuplas que voy a ir cargando abajo
#t = tuple[int, int]
#l = list()

#Titulo principal
window.title("FINTER")
#Tamaño del formulario
window.geometry('500x500')

#Creo el label principal
lbl = Label(window, text="Bienvenido a FINTER", font=("Arial", 25), fg="red")
#No se que es, pero si no lo pongo no se muestra el label XD
#lbl.pack()
lbl.grid(column=0, row=0)

txt = Entry(window, width=5)
txt.grid(column=1, row=1)

txt2 = Entry(window, width=5)
txt2.grid(column=2, row=1)

#Defino la función del click. que deberia crear la tupa como (x,y) y guardarla en una lista
# def clicked():
#     t = (txt.get(), txt2.get())
#     l.append(t)

#Creo botón
btn = Button(window, text='Click here') #, command=clicked)
btn.grid(column=3, row=1)

window.mainloop()