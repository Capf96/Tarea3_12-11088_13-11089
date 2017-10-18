import unittest

from BilleteraElectronica import BilleteraElectronica
from Persona import Persona
from Credito import Credito
from Debito import Debito

'''
La clase ServiciosTest es utilizada para los casos de prueba unitarios, usando
el pluging PyUnit.
'''
class ServiciosTest(unittest.TestCase):

    def setUp(self):
        carlos = Persona("Carlos", "Perez", 1)
        ritces = Persona("Ritces", "Parra", 2)
        
        self.billetera1 = BilleteraElectronica(13, carlos, 1234, 100)
        self.billetera2 = BilleteraElectronica(12, ritces, 4321, 5000)
        
        
    def debitoPinCorrecto(self):
        debito = Debito(1200, 1, 4321)
        
        self.assertNotEquals(-1, self.billetera1.consumir(debito))
    
    