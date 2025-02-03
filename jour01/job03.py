class Operation :
    def __init__(self, nombre1=15, nombre2=5):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        result = self.nombre1 + self.nombre2
        return result

operation = Operation()
print(operation.addition())