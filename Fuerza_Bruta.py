from string import ascii_letters , digits
from itertools import product

#Concatenar letras y digitos en una sola cadena
caracteres = ascii_letters+digits

def buscador(con):

    #Archivo con todas las combinaciones generales
    archivo = open("combinaciones.txt","w")

    if 3<= len(con)<=4:
        for i in range(3,5):
            for comb in product(caracteres, repeat=i):
                #Se utiliza join()  para concatenar los caracteres regresando por la función product().
                #Como join necesita una cadena inicial para hacer la concatenación, se pone una cadena vacía
                #al principio
                prueba = "".join(comb)
                #Escribiendo al archivo cada combinación generada
                archivo.write( prueba + "\n" )
                if prueba == con:
                    print('Tu contraseña es {}'.format(prueba))
                    #Cerrando el archivo
                    archivo.close()
                    break
                else:
                    print('Ingresa una contraseña que contenga de 3 a 4 caracteres')
from time import time
t0 = time()
con ='H0L4'
buscador(con)
print("Tiempos de ejecución {}".format(round(time()-t0,6)))

    
