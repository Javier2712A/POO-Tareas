# ARCHIVO 5: main.py
# Programa Principal - Clase Principal

from motor import Motor
from vehiculo import Vehiculo
from automovil import Automovil
from motocicleta import Motocicleta

def main():
    """Programa principal para demostrar el sistema de vehículos"""
    print("SISTEMA DE GESTIÓN DE VEHÍCULOS - POO EN PYTHON")
    print("Herencia, Composición, Encapsulamiento y Métodos de Comportamiento")
    print()

    # PASO 1: Crear motores (Composición)
    print("PASO 1: CREANDO VEHICULOS (Composición)")
    motor_auto1 = Motor("Gasolina V6", 280)
    motor_auto2 = Motor("Eléctrico", 450)
    motor_moto1 = Motor("4 Tiempos", 150)
    motor_moto2 = Motor("2 Tiempos", 125)
    print(f" {motor_auto1}")
    print(f" {motor_auto2}")
    print(f" {motor_moto1}")
    print(f" {motor_moto2}")
    print()

    # PASO 2: Crear al menos 2 automóviles
    print("PASO 2: CREANDO AUTOMÓVILES (Herencia de Vehiculo)")
    auto1 = Automovil("Toyota", "Camry", 2023, motor_auto1, 4)
    auto2 = Automovil("Tesla", "Model 3", 2024, motor_auto2, 4)
    print(f" {auto1}")
    print(f" {auto2}")
    print()

    # PASO 3: Crear al menos 2 motocicletas
    print("PASO 3: CREANDO MOTOCICLETAS (Herencia de Vehiculo)")
    moto1 = Motocicleta("Yamaha", "YZF-R15", 2023, motor_moto1, 155)
    moto2 = Motocicleta("Kawasaki", "Ninja 400", 2024, motor_moto2, 400)
    print(f" {moto1}")
    print(f" {moto2}")
    print()

    # PASO 4: Asignar un motor a cada objeto (Ya asignado en la creación)
    print("PASO 4: MOTORES ASIGNADOS")
    print(f" {auto1.marca} {auto1.modelo} tiene: {auto1.motor}")
    print(f" {auto2.marca} {auto2.modelo} tiene: {auto2.motor}")
    print(f" {moto1.marca} {moto1.modelo} tiene: {moto1.motor}")
    print(f" {moto2.marca} {moto2.modelo} tiene: {moto2.motor}")
    print()

    # PASO 5: Ejecutar varios métodos de comportamiento - AUTOMÓVILES
    print("PASO 5: DEMOSTRANDO MÉTODOS DE COMPORTAMIENTO - AUTOMÓVILES")
    print(f" {auto1.marca} {auto1.modelo}:")
    print(f" {auto1.encender()}")
    print(f" {auto1.abrir_maletero()}")
    print(f" {auto1.tocar_claxon()}")
    print(f" {auto1.apagar()}")
    print()

    print(f" {auto2.marca} {auto2.modelo}:")
    print(f" {auto2.encender()}")
    print(f" {auto2.abrir_maletero()}")
    print(f" {auto2.tocar_claxon()}")
    print(f" {auto2.apagar()}")
    print()

    # PASO 6: Ejecutar varios métodos de comportamiento - MOTOCICLETAS
    print("PASO 6: DEMOSTRANDO MÉTODOS DE COMPORTAMIENTO - MOTOCICLETAS")
    print(f" {moto1.marca} {moto1.modelo}:")
    print(f" {moto1.encender()}")
    print(f" {moto1.hacer_caballito()}")
    print(f" {moto1.usar_parada_arranque()}")
    print(f" {moto1.apagar()}")
    print()

    print(f"  {moto2.marca} {moto2.modelo}:")
    print(f"  {moto2.encender()}")
    print(f"  {moto2.hacer_caballito()}")
    print(f"  {moto2.usar_parada_arranque()}")
    print(f"  {moto2.apagar()}")
    print()

    # PASO 7: Demostrar Encapsulamiento (@property y @setter)
    print("PASO 7: DEMOSTRANDO ENCAPSULAMIENTO (@property y @setter)")
    print(f"Marca original de auto1: {auto1.marca}")
    auto1.marca = "Honda"  # Usando @setter
    print(f"Marca modificada de auto1: {auto1.marca}")  # Usando @property
    print()

    print(f"Cilindraje original de moto1: {moto1.cilindraje}cc")
    moto1.cilindraje = 160  # Usando @setter
    print(f"Cilindraje modificado de moto1: {moto1.cilindraje}cc")  # Usando @property
    print()

    print(f"Potencia original del motor de moto2: {moto2.motor.potencia} HP")
    moto2.motor.potencia = 135  # Usando @setter del Motor
    print(f"Potencia modificada del motor de moto2: {moto2.motor.potencia} HP")
    print()

    # PASO 8: Imprimir objetos con print() - llama a __str__()
    print("PASO 8: IMPRIMIENDO OBJETOS CON print() - Usa __str__()")
    print(" TODOS LOS AUTOMÓVILES:")
    print(auto1)  # Llama a __str__()
    print(auto2)  # Llama a __str__()
    print()

    print(" TODAS LAS MOTOCICLETAS:")
    print(moto1)  # Llama a __str__()
    print(moto2)  # Llama a __str__()
    print()

    print(" PROGRAMA FINALIZADO - Todos los requerimientos cumplidos")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()