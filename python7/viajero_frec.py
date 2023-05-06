class Viajero:
    __numViajero= " "
    __dni= " "
    __nombre= " "
    __apellido= " "
    __millasAcum: int
    def __init__(self, numViajero, dni, nombre, apellido, millasAcum): #)constructor
     self.__numViajero = numViajero
     self.__dni = dni
     self.__nombre= nombre
     self.__apellido= apellido
     self.__millasAcum= millasAcum
     
    def getMillas(self):
      return self.__millasAcum
       
    def canjearMillas__sub__(self, millasACanjear):
        if millasACanjear <= self.__millasAcum :
          self.__millasAcum = self.__millasAcum - millasACanjear
          return self.__millasAcum
        else:
         print(f'No tienes suficientes millas! elige un monto menor!')

    def __gt__(self, other):
      return self.__millasAcum > other.__millasAcum
    
    def mayorCantMillas_gt_(self,m): 
      if self.__millasAcum > m: #comprara con un viajero none
        m= self.__millasAcum
      return self.__nombre 
    
    def acumMillas__ad__(self, v):
        v=self.__millasAcum +v
        return v
    
    def compararMillas__eq__(self):
      if self.__millasAcum == 400:
        print('Las millas acumuladas de  son igual a 400.')
      else:
        print('Las millas no son igual a 400.')  