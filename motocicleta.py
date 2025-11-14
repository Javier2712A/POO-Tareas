# ARCHIVO 3: motocicleta.py

# Clase Hija 2: Motocicleta (Hereda de Vehiculo)

# from vehiculo import Vehiculo  # En uso real, importarías la clase Vehiculo

from vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    """Clase Motocicleta - Hereda de Vehiculo"""

    def __init__(self, marca, modelo, anio, motor, cilindraje):
        # Herencia: llamada a la superclase con super()
        super().__init__(marca, modelo, anio, motor)
        self.__cilindraje = cilindraje  # Atributo adicional

    # Implementación de @property y @setter para atributo adicional
    @property
    def cilindraje(self):
        """Getter para cilindraje"""
        return self.__cilindraje

    @cilindraje.setter
    def cilindraje(self, valor):
        """Setter para cilindraje"""
        self.__cilindraje = valor

    # Métodos de comportamiento específicos de Motocicleta
    def hacer_caballito(self):
        """Método de comportamiento: hacer caballito"""
        return f"¡{self.marca} {self.modelo} haciendo un caballito espectacular!"

    def usar_parada_arranque(self):
        """Método de comportamiento: usar parada de arranque"""
        return f"Usando parada de arranque en {self.marca} {self.modelo} {self.__cilindraje}cc"

    # Sobrescritura de __str__() usando super()
    def __str__(self):
        """Representación en string de la motocicleta"""
        return f"Motocicleta: {self.marca} {self.modelo} ({self.anio}) - {self.__cilindraje}cc - {self.motor}"