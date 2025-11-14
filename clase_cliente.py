from datetime import datetime
from persona import Persona


class Cliente(Persona):
    '''
    Crear la clase cliente que hereda de persona
    '''

    def __init__(self, idcliente: int, fecharegistro: str, vip: bool, nombre: str,
                 cedula: str, email: str, genero: str, edad: int, ocupacion: str):
        Persona.__init__(self, nombre=nombre, email=email, genero=genero,
                         edad=edad, ocupacion=ocupacion, cedula=cedula)
        self._idcliente = idcliente
        self._fecharegistro = fecharegistro
        self._vip = vip

    @property
    def idcliente(self):
        return self._idcliente

    @idcliente.setter
    def idcliente(self, nuevo_idcliente):
        self._idcliente = nuevo_idcliente

    @property
    def fecharegistro(self):
        return self._fecharegistro

    @fecharegistro.setter
    def fecharegistro(self, nuevo_fecharegistro):
        self._fecharegistro = nuevo_fecharegistro

    @property
    def vip(self):
        return self._vip

    @vip.setter
    def vip(self, nuevo_vip):
        self._vip = nuevo_vip

    def __str__(self):
        return f'Cliente: {self.__dict__.__str__()}'


if __name__ == '__main__':
    objCliente1 = Cliente(nombre='Javier Agusto', email='javieragusto2002@gmail.com',genero='M',
        ocupacion='Estudiante', edad=22,cedula='958378085',idcliente=7,
        vip=True,fecharegistro=str(datetime.now()))

    print(objCliente1)
    print('*'.center(20, '*'))
    print(f'Nombre: {objCliente1.nombre}')
    print(f'Email: {objCliente1.email}')
    print(f'vip: {objCliente1.vip}')
    print(f'idCliente: {objCliente1.idcliente}')
    print(f'fecharegistro: {objCliente1.fecharegistro}')