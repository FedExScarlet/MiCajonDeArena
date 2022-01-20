#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      FedEx
#
# Created:     04/01/2022
# Copyright:   (c) FedEx 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def calendario():
    day=int(input('Indicar el primer día del mes, siendo 0 Lunes y 6 Domingo: '))
    target=int(input('Introducir el número de día que se desea conocer: '))
    x=day+target-1      # -1 debido a que la diferencia puede ser 0, pero al ser el 1° (por ejemplo) ya da 1, y devuelve un dia más
    while x > 6:
        x=x-7
    if x==0:
      print('Cae Lunes')
    elif x==1:
     print('Cae Martes')
    elif x==2:
     print('Cae Miércoles')
    elif x==3:
      print('Cae Jueves')
    elif x==4:
      print('Cae Viernes')
    elif x==5:
      print ('Cae Sábado')
    elif x==6:
       print('Cae Domingo')