from db.database import Base
# Importamos los tipode  datos a usar en sqlalchemy
from sqlalchemy import (Column,
                        Integer,
                        String,
                        Boolean,
                        Date,
                        Float)


class Caja(Base):
    """Clase modelo para la entidad de la base de datos Caja

    Args:
        Base (Base): Instancia de herencia de el objeto base

    Returns:
        str: descripcion del objeto
    """
    __tablename__ = "caja"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date)
    ingreso = Column(Float)
    egreso = Column(Float)
    observacion = Column(String)
    detalle = Column(String)
    mp = Column(Boolean)

    def __init__(self,
                 fecha: Date,
                 ingreso: Float,
                 egreso: Float,
                 observacion: String,
                 detalle: String,
                 mp: Boolean):
        self.fecha = fecha
        self.ingreso = ingreso
        self.egreso = egreso
        self.observacion = observacion
        self.detalle = detalle
        self.mp = mp

    def __str__(self) -> str:
        return f"""Id: {self.id} \n
                 Fecha: {self.fecha} \n
                 Ingreso: {self.ingreso} \n
                 Egreso: {self.egreso} \n
                 Observacion: {self.observacion} \n
                 Detalle: {self.detalle} \n
                 Mercado Pago: {self.mp}"""


class Details(Base):
    """Clase que representa el modelo para la entidad de la bse de datos
    Details

    Args:
        Base (Base): Instancia de herencia de el objeto base
    """
    __tablename__ = "detalles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    detalle = Column(String)

    def __init__(self, detalle: String):
        self.detalle = detalle
