import User
import  Resources
import sys

class Operario:
    
    def __init__(self, id_recurso):
        self.id_recurso = id_recurso


    def info_recurso(self):
        dicc_recursos = Resources.Recurso().leer_recursos("NO")
        print(dicc_recursos[self.id_recurso])
    
    def info_incendio (self):
        print("Leyendo info incendio asignado")
        

    def goodbye(self):
        print()
        print("¡Gracias por trabajar con SuperLuchin! ¡Hasta la proxima!")
        sys.exit()
        
    def salir(self):
        
        exit_loop = False
        
        functions = {"1": User.Usuario().cambiar_usuario, "2": self.goodbye, "3": self.menu_operario}

        while not exit_loop:
            
            print(""" Seleccione:

                1. Cambiar Usuario
                2. Salir del programa
                3. Ninguno. Volver atras.
        
                Respuesta: """)

            user_entry = input()

            if user_entry in functions:
                functions[user_entry]()
            else:
                print("Respuesta Invalida, vuelva a intentarlo")

    def menu_operario (self):
        
        exit_loop = False

        functions = {"1": self.info_recurso, "2": self.info_incendio, "3": self.salir}

        while not exit_loop:
            print(""" Seleccione:

                1. Leer recurso perteneciente
                2. Leer incendio asignado
                3. Salir
        
                Respuesta: """)

            user_entry = input()

            if user_entry in functions:
                functions[user_entry]()
            else:
                print("Respuesta Invalida, vuelva a intentarlo")

