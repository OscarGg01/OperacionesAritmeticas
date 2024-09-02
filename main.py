from OperacionesAritmeticas import OperacionesAritmeticas

if __name__ == '__main__':
    operación = OperacionesAritmeticas()
    num1, num2 = operación.ingreseNumeros()
    print(f"{num1} + {num2} = {operación.suma(num1, num2)}")