from Abstract.abstract import Expression
from math import *

class Trigonometricas(Expression):
    
    def __init__(self, left, tipo, fila, columna):
        
        self.left = left
        self.tipo = tipo
        self.valor = 0
        
        super().__init__(fila, columna)
    
    def operar(self, arbol):
        
        leftValue = ''
        if self.left != None:
            leftValue = self.left.operar(arbol)
        
        
        if self.tipo.operar(arbol) == 'Seno':
            resultado = sin(leftValue)
            self.valor = resultado
            return resultado
        
        
        elif self.tipo.operar(arbol) == 'Coseno':
            resultado = cos(leftValue)
            self.valor = resultado
            return resultado
            
            
            
        elif self.tipo.operar(arbol) == 'Tangente':
            resultado = tan(leftValue)
            self.valor = resultado
            return resultado            
        
        
        else:
            return None
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()
    
    