#Modifica el calendario para guardar la fecha ingresada como numeros para poder crear un contador de los dias q han pasado despues

class Calendario:
    def __init__ (self):
        self.año = range(2000, 2401)
        self.mes = range(1,13)
        self.dia_tipo1 = range(1,32)
        self.dia_tipo2 = range(1,31)
        self.dia_feb_b = range(1,30)
        self.dia_feb_n = range(1,29)
        self.hora = range(0,24)
        self.minutos = range(0,61)
        self.segundos = range(0,61)
        self.fecha = []
        self.reloj = []

    def setear_fecha (self):
        #Ingreso Año
        valido = False
        while valido == False:
            try:
                year = int(input("Ingrese año: "))
                valido = year in self.año
                if valido == False:
                    print()
                    print("Año invalido. Intentelo de nuevo")
                else:
                    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
                        tipo_año = "Bisiesto" 
                    else:
                        tipo_año = "Normal"
            except:
                print()
                print("Año invalido. Intentelo de nuevo")
            print()

        #Ingreso Mes                                                     
        valido = False
        while valido == False:
            try:
                month = int(input("Ingrese mes: "))
                valido = month in self.mes
                if valido == False:
                    print()
                    print("Mes invalido. Intentelo de nuevo.")
            except:
                print()
                print("Mes invalido. Intentelo de nuevo.")
            print()
                            
        #Ingreso Dia
        valido = False 
        while valido == False:
            try:
                day = int(input("Ingrese dia: "))
                if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                    valido = day in self.dia_tipo1
                    if valido == False:
                        print()
                        print("Dia invalido. Intentelo de nuevo")
                elif month == 4 or 6 or 9 or 11:
                    valido = day in self.dia_tipo2
                    if valido == False:
                        print()
                        print("Dia invalido. Intentelo de nuevo")
                else:
                    if tipo_año == "Bisiesto":
                        valido = day in self.dia_feb_b
                    else:
                        valido = day in self.dia_feb_n
                    if valido == False:
                        print()
                        print("Dia invalido. Intentelo de nuevo")
            except:
                print()
                print("Dia invalido. Intentelo de nuevo")
            print()
                        
        self.fecha = [year, month, day]

    def setear_reloj (self):
        valido = False
        while valido == False:
            try:
                hour = int(input("Ingrese hora (formato 24hrs): "))
                valido = hour in self.hora
                if valido == False:
                    print("Hora invalida. Ingresela de nuevo")
            except:
                print()
                print("Hora invalida. Ingresela de nuevo")
            print()

        valido = False
        while valido == False:
            try:
                minutes = int(input("Ingrese minutos: "))
                valido = minutes in self.minutos
                if valido == False:
                    print("Cantidad invalida. Intentelo de nuevo")
            except:
                print()
                print("Cantidad invalida. Intentelo de nuevo")
            print()

        valido = False
        while valido == False:
            try:
                seconds = int(input("Ingrese segundos: "))
                valido = seconds in self.segundos
                if valido == False:
                    print("Cantidad invalida. Intentelo de nuevo")
            except:
                print()
                print("Cantidad invalida. Intentelo de nuevo")
            print()

        self.reloj = [hour, minutes, seconds]

    def imprimir_fecha (self):
        print("La fecha es:", self.fecha[0],"-", self.fecha[1],"-", self.fecha[2])

    def imprimir_hora(self):
        print("La hora es:", self.reloj[0],":",self.reloj[1],":",self.reloj[2])

                         
        
        
