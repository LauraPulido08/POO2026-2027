# uso de las clases cliente y cuenta
from cliente import Cliente
from cuenta import Cuenta

# crear un cliente
cliente = Cliente("1234567890", "Juan Perez", 30, "1234567890", "juanperez@gmail.com", "123456")

# crear una cuenta
cuenta = Cuenta("1234567890", 1000, "Ahorro")

# agregar la cuenta al cliente
cliente.agregar_cuenta(cuenta)

# ingresar al sistema
cliente.ingresar_sistema()

# cambiar la clave
cliente.cambiar_clave()

# actualizar los datos
cliente.actualizar_datos()

# mostrar las cuentas del cliente
print(cliente.get_cuentas())

# retirar dinero de la cuenta
cuenta.retirar(100)

# mostrar las transacciones de la cuenta
print(cuenta.get_transacciones())
