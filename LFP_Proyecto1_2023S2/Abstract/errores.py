from Abstract.abstract import Expression

class Errores(Expression):
    def __init__(self, error, fila, columna):
        self.error = error
        super().__init__(fila, columna)

    def operar(self, arbol):
        return self.error

    def getColumna(self):
        return super().getColumna()
    
    def getFila(self):
        return super().getFila()