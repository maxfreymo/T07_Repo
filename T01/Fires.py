
class Incendio:
    def agregar_incendios(self):
        print("Estoy agregando incendios")

    def leer_incendios(self):

        archivo_incendios = open("incendios.csv","r",encoding="utf-8")
        dic_incendios = {}
        i=0
        for linea in archivo_incendios:
            Linea = linea.strip().split(",")
            if i == 0:
                j = 0
                for element in Linea:
                    if element == "id:string":
                        Linea.pop(j)
                        break
                    else: j+=1
                Linea.append("Porcentaje de extincion")
                Linea.append("Recursos trabajando en el lugar")
                dic_incendios["informacion"] = Linea
                i+=1
            
            else:
                id_incendio = Linea.pop(j)
                Linea.append("pe"+str(i))
                Linea.append("rt"+str(i))
                dic_incendios[id_incendio] = Linea
                i+=1

            print(dic_incendios)
            input()

    def ver_incendios_activos(self):
        print("Estoy leyendo INCENDIOS ACTIVOS")

    def ver_incendios_apagados(self):
        print("Estoy leyendo INCENDIOS APAGADOS")
