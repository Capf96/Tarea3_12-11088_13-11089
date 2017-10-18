class Persona(object):

    def __init__(self, nombres, apellidos, ci):

        if type(nombres) != str:

            raise TypeError("Los nombres deben ser de tipo 'str'")

        

        if type(apellidos) != str:

            raise TypeError("Los apellidos deben ser de tipo 'str")

        

        if type(ci) != int:

            raise TypeError("La cedula de identidad debe ser un entero")


        

        self.nombres = nombres

        self.apellidos = apellidos

        self.ci = ci