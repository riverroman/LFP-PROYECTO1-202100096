from Instrucciones.aritmeticas import Aritmetica
from Instrucciones.trigonometricas import Trigonometricas
from Abstract.lexema import *
from Abstract.numero import *
from Errores.errores import *


class Analizador:
    
    def __init__(self):
        
        
        reserved = {
            
            'ROPERACION'        :   'Operacion',
            'RVALOR1'           :   'Valor1',
            'RVALOR2'           :   'Valor2',
            'RSUMA'             :   'Suma',
            'RRESTA'            :   'Resta',
            'RMULTIPLICACION'   :   'Multiplicacion',
            'RDIVISION'         :   'Division',
            'RPOTENCIA'         :   'Potencia',
            'RRAIZ'             :   'Raiz',
            'RINVERSO'          :   'Inverso',
            'RSENO'             :   'Seno',
            'RCOSENO'           :   'Coseno',
            'RTANGENTE'         :   'Tangente',
            'RMODULO'           :   'Modulo',
            'RTEXTO'            :   'Texto',
            'RCOLORFONDONODO'   :   'Color-Fondo-Nodo',
            'RCOLORFUENTENODO'  :   'Color-Fuente-Nodo',
            'RFORMADNODO'       :   'Forma-Nodo',
            'COMA'              :   ',',
            'PUNTO'             :   '.',
            'DPUNTOS'           :   ':',
            'CORI'              :   '[',
            'CORD'              :   ']',
            'LLAVEI'            :   '{',
            'LLAVED'            :   '}'
            
        }


        lexemas = list(reserved.values())

        global n_linea
        global n_columna
        global instrucciones
        global lista_lexemas
        global lista_errores
        
        n_linea = 1
        n_columna = 1
        lista_lexemas = []
        instrucciones = []
        lista_errores = []

    def instruccion(self,cadena):
    
        global n_linea
        global n_columna
        global lista_lexemas
        lexema = ''
        puntero = 0
        
        while cadena:
            
            char = cadena[puntero]
            puntero += 1
            
            if char == '\"':
                lexema, cadena = self.armar_lexema(cadena[puntero:])
                if lexema and cadena:
                    n_columna += 1
                    
                    l = Lexema(lexema, n_linea, n_columna)
                    
                    lista_lexemas.append(l)
                    n_columna += len(lexema) + 1
                    puntero = 0
                    
            elif char.isdigit():
                
                token, cadena = self.armar_numero(cadena)        
                if token and cadena:
                    n_columna += 1
                    
                    n = Numero(token, n_linea, n_columna)
                    
                    lista_lexemas.append(n)
                    n_columna += len(str(token)) + 1
                    puntero = 0
                    
            elif char == '[' or char == ']':
                
                    c = Lexema(char, n_linea, n_columna)
                
                    lista_lexemas.append(c)
                    cadena = cadena[1:]
                    puntero = 0
                    n_columna += 1
            
            elif char == '\t':
                n_columna += 4
                cadena = cadena[4:]
                puntero = 0
                
            elif char == '\n':
                cadena = cadena[1:]
                puntero = 0
                n_linea += 1
                n_columna = 1
            
            elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == '.' or char == ':':
                n_columna += 1
                cadena = cadena[1:]
                puntero = 0 
                
            else:
                lista_errores.append(Errores(char,n_linea,n_columna))
                cadena = cadena[1:]
                puntero = 0
                n_columna += 1
                
                
        return lista_lexemas
        
    def armar_lexema(self,cadena):
        
        global n_linea
        global n_columna
        global lista_lexemas
        lexema = ''
        puntero = ''
        
        for char in cadena:
            puntero += char
            if char == '\"':
                return lexema, cadena[len(puntero):]
            else:
                lexema += char
            
        return None, None

    def armar_numero(self,cadena):
        
        numero = ''
        puntero = ''
        is_decimal = False
        for char in cadena:
            puntero += char
            if char == '.':
                is_decimal = True
            if char == '"' or char  == ' ' or char == '\n' or char == ']' or char == '\t':
                if is_decimal:
                    return float(numero), cadena[len(puntero)-1:]
                else:
                    return int(numero), cadena[len(puntero)-1:]
            else:
                numero += char
                
        return None, None
        
    def operar(self):
        
        global lista_lexemas
        global instrucciones
        operacion = ''
        n1 = ''
        n2 = ''
        
        while lista_lexemas:
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == 'Operacion':
                operacion = lista_lexemas.pop(0)
            elif lexema.operar(None) == 'Valor1':
                n1 = lista_lexemas.pop(0)
                
                if n1.operar(None) == '[':
                    n1 = self.operar()
                    
            elif lexema.operar(None) == 'Valor2':
                n2 = lista_lexemas.pop(0)
                if n2.operar(None) == '[':
                    n2 = self.operar()
                
            if operacion and n1 and n2:
                return Aritmetica(n1,n2,operacion, f'Inicio:{operacion.getFila()}:{operacion.getColumna()}', f'Fin:{n2.getFila()}:{n2.getColumna()}')
            
            
            elif operacion and n1 and operacion.operar(None) == ('Seno'):
            
                return Trigonometricas(n1, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
        
            elif operacion and n1 and operacion.operar(None) == ('Coseno'):
            
                return Trigonometricas(n1, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
        
            elif operacion and n1 and operacion.operar(None) == ('Tangente'):
            
                return Trigonometricas(n1, operacion, f'Inicio: {operacion.getFila()}:{operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')
            
        return None

    def operar_(self):
        
        instrucciones = []
        while True:
            operacion = self.operar()
            if operacion:
                instrucciones.append(operacion)
            else:
                break
            
        return instrucciones
    
    def getErrores(self):
        lista_errores
        return lista_errores
    
    def entrada1(self,entrada):
        self.instruccion(entrada)
    
        
    def grafica(self,indice,id,etiqueta,objeto):
    
        dot = 'graph [bgcolor="#B7F0F0";\n label="RESULTADOS - 202100096";\n fontname="Arial Black";\n fontsize=20];\n'
        
        if objeto:
            
            if type(objeto) == Numero:
                
                resultado = objeto.operar(None) 
                dot += f'nodo_{indice}_{id}{etiqueta}[label="{resultado}", style=filled, fillcolor="#D7AEFA", color="black"];\n'
                
            if type(objeto) == Trigonometricas:
    
                dot += f'nodo_{indice}_{id}{etiqueta}[label ="{objeto.tipo.lexema}\\n{objeto.valor}", style=filled, fillcolor="#FEC54B", color="black"];\n'
                dot += self.grafica(indice,id + 1,etiqueta + "_ag",objeto.left)
                dot += f'nodo_{indice}_{id}{etiqueta} -> nodo_{indice}_{id+1}{etiqueta}_ag [color="red"];\n'
                
            if type(objeto) == Aritmetica:
                
                dot += f'nodo_{indice}_{id}{etiqueta}[label ="{objeto.tipo.lexema}\\n{objeto.valor}",style=filled, fillcolor="#FEC54B", color="black"];\n'
                dot += self.grafica(indice, id+1, etiqueta + "_iz",objeto.left)
                dot +=  f'nodo_{indice}_{id}{etiqueta} -> nodo_{indice}_{id+1}{etiqueta}_iz [color="red"];\n'
                dot += self.grafica(indice, id+1, etiqueta + "_de",objeto.right)
                dot +=  f'nodo_{indice}_{id}{etiqueta} -> nodo_{indice}_{id+1}{etiqueta}_de [color="red"];\n'
                
        return dot

