# clase cliente con los atributos: cedula, nombres, edad, celular, correo, clave 

from cuenta import Cuenta
class Cliente:
    def __init__(self, cedula, nombres, edad, celular, correo, clave):
        #atributos privados
        self.__cedula = cedula
        self.__nombres = nombres
        self.__edad = edad
        self.__celular = celular
        self.__correo = correo
        self.__clave = clave

        # un cliente puede tener una o mas cuentas
        self.__cuentas = []  # Relacion entre cliente y cuenta

# metodos getter y setter
    def get_cuentas(self) -> list:
        return self.__cuentas

    def set_cuentas(self, cuentas) -> None:
        self.__cuentas = cuentas

    def get_cedula(self) -> str:
        return self.__cedula

    def get_nombres(self) -> str:
        return self.__nombres

    def get_edad(self) -> int:
        return self.__edad

    def get_celular(self) -> str:
        return self.__celular

    def get_correo(self) -> str:
        return self.__correo

    def get_clave(self) -> str:
        return self.__clave

    def set_cedula(self, cedula) -> None:
        self.__cedula = cedula

    def set_nombres(self, nombres) -> None:
        self.__nombres = nombres
    
    def set_edad(self, edad) -> None:
        self.__edad = edad

    def set_celular(self, celular) -> None:
        self.__celular = celular

    def set_correo(self, correo) -> None:
        self.__correo = correo

    def set_clave(self, clave) -> None:
        self.__clave = clave


# metodos: ingresar_sistema, cambiar_clave, actualizar_datos.
    def ingresar_sistema(self) -> bool:
        # logica para ingresar al sistema
        print(f"El cliente {self.__nombres} ha ingresado al sistema")
        return True

    def cambiar_clave(self, celular, correo) -> bool:
        # logica para cambiar la clave usando celular y correo
            if celular != "" and correo != "":
                if celular == self.__celular and correo == self.__correo:
                    print("La clave ha sido cambiada")
                    return True
                else:
                    print("El celular o correo no coinciden")
                    return False

    def actualizar_datos(self, correo, edad) -> bool:
        # logica para actualizar los datos del cliente
        # actulizar correo y edad
        if correo != "" and edad != "":
            if correo == self.__correo and edad == self.__edad:
                print("Los datos han sido actualizados")
                return True
            else:
                print("El correo o edad no coinciden")
                return False
