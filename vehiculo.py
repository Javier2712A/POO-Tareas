# ARCHIVO 1: vehiculo.py

# Clase Principal (Superclase): Vehiculo

# En uso real, importarías la clase Motor

from motor import Motor

class Vehiculo:
    """Clase base Vehiculo - Superclase"""

    def __init__(self, marca, modelo, anio, motor):
        self.__marca = marca  # Atributo privado - Encapsulamiento
        self.__modelo = modelo  # Atributo privado
        self.__anio = anio  # Atributo privado
        self.__motor = motor  # Composición: Vehículo TIENE UN Motor

    # Implementación de @property (getters)
    @property
    def marca(self):
        """Getter para marca"""
        return self.__marca

    @property
    def modelo(self):
        """Getter para modelo"""
        return self.__modelo

    @property
    def anio(self):
        """Getter para año"""
        return self.__anio

    @property
    def motor(self):
        """Getter para motor (composición)"""
        return self.__motor

    # Implementación de @setter
    @marca.setter
    def marca(self, valor):
        """Setter para marca"""
        self.__marca = valor

    @modelo.setter
    def modelo(self, valor):
        """Setter para modelo"""
        self.__modelo = valor

    @anio.setter
    def anio(self, valor):
        """Setter para año"""
        self.__anio = valor

    @motor.setter
    def motor(self, valor):
        """Setter para motor"""
        self.__motor = valor

    # Métodos de comportamiento
    def encender(self):
        """Método de comportamiento: encender el vehículo"""
        return f"{self.__marca} {self.__modelo} encendido. {self.__motor.encender_motor()}"

    def apagar(self):
        """Método de comportamiento: apagar el vehículo"""
        return f"{self.__marca} {self.__modelo} apagado. {self.__motor.detener_motor()}"

    # Sobrescritura de __str__()
    def __str__(self):
        """Representación en string del vehículo"""
        return f"Vehículo: {self.__marca} {self.__modelo} ({self.__anio}) - {self.__motor}"