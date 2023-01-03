import db.database as db
import db.models as models
import openpyxl
from tkinter import messagebox
from pathlib import Path
from datetime import date


def initialize_db():
    """Funcion para inicializar la base de datos con las tablas
    creadas a partir de los modelos de la clase de cada entidad
    """
    db.Base.metadata.create_all(db.engine)
    messagebox.showinfo(
        title="Creacion de base de datos",
        message="La base de datos fue creada correctamente"
    )
    db.session.close()


def get_all_detalles():
    """Funcion que trae todos los registros de la tabla detalles

    Returns:
        list: lista de todos los registros de la tabla detalles
    """
    detalle_list = []
    if Path("caja.db").exists():
        registros = db.session.query(models.Details).all()
        for reg in registros:
            detalle_list.append(reg.detalle)
    db.session.close()
    return detalle_list


def save_income(ingreso: float = None,
                egreso: float = None,
                observacion: str = None,
                detalle: str = None,
                mp: bool = None):
    """Funcion que guarda un registro en la base de datos

    Args:
        ingreso (float, optional): valor de ingreso. Defaults to None.
        egreso (float, optional): valor de egreso. Defaults to None.
        observacion (str, optional): observaciones. Defaults to None.
        detalle (str, optional): detalles transaccion. Defaults to None.
        mp (bool, optional): es o no es mercado pago. Defaults to None.
    """

    new_income = models.Caja(date.today(),
                             ingreso,
                             egreso,
                             observacion,
                             detalle,
                             mp)
    try:
        db.session.add(new_income)
        db.session.commit()
        messagebox.showinfo(
            title="Guardado",
            message="Registro Guardado exitosamente"
        )
        db.session.close()
    except Exception as e:
        messagebox.showerror(
            title="DB Error",
            message=f"Error al intentar subir registro a la base de datos {e}"
        )


def obtener_registros():
    """Funcion que trae los registros de la base de datos que coinciden
    con la fecha actual

    Returns:
        list: lista de registros encontrados que coinciden con la fecha
        actual
    """
    return db.session.query(models.Caja).filter(models.Caja.fecha
                                                == date.today()).all()


def eliminar_registro(id: int):
    """Funcion que se encarga de eliminar el registro seleccionado
    de la base de datos

    Args:
        id (int): id del registro que queremos eliminar
    """
    try:
        db.engine.connect().execute(f"DELETE FROM caja WHERE id = {id}")
        messagebox.showinfo(
            title="Eliminación de registro",
            message="Registro eliminado exitosamente"
        )
        db.engine.connect().close()
    except Exception as e:
        messagebox.showerror(
            title="Error de eliminación",
            message=f"Error al intentar eliminar el registro {e}"
        )


def obtener_detalles():
    """Funcion que trae todos los registros de la tabla detalles de la
    base de datos

    Returns:
        list: lista de registros de detalles
    """
    return db.session.query(models.Details).all()


def eliminar_detalle(id: int):
    """Funcion encargada de eliminar el detalle seleccionado mediante
    su id

    Args:
        id (int): id del elemento de la base de datos a eliminar
    """
    try:
        db.engine.connect().execute(f"DELETE FROM detalles WHERE id = {id}")
        messagebox.showinfo(
            title="Eliminación de registro",
            message="Registro eliminado exitosamente"
        )
        db.engine.connect().close()
    except Exception as e:
        messagebox.showerror(
            title="Error de eliminación",
            message=f"Error al intentar eliminar el registro {e}"
        )


def save_detalle(detalle: str):
    """Funcion que guarda en base de datos el nuevo detalle

    Args:
        detalle (str): texto del nuevo detalle a guardar
    """

    new_detalle = models.Details(detalle)

    try:
        db.session.add(new_detalle)
        db.session.commit()
        messagebox.showinfo(
            title="Guardado",
            message="Registro Guardado exitosamente"
        )
        db.session.close()
    except Exception as e:
        messagebox.showerror(
            title="DB Error",
            message=f"Error al intentar subir registro a la base de datos {e}"
        )


def imprimir_registros_dia():
    """Funcion encargada de generar un archivo excel con el informe
    de los registros del dia
    """

    # Creo coloco en variable la hoja del archivo excel
    xls = openpyxl.Workbook()
    hoja = xls.active
    hoja.title = "Registros del dia"

    # Establezco el ancho inicial de las columnas mas largas
    hoja.column_dimensions["A"].width = 30
    hoja.column_dimensions["D"].width = 20
    hoja.column_dimensions["E"].width = 15

    # Obtengo los registros del dia
    regitros_dia = db.session.query(models.Caja).filter(models.Caja.fecha
                                                        == date.today()).all()

    # fecha actual en el archivo
    hoja["A1"] = "FECHA"
    hoja["B1"] = date.today().strftime("%d/%m/%Y")

    # encabezados de las columnas
    hoja["A3"] = "DETALLE"
    hoja["B3"] = "INGRESO"
    hoja["C3"] = "ENGRESO"
    hoja["D3"] = "OBSERVACION"
    hoja["E3"] = "TIPO"

    # Inicializacion de variables
    celda_final = 0
    total_ingreso = 0
    total_egreso = 0
    total_final = 0
    total_ingreso_mecado_pago = 0
    total_egreso_mecado_pago = 0
    total_ingreso_efectivo = 0
    total_egreso_efectivo = 0

    # Se recorren los regostros y se hacen sus repsectivas operaciones
    for index, reg in enumerate(regitros_dia):

        # Se verifica que tipo de ingreso o egreso es y de acuerdo a
        # esto se realiza una operacion u otra
        if reg.mp and reg.ingreso == 0:
            total_egreso_mecado_pago += reg.egreso
        elif reg.mp and reg.egreso == 0:
            total_ingreso_mecado_pago += reg.ingreso
        elif reg.mp is False and reg.egreso == 0:
            total_ingreso_efectivo += reg.ingreso
        else:
            total_egreso_efectivo += reg.egreso

        # Establecemos los valores de acada una de ls columnas
        hoja[f"A{4+index}"] = reg.detalle
        hoja[f"B{4+index}"] = reg.ingreso
        hoja[f"C{4+index}"] = reg.egreso
        hoja[f"D{4+index}"] = reg.observacion

        if reg.mp:
            hoja[f"E{4+index}"] = "Mercado Pago"
        else:
            hoja[f"E{4+index}"] = "Efectivo"

        # Totales
        total_ingreso += reg.ingreso
        total_egreso += reg.egreso

        # Indicador de ultima fila creada para luego comenzar a mostrar
        # los totales al final a pártir de esta
        celda_final = 4+index

    total_final += total_ingreso - total_egreso

    # Colocamos los totales al final del archivo
    hoja[f"A{celda_final+2}"] = "TOTAL GENERAL MERCADO PAGO"
    hoja[f"B{celda_final+2}"] = total_ingreso_mecado_pago - \
        total_egreso_mecado_pago
    hoja[f"A{celda_final+3}"] = "TOTAL GENERAL EFECTIVO"
    hoja[f"B{celda_final+3}"] = total_ingreso_efectivo - \
        total_egreso_efectivo
    hoja[f"A{celda_final+4}"] = "TOTAL INGRESOS"
    hoja[f"B{celda_final+4}"] = total_ingreso
    hoja[f"A{celda_final+5}"] = "TOTAL EGRESOS"
    hoja[f"B{celda_final+5}"] = total_egreso
    hoja[f"A{celda_final+6}"] = "TOTAL GENERAL"
    hoja[f"B{celda_final+6}"] = total_final

    try:
        # Guardamos el archivo
        xls.save("caja_dia.xlsx")

        messagebox.showinfo(
            title="Generacion Excel",
            message="Archivo excel Generado correctamente"
        )
    except Exception as e:
        messagebox.showerror(
            title="Error",
            message=f"Error: {e}"
        )


def registro_por_fecha(fecha: date):
    """Funcion encargada de encontrar los registros que coincidan
    con la fecha seleccionada

    Args:
        fecha (date): fecha seleccionada del widget calendario

    Returns:
        list: lista de registros de la fecha
    """
    return db.session.query(models.Caja).filter(models.Caja.fecha
                                                == fecha).all()


def imprimir_registro_por_fecha(tabla, fecha_seleccion):
    """Funcion encargada de generar reporte en excel con la informacion
    de la tabla con registros de la fecha seleccionada

    Args:
        tabla (tkk.TreeView): tabla con registros de la fecha
        fecha_seleccion (date): fecha seleccionada
    """

    # Creo coloco en variable la hoja del archivo excel
    xls = openpyxl.Workbook()
    hoja = xls.active
    hoja.title = "Registros del dia"

    # Obtenemos filas de la tabla
    items = tabla.get_children()

    # Establezco el ancho inicial de las columnas mas largas
    hoja.column_dimensions["A"].width = 30
    hoja.column_dimensions["D"].width = 20
    hoja.column_dimensions["E"].width = 15

    # fecha actual en el archivo
    hoja["A1"] = "FECHA"
    hoja["B1"] = fecha_seleccion

    # encabezados de las columnas
    hoja["A3"] = "DETALLE"
    hoja["B3"] = "INGRESO"
    hoja["C3"] = "ENGRESO"
    hoja["D3"] = "OBSERVACION"
    hoja["E3"] = "TIPO"

    # Inicializacion de variables
    celda_final = 0
    total_ingreso = 0
    total_egreso = 0
    total_final = 0
    total_ingreso_mecado_pago = 0
    total_egreso_mecado_pago = 0
    total_ingreso_efectivo = 0
    total_egreso_efectivo = 0

    for index, item in enumerate(items):
        valores = tabla.item(item, "values")

        # fecha = valores[0]
        ingreso = float(valores[1])
        egreso = float(valores[2])
        detalle = valores[3]
        mercado_pago = valores[4]
        observacion = valores[5]

        # Se verifica que tipo de ingreso o egreso es y de acuerdo a
        # esto se realiza una operacion u otra
        if mercado_pago and ingreso == 0:
            total_egreso_mecado_pago += egreso
        elif mercado_pago and egreso == 0:
            total_ingreso_mecado_pago += ingreso
        elif mercado_pago is False and egreso == 0:
            total_ingreso_efectivo += ingreso
        else:
            total_egreso_efectivo += egreso

        # Establecemos los valores de acada una de ls columnas
        hoja[f"A{4+index}"] = detalle
        hoja[f"B{4+index}"] = ingreso
        hoja[f"C{4+index}"] = egreso
        hoja[f"D{4+index}"] = observacion

        if mercado_pago:
            hoja[f"E{4+index}"] = "Mercado Pago"
        else:
            hoja[f"E{4+index}"] = "Efectivo"

        # Totales
        total_ingreso += ingreso
        total_egreso += egreso

        # Indicador de ultima fila creada para luego comenzar a mostrar
        # los totales al final a pártir de esta
        celda_final = 4+index

    total_final += total_ingreso - total_egreso

    # Colocamos los totales al final del archivo
    hoja[f"A{celda_final+2}"] = "TOTAL GENERAL MERCADO PAGO"
    hoja[f"B{celda_final+2}"] = total_ingreso_mecado_pago - \
        total_egreso_mecado_pago
    hoja[f"A{celda_final+3}"] = "TOTAL GENERAL EFECTIVO"
    hoja[f"B{celda_final+3}"] = total_ingreso_efectivo - \
        total_egreso_efectivo
    hoja[f"A{celda_final+4}"] = "TOTAL INGRESOS"
    hoja[f"B{celda_final+4}"] = total_ingreso
    hoja[f"A{celda_final+5}"] = "TOTAL EGRESOS"
    hoja[f"B{celda_final+5}"] = total_egreso
    hoja[f"A{celda_final+6}"] = "TOTAL GENERAL"
    hoja[f"B{celda_final+6}"] = total_final

    try:
        # Guardamos el archivo
        xls.save("caja_dia.xlsx")

        messagebox.showinfo(
            title="Generacion Excel",
            message="Archivo excel Generado correctamente"
        )
    except Exception as e:
        messagebox.showerror(
            title="Error",
            message=f"Error: {e}"
        )
