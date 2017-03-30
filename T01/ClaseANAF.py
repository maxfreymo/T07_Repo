
import User
import Fires
import Resources
import sys

class ANAF:
    
    #Consultas Basicas
    
    def agregar_pronosticos(self):
        print("Estoy agregando pronosticos")
    
    #Otros
    def estrategia_de_extincion(self):
        print("estrategia de extincion")
        
    def cambiar_calendario(self):
        print("cambiando calendario")

    def goodbye(self):
        print()
        print("¡Gracias por trabajar con SuperLuchin! ¡Hasta la proxima!")
        sys.exit()
        
    def salir(self):
        exit_loop = False

        functions = {"1": User.Usuario().cambiar_usuario, "2": self.goodbye, "3": self.menu_anaf}

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


    def leer_2 (self):
        exit_loop = False

        functions = {"1": Resources.Recurso().leer_recursos("YES"), "2": Resources.Recurso().ver_recursos_mas_utilizados, "3": Resources.Recurso().ver_recursos_mas_efectivos, "4": self.leer_archivos}

        while not exit_loop:
            print(""" Elija una opcion:

                1. Todo el archivo
                2. Recursos mas utilizados
                3. Recursos mas efectivos
                4. Ninguno. Volver atras.
        
                Respuesta: """)

            user_entry = input()

            if user_entry in functions:
                functions[user_entry]()
            else:
                print("Respuesta Invalida, vuelva a intentarlo")

                
    def leer_3 (self):
        exit_loop = False

        functions = {"1": Fires.Incendio().leer_incendios, "2": Fires.Incendio().ver_incendios_activos, "3": Fires.Incendio().ver_incendios_apagados, "4": self.leer_archivos}

        while not exit_loop:
            print(""" Elija una opcion:

                1. Todo el archivo
                2. Incendios activos
                3. Incendios apagados
                4. Ninguno. Volver atras.
        
                Respuesta: """)

            user_entry = input()

            if user_entry in functions:
                functions[user_entry]()
            else:
                print("Respuesta Invalida, vuelva a intentarlo")
                
                
    def leer_archivos(self):
        exit_loop = False

        functions = {"1": User.Usuario().leer_usuarios, "2": self.leer_2, "3": self.leer_3, "4": self.menu_anaf}

        while not exit_loop:
            print(""" ¿Cual archivo desea leer?

                1. Usuarios
                2. Recursos
                3. Incendios
                4. Ninguno. Volver al menu principal
        
                Respuesta: """)

            user_entry = input()

            if user_entry in functions:
                functions[user_entry]()
            else:
                print("Respuesta Invalida, vuelva a intentarlo")



    def menu_anaf(self):
        exit_loop = False

        functions = {"1": self.leer_archivos, "2": User.Usuario().crear_usuario, "3": self.agregar_pronosticos, "4": Fires.Incendio().agregar_incendios, "5": self.estrategia_de_extincion, "6": self.cambiar_calendario, "7": self.salir }

        while not exit_loop:
            print("""*** MENU PRINCIPAL ***

                Seleccione una opcion:

                1. Leer Archivos
                2. Crear nuevo Usuario
                3. Agregar Pronosticos
                4. Agregar Incendios
                5. Realizar estrategia de extincion 
                6. Cambiar Fecha/Hora
                7. Salir
                
                Respuesta: """)

            user_entry = input()

            if user_entry in functions:
                functions[user_entry]()
            else:
                print("Respuesta Invalida, vuelva a intentarlo")


    
"""funcionario = ANAF()
funcionario.menu_anaf()"""






        
