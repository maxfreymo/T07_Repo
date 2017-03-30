
#No pude descargar las cosas asiq las copie directo de internet
import unittest
import main

class TestearFormato(unittest.TestCase):
    
    def setUp(self):
        self.stats = Descifrador("mensaje_marciano.txt")
        
    def test_archivo(self):
        i=0
        j=0
        for element in self.stats:
            i+=1
            if type(element) != str:
                return False
            elif:
                j+=float(element)
        if i != 408:
            return False
        elif j != 253:
            return False

        return True
        
class TestearMensaje(unittest.TestCase):
    
    def setUp(self):
        self.stats = Descifrador("mensaje_marciano.txt")
        
    def test_incorrectos(self, texto):
        lista=texto.split(" ")
        texto=""
        for i in lista:
            if len(i) < 6 or len(i) > 7:
                #Si el texto posee secuencias codificadas incorrectas devuelvo False
                return False
            else:
                self.codigo+=' '+i
                
        #Si el testeo es exitoso devuelvo el texto
        return texto
        
    def test_caracteres(self,lista):
        i = -1
        string = ''
        raise ErrorI(lista)
        while i < len(lista):
            i += 1
            if '$' != lista[i]:
                string += lista[i]
        return string
        
    def test_codificacion(self, texto):
        #Si es que esta malo retorna False
        for element in texto:
            if element == "1" or element == "0":
                pass
            else: return False
        
#No alcance a implementarlo ojala sirva :D


