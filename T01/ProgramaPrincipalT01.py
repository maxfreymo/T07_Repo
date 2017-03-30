import User
import Calendar
import ClaseANAF
import ClaseOperario
import Resources
import sys

Resources.Recurso().leer_recursos("NO")

print("¡Bienvenido al programa SuperLuchin!")
print()
User.Usuario().ingreso_usuario()
        

"""print("Ha continuacion establezca fecha y hora")
print()
Calendar.Calendario().setear_fecha()
Calendar.Calendario().setear_reloj()"""

while True:
    if User.usuarioActual[3] == "":
        ClaseANAF.ANAF().menu_anaf()
    else:
        ClaseOperario.Operario(User.usuarioActual[3]).menu_operario()
        
print("Finish")


        

