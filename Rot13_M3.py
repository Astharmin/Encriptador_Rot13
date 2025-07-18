import os
from enum import Enum, auto


class OpcionMenu(Enum):
    CIFRAR = auto()
    DESCIFRAR = auto()
    SALIR = auto()


class LimpiadorPantalla:
    @staticmethod
    def limpiar():
        os.system('cls' if os.name == 'nt' else 'clear')


class CifradorRot13:
    @staticmethod
    def cifrar(texto: str) -> str:
        resultado = []
        for letra in texto:
            if 'a' <= letra <= 'z':
                nueva_letra = chr(((ord(letra) - ord('a') + 13) % 26)+ ord('a'))

            elif 'A' <= letra <= 'Z':
                nueva_letra = chr(((ord(letra) - ord('A') + 13) % 26)+ ord('A'))
            else:
                nueva_letra = letra
            resultado.append(nueva_letra)
        return ''.join(resultado)


class InterfazUsuario:
    @staticmethod
    def mostrar_titulo():

        print(' Encriptador de Mensajes (Rot13_M1) '.center(50, '-'))

    @staticmethod
    def mostrar_menu() -> OpcionMenu:

        while True:
            try:
                opcion = int(input('''¿Qué quieres hacer?

1. Cifrar Mensaje
2. Descifrar mensaje
3. Salir

Opción: '''))

                if opcion == 1:
                    return OpcionMenu.CIFRAR
                elif opcion == 2:
                    return OpcionMenu.DESCIFRAR
                elif opcion == 3:
                    return OpcionMenu.SALIR
                else:
                    print("Opción no válida. Por favor ingrese 1, 2 o 3.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")

    @staticmethod
    def preguntar_continuar() -> bool:

        while True:
            respuesta = input("\n¿Quieres seguir en el programa? (S/N): ").lower()
            if respuesta == 's':
                return True
            elif respuesta == 'n':
                return False
            else:
                print("Por favor ingrese S o N.")

    @staticmethod
    def obtener_mensaje(accion: str) -> str:

        return input(f'Escribir mensaje a {accion}: \n')

    @staticmethod
    def mostrar_resultado(mensaje: str, accion: str):

        print(f'\nMensaje {accion}:\n{mensaje}\n')


class AplicacionRot13:
    def __init__(self):
        self.cifrador = CifradorRot13()
        self.interfaz = InterfazUsuario()
        self.limpiador = LimpiadorPantalla()

    def ejecutar(self):

        self.limpiador.limpiar()
        self.interfaz.mostrar_titulo()

        while True:
            opcion = self.interfaz.mostrar_menu()

            if opcion == OpcionMenu.SALIR:
                self.limpiador.limpiar()
                print(' Saliendo del programa '.center(30, '-'))
                break

            accion = "cifrar" if opcion == OpcionMenu.CIFRAR else "descifrar"

            self.limpiador.limpiar()
            mensaje = self.interfaz.obtener_mensaje(accion)
            resultado = self.cifrador.cifrar(mensaje)
            self.interfaz.mostrar_resultado(resultado, accion)

            if not self.interfaz.preguntar_continuar():
                self.limpiador.limpiar()
                print(' Saliendo del programa '.center(30, '-'))
                break

            self.limpiador.limpiar()


if __name__ == '__main__':
    app = AplicacionRot13()
    app.ejecutar()