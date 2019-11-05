import decimal
# testing something
class BilleteraElectronica(object):
   
    def __init__(self, id, persona, pin, saldo_inicial):
        
        if type(pin) != int:

            raise TypeError("El PIN debe ser de tipo 'int'")

        self.id = id

        self.persona = persona
        
        self.pin = pin

        self.creditos = []

        self.debitos = []
        
        self.deuda_actual = decimal.Decimal(0)

        self.saldo_actual = decimal.Decimal(saldo_inicial)

    

    def saldo(self):

        return self.saldo_actual

    

    def recargar(self, recarga):

        if (recarga.monto <= 0):

            print("El saldo a recargar debe ser un numero natural.")

            return -1

        

        self.creditos.append(recarga)

        self.deuda_actual += recarga.monto

        

    def consumir(self, debito):

        if (self.pin != debito.pin_debito):

            print("El PIN ingresado no coincide con el del usuario.")

            return -1


        if (debito.monto > self.saldo_actual):

            print("El consumo es mayor al saldo disponible.")
            
            return -1
            
        self.saldo_actual -= debito.monto
