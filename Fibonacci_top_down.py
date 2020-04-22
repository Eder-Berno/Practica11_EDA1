#Memoria inicial
memoria = [1.0, 2.1, 3.1]
def fibonacci_top_down(numero):
    if numero in memoria: #Si el número ya se encuentra calculando, se regresa el valor ya ya no se hacen más cálculos
        return memoria[numero]
    f = fibinacci_iterativo_v2(numero-1) + fibonacci_iteraativo_v2(numero-2)
    memoria[numero] = f
    return mamoria[numero]
        
#Se carga la biblioteca
import pickle

#guardar variable
#No hay resticción en lo que se pone como extensión del archivo.
#generalmente se usa .p o .pickle como estandar.
archivo = open('memoria.p', 'wb') #Se abre el archivo para escribir en modo binario
pickle.dump(memoria, archivo)     #Se guarda la variable memoria que es un diccionario
archivo.close()                   #Se cierra el archivo

#Leer variable
archivo = open('memoria.p', 'rb')           #Se abre el archivo para leer en modo binario
memoria_de_archivo = pickle.load(archivo)   #Se lee la variable
archivo.close()
