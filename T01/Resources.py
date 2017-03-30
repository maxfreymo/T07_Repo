from User import buscador
import os

class Recurso:
    def leer_recursos(self, impresion):
        archivo_recursos = open("recursos.csv","r",encoding="utf-8")
        arch_del_momento = open("recursosCOPY.csv","w",encoding="utf-8")
        dic_recursos = {}
        i=0
        for linea in archivo_recursos:
            Linea = linea.strip().split(",")
            if i == 0:
                j = 0
                for element in Linea:
                    if element == "id:string":
                        st = Linea.pop(j)
                        break
                    else: j+=1

                contador_tipo = buscador("tipo:string", Linea)
                contador_lat = buscador("lat:float", Linea)
                contador_lon = buscador("lon:float", Linea)
                contador_vel = buscador("velocidad:int", Linea)
                contador_aut = buscador("autonomia:int", Linea)
                contador_delay = buscador("delay:int", Linea)
                contador_tasa_extincion = buscador("tasa_extincion:int", Linea)
                contador_costo = buscador("costo:int", Linea)

                yatusae = "no"
                if buscador("ubicacion_geo:list", Linea) == False:
                    Linea.append("ubicacion_geo:list")
                    Linea.append("estado_actual:str")
                    yatusae = "si"

                dic_recursos["informacion"] = Linea
                i+=1
                

            else:
                id_recurso = Linea.pop(j)
                
                if yatusae == "si":
                    Linea.append([Linea[contador_lat],Linea[contador_lon]])
                    Linea.append("standby")
                    
                dic_recursos[id_recurso] = Linea
                i+=1
                
            linea_programa = Linea

            if i == 1:
                linea_programa.insert(j,st)
            else:
                linea_programa.insert(j,id_recurso)
                
            paso = 0
            for variable in linea_programa:
                if paso == 0:
                    Escribir_linea_programa = str(variable)
                    paso += 1
                else:
                    Escribir_linea_programa = Escribir_linea_programa + "," + str(variable)
                
            arch_del_momento.write(Escribir_linea_programa + "\n")

        archivo_recursos.close()
        arch_del_momento.close()
        
        with open("recursosCOPY.csv","r",encoding="utf-8") as arch_del_momento:
            with open("recursos.csv","w",encoding="utf-8") as archivo_recursos:
                for linea_renovada in arch_del_momento:
                    archivo_recursos.write(linea_renovada)
        
        os.remove("recursosCOPY.csv")
        
        if impresion == "NO":
            return(dic_recursos)
        
        self.imprimir_recursos()
        
    #Se imprimen todos los recursos en manera de lista para optimizar el programa.
    #Imprimir el diccionario de recursos demoraba mucho.
        
    def imprimir_recursos(self):
        with open("recursos.csv","r", encoding="utf-8") as archivo_recursos:
            for linea in archivo_recursos:
                print(linea.strip().split(","))
                print()

    def ver_recursos_mas_utilizados(self):
        print("Estoy leyendo RECURSOS MAS UTILIZADOS")
        
    def ver_recursos_mas_efectivos(self):
        print("Estoy leyendo RECURSOS MAS EFECTIVOS")

"""Recurso().leer_recursos("NO")"""
