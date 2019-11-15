from tkinter import ttk
from tkinter import *
from newton_gregory import newton_gregory, newton_gregory_regresivo
from lagrange import lagrange


class Menu:
    def __init__(self, window):
        # Initializations
        self.wind = window
        self.wind.title('FINTER')

        # Creating a Frame Container
        frame = LabelFrame(self.wind, text='Ingrese los puntos a interpolar')
        frame.grid(row=0, column=0, columnspan=1, pady=20, padx=20)

        # Creo botones radiales para seleccionar el Metodo
        self.metodoVar = StringVar()
        frame2 = LabelFrame(self.wind, text='Seleccione un método para aproximar')
        frame2.grid(row=0, column=1, columnspan=1, pady=20, padx=20)
        rl = Radiobutton(frame2, text="Lagrange", value='Lagrange', variable=self.metodoVar)
        rl.grid(row=1, column=0, sticky=W)
        rl.select() # Lagrange va a ser el default
        Radiobutton(frame2, text="Newton-Gregory (Progresivo)",
                    value='Newton-Gregory (Progresivo)',
                    variable=self.metodoVar).grid(row=2, column=0, sticky=W)

        Radiobutton(frame2, text="Newton-Gregory (Regresivo)",
                    value='Newton-Gregory (Regresivo)',
                    variable=self.metodoVar).grid(row=3, column=0, sticky=W)

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
        self.message = Label(text='Utilice el punto como signo para separar decimales. ej: 3.141592', fg='grey')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)

        # Table
        self.tree = ttk.Treeview(height=8, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2, sticky=W+E)
        self.tree.heading('#0', text='X', anchor=CENTER)
        self.tree.heading('#1', text='Y', anchor=CENTER)

        # Buttons
        ttk.Button(text='Borrar', command=self.delete_punto).grid(row=5, column=0, sticky=W + E)
        ttk.Button(text='Iniciar', command=self.pcd_iniciar).grid(row=5, column=1, sticky=W + E)


        # Borrar estas lineas luego:
        borrar = [(0, 0), (1, 1), (2, 2), (3, 3)]
        for element in borrar:
            self.tree.insert('', 0, text=element[0], values=element[1])


# User Input Validation
    def validation(self):
        ptoX:str = self.px.get()
        ptoY:str = self.py.get()
        puntos_no_nulos = len(ptoX) != 0 and len(ptoY) != 0
        puntos_son_floats = is_float(ptoX) and is_float(ptoY)
        unicidad = self.verificar_unicidad(ptoX)
        return puntos_no_nulos and puntos_son_floats and unicidad

    def verificar_unicidad(self, ptoX):
        if is_float(ptoX):
            ptoX = float(ptoX)
        else:
            return False

        equis = []
        for item in self.tree.get_children():
            elemento = self.tree.item(item)
            x = float(elemento["text"])
            equis.append(x)

        return ptoX not in equis


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
        self.puntos = []
        for item in self.tree.get_children():
            elemento = self.tree.item(item)
            x = float(elemento["text"])
            y = float(elemento["values"][0])
            self.puntos.append((x, y))

        if len(self.puntos) == 0:
            self.message['fg'] = 'red'
            self.message['text'] = 'Debe ingresar al menos un punto'
            return

        self.puntos.sort(key=lambda tup: tup[0])
        self.metodo = self.metodoVar.get()
        print(self.metodo)
        print(self.puntos)
        # self.wind.withdraw()

        self.finter()


    def finter(self):
        ventana = Toplevel(self.wind)

        frame = ttk.LabelFrame(ventana, text="Resolviendo por el método de {}:".format(self.metodo))
        frame.grid(row=1, column=0, columnspan=1)
        if(self.metodo == "Lagrange"):
            resultado, pasos = lagrange(*self.puntos)
        elif(self.metodo == "Newton-Gregory (Progresivo)"):
            resultado, pasos = newton_gregory(*self.puntos)
        elif(self.metodo == "Newton-Gregory (Regresivo)"):
            resultado, pasos = newton_gregory_regresivo(*self.puntos)

        Label(frame, text=pasos, anchor="e").grid(row=0, column=0)
        # mytext = StringVar(value=pasos)
        # myentry = ttk.Entry(frame, textvariable=mytext, state='readonly')
        # myentry.pack
        # myscroll = ttk.Scrollbar(frame, orient='vertical', command=myentry.xview)
        # myentry.config(xscrollcommand=myscroll.set)
        # myentry.grid(row=1, sticky='ew')
        # myscroll.grid(row=2, sticky='ew')

        frameFinal = ttk.LabelFrame(ventana, text="Resultado Final")
        frameFinal.grid(row=0, column=0, columnspan=2, sticky="ew")
        ttk.Label(frameFinal, text=resultado).grid(row=0, column=0, sticky="ew")

        ttk.Button(frameFinal, text='Mostrar', command= lambda : frame.grid()).grid(row=0, column=2, columnspan=3)
        ttk.Button(frameFinal, text='Ocultar', command = lambda: frame.grid_forget()).grid(row=0, column=5, columnspan=3)
        frame.grid_forget()

        entryP = Entry(frameFinal)
        entryP.grid(row=0, column=8)
        ttk.Button(frameFinal, text='Calcular').grid(row=0, column=9)



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
