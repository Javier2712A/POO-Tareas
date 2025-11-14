# ARCHIVO 2: automovil.py

# Clase Hija 1: Automovil (Hereda de Vehiculo)

# from vehiculo import Vehiculo  # En uso real, importarías la clase Vehiculo

from vehiculo import Vehiculo

class Automovil(Vehiculo):
    """Clase Automovil - Hereda de Vehiculo"""

    def __init__(self, marca, modelo, anio, motor, numero_puertas):
        # Herencia: llamada a la superclase con super()
        super().__init__(marca, modelo, anio, motor)
        self.__numero_puertas = numero_puertas  # Atributo adicional

    # Implementación de @property y @setter para atributo adicional
    @property
    def numero_puertas(self):
        """Getter para número de puertas"""
        return self.__numero_puertas

    @numero_puertas.setter
    def numero_puertas(self, valor):
        """Setter para número de puertas"""
        self.__numero_puertas = valor

    # Métodos de comportamiento específicos de Automovil
    def abrir_maletero(self):
        """Método de comportamiento: abrir maletero"""
        return f"Maletero del {self.marca} {self.modelo} abierto"

    def tocar_claxon(self):
        """Método de comportamiento: tocar claxon"""
        return f"¡Beep beep! Claxon del {self.marca} {self.modelo}"

    # Sobrescritura de __str__() usando super()
    def __str__(self):
        """Representación en string del automóvil"""
        return f"Automóvil: {self.marca} {self.modelo} ({self.anio}) - {self.__numero_puertas} puertas - {self.motor}"