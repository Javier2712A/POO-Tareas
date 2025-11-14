# ARCHIVO 4: motor.py
# Clase de Composición: Motor

class Motor:
    """Clase Motor para composición con Vehículos"""

    def __init__(self, tipo, potencia):
        self.__tipo = tipo  # Atributo privado - Encapsulamiento
        self.__potencia = potencia  # Atributo privado - Encapsulamiento

    # Implementación de @property (getters)
    @property
    def tipo(self):
        """Getter para tipo de motor"""
        return self.__tipo

    @property
    def potencia(self):
        """Getter para potencia del motor"""
        return self.__potencia

    # Implementación de @setter
    @tipo.setter
    def tipo(self, valor):
        """Setter para tipo de motor"""
        self.__tipo = valor

    @potencia.setter
    def potencia(self, valor):
        """Setter para potencia del motor"""
        self.__potencia = valor

    # Métodos de comportamiento
    def encender_motor(self):
        """Método de comportamiento: encender el motor"""
        return f"Motor {self.__tipo} de {self.__potencia} HP encendido"

    def detener_motor(self):
        """Método de comportamiento: detener el motor"""
        return f"Motor {self.__tipo} detenido"

    # Sobrescritura de __str__()
    def __str__(self):
        """Representación en string del motor"""
        return f"Motor(tipo={self.__tipo}, potencia={self.__potencia} HP)"