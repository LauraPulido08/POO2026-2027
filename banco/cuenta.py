# clase cuenta con los atributos: numero_cuenta, saldo, tipo_cuenta
class Cuenta:
    def __init__(self, numero_cuenta, saldo, tipo_cuenta):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta

    def retirar(self, cantidad):
        self.saldo -= cantidad


    def registrar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)

    def get_transacciones(self):
        return self.transacciones