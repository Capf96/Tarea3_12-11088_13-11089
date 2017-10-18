import decimal
import datetime

class Credito(object):

    
    def __init__(self, monto, id_recarga):

        try:

            if type(id_recarga) != str:

                raise TypeError("El id de la recarga debe ser de tipo string")

            

            assert(type(monto) is int or type(monto) is float)

            self.monto = decimal.Decimal(monto)

            self.fecha_recarga = datetime.datetime.now()

            self.id_recarga = id_recarga

        except:

            print("Error en la recarga.")

            self.fecha = None

            self.id_recarga = None

            self.monto = None