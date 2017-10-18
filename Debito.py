import decimal
import datetime

class Debito(object):    

    def __init__(self, monto, id_consumo, pin_debito):

        try:

            assert(type(monto) is int or type(monto) is float)

            self.monto = decimal.Decimal(monto)

            self.fecha_consumo = datetime.datetime.now()

            self.id_consumo = id_consumo
            
            self.pin_debito = pin_debito

        except:

            print("Error en el consumo")

            self.fecha = None

            self.id_consumo = None

            self.monto = None
