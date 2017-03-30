#Creo la clase Usuario que almacenara los datos del csv de usuarios
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random

usuarioActual = []

def buscador (palabra, lista):
    for element in lista:
        if element == palabra:
            return (lista.index(palabra))
    return(False)
        
class Usuario :
    
    def __init__ (self):
        pass

    def ingreso_usuario(self):

        archivo = open("usuarios.csv", "r",encoding='utf-8')
        i=0
        lista_usuarios = []
        for linea in archivo:
            if i==0:
                Linea = linea.strip().split(",")
                for element in Linea:
                    element = []
                    lista_usuarios.append(element)
                    i+=1
            else: pass
        
            Linea = linea.strip().split(",")
            k=0
            for element in Linea:
                lista_usuarios[k].append(element)
                k+=1
                
        archivo.close()
        
        usuario_valido = False

        while usuario_valido == False:
            while True:
                try:
                    user = str(input ("Porfavor, ingrese nombre de usuario: "))
                    print()
                    break
                except ValueError:
                    print("Usuario No valido. Intentelo de nuevo")
                    print()

            for lista in  lista_usuarios:
                if lista[0] == "nombre:string":
                    numero_fila=-1
                    j=0
                    for element in lista:
                        numero_fila +=1
                        if user == element:
                            while True:
                                try:
                                    password = str(input("Ingrese contraseña: "))
                                    print()
                                    for lista_password in lista_usuarios:
                                        if lista_password[j] == password:
                                            print("¡Bienvenido ",user,"!")
                                            usuario_valido = True
                                            print()
                                            archivoP = open("usuarios.csv","r", encoding='utf-8')
                                            filas = 0
                                            for line in archivoP:
                                                if filas == 0:
                                                    orden = line.strip().split(",")
                                                    contador_id = buscador("id:string", orden)
                                                    contador_nombre = buscador("nombre:string", orden)
                                                    contador_contraseña = buscador("contraseña:string", orden)
                                                    contador_recurso = buscador("recurso_id:string", orden)
                                                    
                                                if filas == numero_fila:
                                                    lista_desordenada = line.strip().split(",")
                                                    usuarioActual.append(lista_desordenada[contador_id])
                                                    usuarioActual.append(lista_desordenada[contador_nombre])
                                                    usuarioActual.append(lista_desordenada[contador_contraseña])
                                                    usuarioActual.append(lista_desordenada[contador_recurso])
                                                    archivoP.close()
                                                    
                                                    break
                                                    
                                                else:
                                                    filas += 1
                                            break
                                
                                    if usuario_valido == True:
                                        break
                                    else: pass
                            
                                    print("¡Contraseña incorrecta! ")
                                    print()
                                    while True:
                                        resp1 = input("¿Desea intentarlo de nuevo o salir? (intentar/salir): ")
                                        print()
                                        if resp1 == "intentar":
                                            break
                                        elif resp1 == "salir":
                                            print("¡Hasta pronto!")
                                            print()
                                            sys.exit()
                                        else:
                                            print("Ingrese respuesta valida.")
                                            print()
                                
                        

                                except ValueError:
                                    print("Contraseña No valida. Intentelo de nuevo")
                                    print()

                        else: j+=1
            
                    if usuario_valido == True:
                        break
                        

                    else:
                        print("Este usuario No existe.")
                        print()
                        while True:
                            resp2 = str(input("¿Desea intentarlo de nuevo o salir? (intentar/salir): "))
                            print()
                            if resp2 == "intentar":
                                break
                            elif resp2 == "salir":
                                print("¡Hasta la proxima!")
                                print()
                                sys.exit()
                            else:
                                print("Ingrese respuesta valida")
                                print()
                else: pass
                

    def crear_usuario(self):
        
        with open("usuarios.csv","r", encoding="utf-8") as ARCHIVO:
            numeroF1 = -1
            for line in ARCHIVO:
                numeroF1 += 1
                if numeroF1 == 0:
                    orden_usuarios = line.strip().split(",")

        with open("recursos.csv","r",encoding = "utf-8") as ARCHIVO:
            numeroF2 = -1
            for line in ARCHIVO:
                numeroF2 += 1
                if numeroF2 == 0:
                    orden_recursos = line.strip().split(",")

        
        ARCHIVO1 = open("usuarios.csv","a", encoding="utf-8")
        
        #Creo el nuevo usuario y ordeno sus componentes como en el archivo
            
        contador_id = buscador("id:string", orden_usuarios)
        contador_nombre = buscador("nombre:string", orden_usuarios)
        contador_contraseña = buscador("contraseña:string", orden_usuarios)
        contador_recurso = buscador("recurso_id:string", orden_usuarios)

        print("Ingrese los datos del nuevo usuario:")
        print("")

        while True:
            try:
                nombre_usuario = input("Nombre usuario: ")
                break
            except:
                print("Error. Ingrese nombre valido")
                
        while True:
            try:
                contraseña_usuario = input("Contraseña usuario: ")
                break
            except:
                print("Error. Ingrese contraseña valida")

        exit_loop = False
        functions = {"1": "ANAF", "2": "BOMBEROS", "3": self.elegir_nave(), "4": "BRIGADA"}

        while not exit_loop:
            print("""Seleccione el recurso al cual pertenece:

                    1. ANAF
                    2. BOMBEROS
                    3. PILOTOS (AVION/HELICOPTERO)
                    4. BRIGADISTAS

                    Respuesta: """)

            user_entry = input()

            if user_entry in functions:
                nombre_recurso = functions[user_entry]
                break
            else:
                print("Respuesta Invalida, vuelva a intentarlo")
                
        lista_Random = ["espacio1","espacio2","espacio3","espacio4"]

        lista_Random.insert(contador_nombre, nombre_usuario)
        lista_Random.pop(contador_nombre + 1)

        lista_Random.insert(contador_contraseña, contraseña_usuario)
        lista_Random.pop(contador_contraseña + 1)

        lista_Random.insert(contador_id,str(numeroF1))
        lista_Random.pop(contador_id + 1)

        if nombre_recurso == "ANAF":
            lista_Random.insert(contador_recurso, "")
            lista_Random.pop(contador_recurso+1)
            
        else:
            lista_Random.insert(contador_recurso, str(numeroF2))
            lista_Random.pop(contador_recurso + 1)

        NuevoUsuario =  ",".join(lista_Random)
        
        ARCHIVO1.write(NuevoUsuario + "\n")
        ARCHIVO1.close()

        #Ahora creare un recurso asociado al nuevo usuario con la misma logica anterior.
        #Si es ANAF no se crea ningun recurso.

        if nombre_recurso == "ANAF":
            return()

        ARCHIVO2 = open("recursos.csv","a",encoding="utf-8")
        
        contador_id_R = buscador("id:string", orden_recursos)
        contador_tipo = buscador("tipo:string", orden_recursos)
        contador_lat = buscador("lat:float", orden_recursos)
        contador_lon = buscador("lon:float", orden_recursos)
        contador_vel = buscador("velocidad:int", orden_recursos)
        contador_aut = buscador("autonomia:int", orden_recursos)
        contador_delay = buscador("delay:int", orden_recursos)
        contador_tasa_extincion = buscador("tasa_extincion:int", orden_recursos)
        contador_costo = buscador("costo:int", orden_recursos)
        
        LRA = [1,2,3,4,5,6,7,8,9]
        
        LRA.insert(contador_id_R, str(numeroF2))
        LRA.pop(contador_id_R + 1)
        
        LRA.insert(contador_tipo, nombre_recurso)
        LRA.pop(contador_tipo + 1)

        lat = -(random.randint(3200000000000000,3800000000000000)/100000000000000)
        
        LRA.insert(contador_lat, str(lat))
        LRA.pop(contador_lat + 1)

        lon = -(random.randint(7000000000000000,7200000000000000)/100000000000000)

        LRA.insert(contador_lon, str(lon))
        LRA.pop(contador_lon + 1)

        if nombre_recurso == "BOMBEROS":
            vel = random.randint(50,65)
        elif nombre_recurso == "BRIGADA":
            vel = random.randint(95,105)
        elif nombre_recurso == "HELICOPTERO":
            vel = random.randint(150,200)
        else:
            vel = random.randint(250,800)
        

        LRA.insert(contador_vel, str(vel))
        LRA.pop(contador_vel + 1)

        if nombre_recurso == "BOMBEROS" or "BRIGADA":
            aut = random.randint(3,8)
            
        else:
            aut = random.randint(0,2)

        LRA.insert(contador_aut, str(aut))
        LRA.pop(contador_aut + 1)

        if nombre_recurso == "BOMBEROS" or "BRIGADA":
            dela_y = random.randint(2,4)
            
        else:
            dela_y = 1

        LRA.insert(contador_delay, str(dela_y))
        LRA.pop(contador_delay + 1)

        if nombre_recurso == "BOMBEROS":
            tasa = random.randint(1600000000,2200000000)
        elif nombre_recurso == "BRIGADA":
            tasa = random.randint(2400000000,2600000000)
        elif nombre_recurso == "HELICOPTERO":
            tasa = random.randint(3800000000,4200000000)
        else:
            tasa = random.randint(5000000000,10000000000)

        LRA.insert(contador_tasa_extincion, str(tasa))
        LRA.pop(contador_tasa_extincion + 1)

        if nombre_recurso == "BOMBEROS":
            costo = random.randint(1300,1700)
        elif nombre_recurso == "BRIGADA":
            costo = random.randint(1900,2300)
        elif nombre_recurso == "HELICOPTERO":
            costo = random.randint(2800,3200)
        else:
            costo = random.randint(4000,10000)

        LRA.insert(contador_costo, str(costo))
        LRA.pop(contador_costo + 1)

        recurso_asociado =  ",".join(LRA)

        ARCHIVO2.write(recurso_asociado + "\n")
        ARCHIVO2.close()

    def leer_usuarios(self):
        with open("usuarios.csv","r", encoding="utf-8") as archivo_usuarios:
            for linea in archivo_usuarios:
                print(linea.strip().split(","))
                print()
                
    def cambiar_usuario(self):
        print("A continuacion realice su cambio:")

    def elegir_nave (self):
        eleccion = random.randint(1,2)
        if eleccion == 1:
            return("HELICOPTERO")
        else: return("AVION")
        
        


"""arturito = Usuario()
arturito.crear_usuario()"""








        
