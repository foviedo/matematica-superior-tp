from tkinter import ttk
from tkinter import *


class Menu:
    def __init__(self, window):
        # Initializations
        self.wind = window
        self.wind.title('FINTER')

        # Creating a Frame Container
        frame = LabelFrame(self.wind, text='Ingrese los puntos a interpolar')
        frame.grid(row=0, column=0, columnspan=1, pady=20, padx=20)

        # Creo botones radiales para seleccionar el Metodo
        frame2 = LabelFrame(self.wind, text='Seleccione un método para aproximar')
        frame2.grid(row=0, column=1, columnspan=1, pady=20, padx=20)
        rl = Radiobutton(frame2, text="Lagrange", value='lagrange')
        rl.grid(row=1, column=0, sticky=W)
        rl.select() # Lagrange va a ser el default
        Radiobutton(frame2, text="Newton-Gregory (Progresivo)", value='ng-progresivo').grid(row=2, column=0, sticky=W)
        Radiobutton(frame2, text="Newton-Gregory (Regresivo)", value='ng-regresivo').grid(row=3, column=0, sticky=W)

        # X Input
        Label(frame, text='X: ').grid(row=1, column=0)
        self.px = Entry(frame)
        self.px.focus()
        self.px.grid(row=1, column=1)

        # Y Input
        Label(frame, text='Y: ').grid(row=2, column=0)
        self.py = Entry(frame)
        self.py.grid(row=2, column=1)

        # Button Add Product
        ttk.Button(frame, text='Ingresar punto', command = self.add_punto).grid(row=3, columnspan=2, sticky=W+E)

        # Output Messages
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)

        # Table
        self.tree = ttk.Treeview(height=8, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2, sticky=W+E)
        self.tree.heading('#0', text='X', anchor=CENTER)
        self.tree.heading('#1', text='Y', anchor=CENTER)

        # Buttons
        ttk.Button(text='Borrar', command=self.delete_punto).grid(row=5, column=0, sticky=W + E)
        ttk.Button(text='Iniciar', command=self.pcd_iniciar).grid(row=5, column=1, sticky=W + E)


# User Input Validation
    def validation(self):
        ptoX:str = self.px.get()
        ptoY:str = self.py.get()
        puntos_no_nulos = len(ptoX) != 0 and len(ptoY) != 0
        puntos_son_floats = is_float(ptoX) and is_float(ptoY)
        return puntos_no_nulos and puntos_son_floats

    def add_punto(self):
        if self.validation():
            self.tree.insert('', 0, text=self.px.get(), values=self.py.get())
            self.message['fg'] = 'green'
            self.message['text'] = 'Punto ingresado correctamente'
            self.px.delete(0, END)
            self.py.delete(0, END)
            self.px.focus()
        else:
            self.message['fg'] = 'red'
            self.message['text'] = 'No se pudo ingresar el punto'

    def delete_punto(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['fg'] = 'red'
            self.message['text'] = 'Seleccione una fila primero'
            return
        self.message['text'] = ''
        self.tree.delete(self.tree.selection())
        self.message['fg'] = 'green'
        self.message['text'] = 'El punto fue eliminado correctamente'

    def pcd_iniciar(self):
        #x = list()
        #y = list()
        #puntos = self.tree.get_children()
        #for item in puntos:
        #    x.insert(self.tree.index(item)['text'][0])
        #    y.insert(self.tree.index(item)['value'][0])

        # L = list(zip(x,y))
        print('s')


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    window = Tk()
    application = Menu(window)
    window.mainloop()