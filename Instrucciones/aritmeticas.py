from Abstract.abstract import Expression


class Aritmetica(Expression):

    def __init__(self, left, right, tipo, fila, columna):
        
        self.left = left
        self.right = right
        self.tipo = tipo
        self.valor = 0
        
        super().__init__(fila, columna)
        
    def operar(self, arbol):
        leftValue    = ''
        rightValue   = ''
        
        
        if self.left != None:
            leftValue  = self.left.operar(arbol)
            rightValue = self.right.operar(arbol)
        elif self.right != None:
            rightValue = self.right.operar(arbol)


        if self.tipo.operar(arbol) == 'Suma':
            resultado = leftValue + rightValue
            self.valor = resultado
            return resultado
        
        elif self.tipo.operar(arbol) == 'Resta':
            resultado = leftValue - rightValue
            self.valor = resultado
            return resultado

        elif self.tipo.operar(arbol) == 'Multiplicacion':
            resultado = leftValue * rightValue
            self.valor = resultado
            return resultado
            
        elif self.tipo.operar(arbol) == 'Division':
            resultado = leftValue / rightValue
            self.valor = resultado
            return resultado

        elif self.tipo.operar(arbol) == 'Potencia':
            resultado = leftValue ** rightValue
            self.valor = resultado
            return resultado
            
        elif self.tipo.operar(arbol) == 'Modulo':
            resultado = leftValue % rightValue
            self.valor = resultado
            return resultado
            
        elif self.tipo.operar(arbol) == 'Raiz':
            resultado = leftValue ** (1/rightValue)
            self.valor = resultado
            return resultado
            
        elif self.tipo.operar(arbol) == 'Inverso':
            resultado = 1/leftValue
            self.valor = resultado
            return resultado
        
        else:
            return None
    
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()
    
    

