 RESUMEN DEL PROGRAMA
Sistema de Gestión de Vehículos con Programación Orientada a Objetos (POO)
¿Qué hace el programa?
Este programa simula un sistema de vehículos (automóviles y motocicletas) usando los 4 pilares de la Programación Orientada a Objetos:
Conceptos implementados:

HERENCIA:
Hay una clase principal llamada Vehiculo (la "mamá")
De ella heredan Automovil y Motocicleta (los "hijos")
Los hijos tienen todo lo que tiene la mamá, más cosas propias


COMPOSICIÓN:
Cada vehículo "TIENE UN" motor
El motor es un objeto independiente que se le asigna al vehículo


ENCAPSULAMIENTO:
Los datos están protegidos (privados) con __
Solo se pueden ver o modificar mediante métodos especiales (@property y @setter)


MÉTODOS DE COMPORTAMIENTO:
Los objetos pueden hacer acciones: encender, apagar, tocar claxon, hacer caballito, etc.


 ¿Qué contiene?
5 archivos de código Python
4 clases: Motor, Vehiculo, Automovil, Motocicleta
1 programa principal que crea 2 autos y 2 motos, les asigna motores, y demuestra todos sus métodos

Objetivo:
Demostrar de forma práctica cómo funciona la POO en Python, cumpliendo con todos los requisitos de la actividad asincrónica.

En pocas palabras: Es un programa que crea autos y motos virtuales, cada uno con su propio motor, y les hace realizar diferentes acciones para mostrar cómo funciona la programación orientada a objetos.
