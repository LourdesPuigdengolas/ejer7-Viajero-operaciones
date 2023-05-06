from viajero_frec import Viajero
import csv

if __name__=='__main__':
       
        DatosViajeros= []  #inicializar lista vacia
        with open("datos_de_viajeros.csv") as archivo:
                reader = csv.reader(archivo, delimiter=',')
                for fila in reader:
                        unViajero= Viajero(fila[0], fila[1], fila[2], fila[3], int(fila[4]))
                        DatosViajeros.append(unViajero)
   
        print(f"--- MENU: ---")
        print(f"[1]. Comparar las cantidad de millas. ")
        print(f"[2]. Acumluar millas")
        print(f"[3]. Canjear millas")
        print(f"[0]. Salir")
        opcion= int(input("Ingrese el numero de opción que desea: "))
        
        while opcion != 0: 
                if opcion == 1:
                        for i in range(len(DatosViajeros)):               
                           Viajero.compararMillas__eq__(DatosViajeros[i])      
                                        
                elif opcion == 2: 
                        for i in range(len(DatosViajeros)):
                                v:int=100
                                r=DatosViajeros[i].acumMillas__ad__(v)
                                print(f' Las millas acumuladas son: {r}')  #retorno al main para poder mostrar el de todos gracias a la iteracion
                              
                elif opcion ==3:
                        for i in range(len(DatosViajeros)):
                                millasACanjear= int(input('Ingrese la cantidad de millas que desea canjear: '))
                                c=DatosViajeros[i].canjearMillas__sub__(millasACanjear)
                                print(f' Las millas restantes del viejro numero {i+1} son: {c}')  #con {i+1} voy mostrando los numeros de viajeros ;)
                                                                     
                opcion= int(input("Ingrese el numero de opción que desea: "))
