import os

class Descifrador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.suma=0
        with open(self.nombre, "r") as self.archivo:
            lineas = self.archivo.readlines()
            self.codigo = ''
            self.texto = "".join(lineas).replace('\n', '')
            i = 0

    def lectura_archivo(self):
        with open(self.nombre, "r") as archivo:
            lineas = archivo.readlines()
            self.codigo = ''
            texto = "".join(lineas).replace('\n', '')
            for caracter in texto:
                if caracter == "a":
                    raise ErrorEntradaA(texto)
                self.codigo += caracter
            return self.codigo

    def elimina_incorrectos(self):
        lista=self.codigo.split(" ")
        self.codigo=''
        for i in lista:
            if len(i) < 6 or len(i) > 7:
                pass
            else:
                self.codigo+=' '+i
        return self.codigo

    def cambiar_binario(self, binario):
        lista = binario.split(' ')
        texto = []
        for x in lista[1:]:
            texto.append(chr(int(x, 2)))
        return texto

    def limpiador(self, lista):
        i = -1
        string = ''
        raise ErrorI(lista)
        while i < len(lista):
            i += 1
            if '$' != lista[i]:
                string += lista[i]
        return string

class Error(Exception):
    """Clase base para excepciones"""
    pass

class ErrorEntradaA(Error):
    def __init__(self,text):
        self.text = text
        
    def modificar_text(self):
        aux = ""
        frases_a_cambiar = ""
        turndown = None
        for element in self.text:
            if element != "a" and turndown == None:
                aux += element
            elif element == "a":
                turndown = True
            else:
                frases_a_cambiar += element
                
        self.text = aux
        frases_correctas = invertir(frases_a_cambiar)
        self.text += frases_correctas
        input("aqui voy")
        os.remove('mensaje_marciano.txt')
        with open('mensaje_marciano.txt',"w") as arch:
            arch.write(self.text)
            
class ErrorI(Error):
    def __init__(self,lista):
        self.lista = lista
    def fix(self):
        i = -1
        string = ''
        while i < len(lista):
            i += 1
            if i == len(lista):
                pass
            elif '$' != lista[i]:
                string += lista[i]
        return string
        
def invertir(var):
    return var[::-1]


if __name__ == "__main__":
    while True:
        try:
            des = Descifrador('mensaje_marciano.txt')
            codigo= des.lectura_archivo()
            codigo=des.elimina_incorrectos()
            lista = des.cambiar_binario(des.codigo)
            texto = des.limpiador(lista)
            print(texto)
            
        except ErrorI as error_b:
            texto = error_b.fix()
            print(texto)
            break
            
    
        except ErrorEntradaA as error_a:
            error_a.modificar_text()
        
        except Exception as err:
            print('Esto no debiese imprimirse')

        

