import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from functionalities import (obtener_registros,
                             eliminar_registro,
                             obtener_detalles,
                             eliminar_detalle,
                             save_detalle,
                             registro_por_fecha,
                             imprimir_registro_por_fecha)
from datetime import date, datetime


# Para vista de registros
def eliminar():
    """Funcion para eliminar elemento seleccionado de tabla
    """
    # seleccion primer elemento de lista de elementos de la tabla
    item = treeview.selection()[0]
    # Seleccion del item text de la fila, es donde esta el id
    id_selected = int(treeview.item(item, "text"))
    eliminar_registro(id_selected)
    window.destroy()
    # Funcion que arma la ventana de registros nuevamente
    registros()


# Para vista de detalles
def delete_detalle():
    """funcion que alimina el detalle seleccionado de la tabla, su
    funcionamiento es similar al de eliminar registro
    """
    item = detallesview.selection()[0]
    id_selected = int(detallesview.item(item, "text"))
    eliminar_detalle(id_selected)
    detalles.destroy()
    detalles_view()


def guardar_detalle():
    """Funcion encargada de guardar el nuevo detalle y seguidamente
    eliminar la instancia de la ventana para volver a la principal
    """
    save_detalle(detalleEntry.get())
    detalles.destroy()


def registros():
    """Funcion que genera la vista de la ventana registros donde
    se puede eliminar cada uno seleccionando el que se quiera
    """
    registros = obtener_registros()

    # declaracion de variables globales para poder usarlas fuera
    # de esta funcion
    global window
    global treeview
    # Crear la ventana
    window = tk.Toplevel()

    # TITULO APLICACION
    window.title("Datos del dia en caja")
    # Sin estas dimensiones se acomoda al tamaño de los widgets
    window.geometry("700x400+350+80")
    window.resizable(0, 0)
    window.configure(bg="sky blue")

    # TITULO BOX
    titulo = tk.Frame(window)
    titulo_text = tk.Label(titulo,
                           text="DATOS DEL DIA",
                           bg="sky blue", fg="black",
                           font=("times new roman", 15, "bold"),
                           relief=tk.GROOVE, bd=2,
                           padx=10, pady=10
                           )
    titulo_text.pack()
    titulo.pack(pady=5, padx=5)

    # TABLA
    tabla = tk.Frame(window)
    # Crear el widget Treeview
    treeview = ttk.Treeview(tabla)

    # Establecer el modo de selección del widget a "browse"
    treeview.configure(selectmode="browse")

    # Añadir las columnas a la tabla
    treeview["columns"] = ("Fecha",
                           "Ingreso",
                           "Egreso",
                           "Detalle",
                           "Mercado Pago")

    # Ocultamos la columna de índice
    treeview.column("#0", width=100, anchor="center")

    # Establecer el título de las columnas
    treeview.column("Fecha", width=100, anchor="center")
    treeview.column("Ingreso", width=100, anchor="center")
    treeview.column("Egreso", width=100, anchor="center")
    treeview.column("Detalle", width=100, anchor="center")
    treeview.column("Mercado Pago", width=100, anchor="center")
    treeview.heading("#0", text="N°")
    treeview.heading("Fecha", text="Fecha")
    treeview.heading("Ingreso", text="Ingreso")
    treeview.heading("Egreso", text="Egreso")
    treeview.heading("Detalle", text="Detalle")
    treeview.heading("Mercado Pago", text="Mercado Pago")

    # Añadir las filas a la tabla
    for registro in registros:
        treeview.insert("",
                        "end",
                        text=str(registro.id),
                        values=(registro.fecha,
                                registro.ingreso,
                                registro.egreso,
                                registro.detalle,
                                registro.mp))

    # Añadir la tabla a la ventana
    treeview.pack()
    tabla.pack()

    # BOTON
    boton_frame = tk.Frame(window, bg="sky blue")
    btn_eliminar = tk.Button(boton_frame,
                             text="Eliminar",
                             bg="red",
                             fg="white",
                             font=("times new roman", 13, "bold"),
                             width=10,
                             state="normal",
                             command=eliminar)
    btn_eliminar.pack(pady=20)
    boton_frame.pack()

    # # Función que se ejecutará cuando se haga clic en una fila de la tabla
    # def on_row_click(event):
    #     # Obtener el ídentificador de la fila seleccionada
    #     item = treeview.selection()[0]

    #     # Obtener el valor de la fila seleccionada
    #     value1 = treeview.item(item, "Egreso")[0]

    #     # Mostrar los valores de la fila seleccionada
    #     print("Valor de la columna 1:", value1)

    # # Asociar la función a la señal "<<TreeviewSelect>>"
    # treeview.bind("<<TreeviewSelect>>", on_row_click)

    # Mostrar la ventana
    window.mainloop()


def detalles_view():
    """Funcion la cual crea la ventana detalles donde se muestra una
    tabla de detalles, aca vamos a tener una vista donde ver eliminar
    y agregar detalles
    """

    detalles_obtenidos = obtener_detalles()

    # Crear la ventana
    global detalles
    global detallesview
    detalles = tk.Toplevel()

    # TITULO APLICACION
    detalles.title("Datos del dia en caja")
    # Sin estas dimensiones se acomoda al tamaño de los widgets
    detalles.geometry("400x600+500+50")
    detalles.resizable(0, 0)
    detalles.configure(bg="sky blue")

    # TITULO BOX
    titulo = tk.Frame(detalles)
    titulo_text = tk.Label(titulo,
                           text="DETALLES",
                           bg="sky blue", fg="black",
                           font=("times new roman", 15, "bold"),
                           relief=tk.GROOVE, bd=2,
                           padx=10, pady=10
                           )
    titulo_text.pack()
    titulo.pack(pady=5, padx=5)

    # TABLA
    tabla = tk.Frame(detalles)
    # Crear el widget Treeview
    detallesview = ttk.Treeview(tabla)

    # Establecer el modo de selección del widget a "browse"
    detallesview.configure(selectmode="browse")

    # Añadir las columnas a la tabla
    detallesview["columns"] = ("Detalle")

    # Ocultamos la columna de índice
    detallesview.column("#0", width=100, anchor="center")

    # Establecer el título de las columnas
    detallesview.column("Detalle", width=200, anchor="center")

    detallesview.heading("#0", text="Id")
    detallesview.heading("Detalle", text="Detalle")

    # Añadir las filas a la tabla
    for detalle in detalles_obtenidos:
        detallesview.insert("",
                            "end",
                            text=str(detalle.id),
                            values=(detalle.detalle,))

    # Añadir la tabla a la ventana
    detallesview.pack()
    tabla.pack()

    # Creamos los widgets
    nuevo_detalle = tk.Frame(detalles)
    detalle_label = tk.Label(nuevo_detalle,
                             text="Nuevo detalle: ",
                             font=("times new roman", 15, "bold"),
                             bg="sky blue",
                             anchor=tk.W,
                             width=10)
    detalle_label.pack(side="left")

    global detalleEntry

    detalleEntry = tk.Entry(nuevo_detalle,
                            font=("times new roman", 15, "bold"),
                            relief=tk.GROOVE, bd=2,
                            bg="white", fg="black",
                            justify=tk.RIGHT,
                            state="normal",
                            width=20)
    detalleEntry.pack(side="left")
    nuevo_detalle.pack(padx=10, pady=10)

    # BOTONES
    boton_frame = tk.Frame(detalles, bg="sky blue")
    btn_crear = tk.Button(boton_frame,
                          text="Agregar Detalle",
                          bg="green",
                          fg="white",
                          font=("times new roman", 13, "bold"),
                          width=13,
                          state="normal",
                          command=guardar_detalle)
    btn_crear.pack(pady=20)

    btn_borrar = tk.Button(boton_frame,
                           text="Borrar Detalle",
                           bg="red",
                           fg="white",
                           font=("times new roman", 13, "bold"),
                           width=13,
                           state="normal",
                           command=delete_detalle)
    btn_borrar.pack(pady=20)
    boton_frame.pack()

    detalles.mainloop()


def busqueda_view():
    """Funcion para crear venta donde se buscan registros segun la fecha
    en ella se puede buscar asi como tambien generar un reporte del dia
    en excel
    """

    # Crear la ventana
    global ventana_busuqeda
    global tabla_busuqeda
    ventana_busuqeda = tk.Toplevel()

    # TITULO APLICACION
    ventana_busuqeda.title("Datos del dia en caja")
    # Sin estas dimensiones se acomoda al tamaño de los widgets
    ventana_busuqeda.geometry("900x600+250+30")
    ventana_busuqeda.resizable(0, 0)
    ventana_busuqeda.configure(bg="sky blue")

    # TITULO BOX
    titulo = tk.Frame(ventana_busuqeda)
    titulo_text = tk.Label(titulo,
                           text="DATOS",
                           bg="sky blue", fg="black",
                           font=("times new roman", 15, "bold"),
                           relief=tk.GROOVE, bd=2,
                           padx=10, pady=10
                           )
    titulo_text.pack()
    titulo.pack()

    # WIDGET DE CLAENDARIO
    calendario_frame = tk.Frame(ventana_busuqeda)
    ingreso = tk.Label(calendario_frame,
                       text="Seleccione la fecha a buscar: ",
                       font=("times new roman", 15, "bold"),
                       bg="sky blue",
                       anchor=tk.W,
                       width=20)
    ingreso.pack(side="left")
    calendario_frame.pack(pady=5)

    calendar = Calendar(ventana_busuqeda,
                        date_pattern="yyyy-mm-dd",
                        selectmode='day',
                        year=date.today().year,
                        month=date.today().month,
                        day=date.today().day)
    calendar.pack(pady=20)

    def get_date():
        """Funcion que borra los datos viejos de la tabla e
        incerta los datos nuevos
        """
        # Borro todos los elementos que pueda tener la tabla
        tabla_busuqeda.delete(*tabla_busuqeda.get_children())
        # Obtengo la fecha del calendario
        date = calendar.get_date()
        # Convierto la fecha de string a date con formato
        fecha = datetime.strptime(date, "%Y-%m-%d").date()
        # Traigo los registros con la funcion creada
        informacion = registro_por_fecha(fecha)
        # Añadir las filas a la tabla
        for info in informacion:
            # incerto los nuevos registros en la tabla
            tabla_busuqeda.insert("",
                                  "end",
                                  text=str(info.id),
                                  values=(info.fecha,
                                          info.ingreso,
                                          info.egreso,
                                          info.detalle,
                                          info.mp,
                                          info.observacion))

    def imprimir_registros_buscados():
        """Funcion para generar reporte en excel de los registros buscados
        """
        fecha_calendar = calendar.get_date()
        fecha_calendar = datetime.strptime(fecha_calendar,
                                           "%Y-%m-%d").date()
        fecha_calendar = fecha_calendar.strftime("%d/%m/%Y")
        imprimir_registro_por_fecha(tabla_busuqeda, fecha_calendar)

    # TABLA
    tabla = tk.Frame(ventana_busuqeda)
    # Crear el widget Treeview
    tabla_busuqeda = ttk.Treeview(tabla)

    # Establecer el modo de selección del widget a "browse"
    tabla_busuqeda.configure(selectmode="browse")

    # Añadir las columnas a la tabla
    tabla_busuqeda["columns"] = ("Fecha",
                                 "Ingreso",
                                 "Egreso",
                                 "Detalle",
                                 "Mercado Pago",
                                 "Observacion")

    # Ocultamos la columna de índice
    tabla_busuqeda.column("#0", width=100, anchor="center")

    # Establecer el título de las columnas
    tabla_busuqeda.column("Fecha", width=100, anchor="center")
    tabla_busuqeda.column("Ingreso", width=100, anchor="center")
    tabla_busuqeda.column("Egreso", width=100, anchor="center")
    tabla_busuqeda.column("Detalle", width=100, anchor="center")
    tabla_busuqeda.column("Mercado Pago", width=100, anchor="center")
    tabla_busuqeda.column("Observacion", width=250, anchor="center")
    tabla_busuqeda.heading("#0", text="N°")
    tabla_busuqeda.heading("Fecha", text="Fecha")
    tabla_busuqeda.heading("Ingreso", text="Ingreso")
    tabla_busuqeda.heading("Egreso", text="Egreso")
    tabla_busuqeda.heading("Detalle", text="Detalle")
    tabla_busuqeda.heading("Mercado Pago", text="Mercado Pago")
    tabla_busuqeda.heading("Observacion", text="Observacion")

    # Añadir la tabla a la ventana
    tabla_busuqeda.pack()
    tabla.pack()

    # BOTON
    boton_frame = tk.Frame(ventana_busuqeda, bg="sky blue")
    btn_eliminar = tk.Button(boton_frame,
                             text="Generar Reporte",
                             bg="blue",
                             fg="white",
                             font=("times new roman", 13, "bold"),
                             width=15,
                             state="normal",
                             command=imprimir_registros_buscados)
    btn_eliminar.grid(column=1, row=1, pady=10, padx=10)

    btn_buscar = tk.Button(boton_frame,
                           text="Buscar",
                           bg="orange",
                           font=("times new roman", 13, "bold"),
                           width=10,
                           state="normal",
                           command=get_date)
    btn_buscar.grid(column=2, row=1, pady=10, padx=10)
    boton_frame.pack()

    # Mostrar la ventana
    ventana_busuqeda.mainloop()
