import functionalities
import sys
import os
from db.models import Caja, Details
import tkinter as tk
from tkinter import ttk
from tree_view import registros, detalles_view, busqueda_view
from functionalities import imprimir_registros_dia


def radio_cambiar():
    """Desactiva un entry u otro segun seleccionemos
    ingreso o egreso en el radiobutton
    """
    if selected_option.get() == 1:
        egresoEntry.config(state="disabled")
        ingresoEntry.config(state="normal")
    else:
        egresoEntry.config(state="normal")
        ingresoEntry.config(state="disabled")


def guardar():
    """Funcion que guarda el nuevo registro dentro de la base de datos
    en la base de datos generada
    """
    # Controlo si el entry trae una cadena vacia le asigno cero
    # ya que de otra forma
    # Al intentar convertirlo a float una cadena vacia me da error
    if ingresoEntry.get() == "":
        ingreso = 0
    else:
        ingreso = float(ingresoEntry.get())

    if egresoEntry.get() == "":
        egreso = 0
    else:
        egreso = float(egresoEntry.get())

    functionalities.save_income(ingreso,
                                egreso,
                                observacionEntry.get("1.0", "end"),
                                detalle_box.get(),
                                selection_mp.get())
    # Borramos los campos
    ingresoEntry.delete("0", "end")
    egresoEntry.delete("0", "end")
    observacionEntry.delete("1.0", "end")


def actualizar():
    """Funcion para actualizar la venta y que se recargue su contenido
    """
    window.destroy()
    main_view()


def main_view():
    """Funcion principal que llama a la vista function la cual se encarga
    de armar la ventana princiapal de nuestro programa
    """
    global window
    window = tk.Tk()
    functions(window)
    window.mainloop()


def functions(window):
    """Funcion que genera la ventana principal de nuestro programa

    Args:
        window (tk.TK()): Objeto de ventana principal
    """
    # Variables globales para utilizarse fuera de esta funcion
    global observacionEntry
    global ingresoEntry
    global egresoEntry
    global detalle_box
    global selection_mp
    global selected_option

    window.title("Caja Principal")
    # Sin estas dimensiones se acomoda al tamaño de los widgets
    window.geometry("400x600+500+20")
    window.resizable(0, 0)
    window.configure(bg="sky blue")

    # Creamos la barra de menús
    menubar = tk.Menu(window)

    # Creamos un menú desplegable "Archivo"
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Ver registros del dia",
                         command=registros)
    filemenu.add_command(label="Ver lista detalles",
                         command=detalles_view)
    filemenu.add_command(label="Actualizar ventana",
                         command=actualizar)
    filemenu.add_command(label="Crear Base de datos",
                         state=["disabled" if os.path.exists("caja.db")
                                else "normal"],
                         command=functionalities.initialize_db)
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=sys.exit)
    menubar.add_cascade(label="Archivo", menu=filemenu)

    # Creamos otro menú desplegable "Edición"
    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Generar reporte del dia",
                         command=imprimir_registros_dia)
    editmenu.add_command(label="Buscar registros por fecha",
                         command=busqueda_view)
    menubar.add_cascade(label="Edición", menu=editmenu)

    # Asignamos la barra de menús a la ventana
    window.config(menu=menubar)

    # Titulo
    titulo = tk.Frame(window)
    titulo_text = tk.Label(titulo,
                           text="CAJA DIARIA",
                           bg="sky blue", fg="black",
                           font=("times new roman", 15, "bold"),
                           relief=tk.GROOVE, bd=2,
                           padx=10, pady=10
                           )
    titulo_text.pack()
    titulo.pack(pady=5, padx=5)

    # Selector de Detalles
    detalles_label = tk.Label(window,
                              text="Detalle ingreso o egreso: ",
                              font=("times new roman", 15, "bold"),
                              bg="sky blue",
                              anchor=tk.W,
                              )
    detalles_label.pack()

    detalle_variable = tk.StringVar()

    detalle_box = ttk.Combobox(window,
                               font=("times new roman", 13, "bold"),
                               width=15,
                               values=functionalities.get_all_detalles(),
                               state="readonly",
                               textvariable=detalle_variable)
    detalle_box.pack()

    # Creamos el marco
    radio_frame = tk.LabelFrame(window,
                                bg="sky blue",
                                text="Tipo de ingreso",
                                font="arial 12 underline"
                                )

    # Crear una variable para el grupo de botones de radio
    selected_option = tk.IntVar()

    # Crear dos botones de radio
    radio_button1 = tk.Radiobutton(radio_frame,
                                   text="Ingreso",
                                   font=("times new roman", 15, "bold"),
                                   bg="sky blue",
                                   anchor=tk.W,
                                   value=1,
                                   width=30,
                                   variable=selected_option,
                                   command=radio_cambiar)
    radio_button1.pack()

    radio_button2 = tk.Radiobutton(radio_frame,
                                   text="Egreso",
                                   font=("times new roman", 15, "bold"),
                                   bg="sky blue",
                                   anchor=tk.W,
                                   value=2,
                                   width=30,
                                   variable=selected_option,
                                   command=radio_cambiar)
    radio_button2.pack()

    # Marcamos por defecto la opcion 1 para los radio buttons
    selected_option.set(1)
    radio_frame.pack(padx=20, pady=10)

    # Creamos los widgets
    entry_ingreso_frame = tk.Frame(window)
    ingreso = tk.Label(entry_ingreso_frame,
                       text="Ingreso: ",
                       font=("times new roman", 15, "bold"),
                       bg="sky blue",
                       anchor=tk.W,
                       width=10)
    ingreso.pack(side="left")
    ingresoEntry = tk.Entry(entry_ingreso_frame,
                            font=("times new roman", 15, "bold"),
                            relief=tk.GROOVE, bd=2,
                            bg="white", fg="black",
                            justify=tk.RIGHT,
                            state="normal",
                            width=20)
    ingresoEntry.pack(side="left")

    entry_ingreso_frame.pack(padx=10, pady=10)

    entry_egreso_frame = tk.Frame(window)
    egreso = tk.Label(entry_egreso_frame,
                      text="Egreso: ",
                      font=("times new roman", 15, "bold"),
                      bg="sky blue",
                      anchor=tk.W,
                      width=10)
    egreso.pack(side="left")

    egresoEntry = tk.Entry(entry_egreso_frame,
                           font=("times new roman", 15, "bold"),
                           relief=tk.GROOVE, bd=2,
                           bg="white", fg="black",
                           justify=tk.RIGHT,
                           state="disabled",
                           width=20)
    egresoEntry.pack(side="left")
    entry_egreso_frame.pack(padx=10, pady=10)

    # Observacion
    observacion_frame = tk.Frame(window, bg="sky blue")
    observacion = tk.Label(observacion_frame,
                           text="Observación: ",
                           font=("times new roman", 15, "bold"),
                           bg="sky blue",
                           anchor=tk.W,
                           width=10)
    observacion.pack(side="left")

    observacionEntry = tk.Text(observacion_frame,
                               font=("times new roman", 13, "bold"),
                               relief=tk.GROOVE, bd=2,
                               bg="white", fg="black",
                               width=22, height=3)
    observacionEntry.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
    observacion_frame.pack(pady=5)

    # Mercado pago
    mp = tk.Frame(window, bg="sky blue")
    selection_mp = tk.BooleanVar()
    mp_checkbox = tk.Checkbutton(
                                 mp,
                                 text="Mercado Pago",
                                 bg="sky blue",
                                 font=("times new roman", 14, "bold"),
                                 anchor=tk.W,
                                 variable=selection_mp
                                 )
    mp_checkbox.pack()
    mp.pack()

    # Botones
    cuadro3 = tk.Frame(window,
                       bg="sky blue")
    boton_convertir = tk.Button(cuadro3,
                                text="Guardar",
                                bg="white",
                                relief=tk.RAISED,
                                bd=3,
                                font=("times new roman", 13, "bold"),
                                width=10,
                                state="normal",
                                command=guardar)
    boton_convertir.pack(side=tk.LEFT, padx=20, pady=20)
    cuadro3.pack(pady=10)


# Llamamos a la vista principal para al ejecutar
# el modulo se ejecute todo el programa
main_view()
