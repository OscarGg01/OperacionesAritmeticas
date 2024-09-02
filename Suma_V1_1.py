def ingreseNumeros():
    numero01 = float(input("ingrese sumando uno: "))
    numero02 = float(input("ingrese sumando dos: "))
    return numero01,numero02
def suma(numero01,numero02):
    return numero01 + numero02

if __name__ = '__main__':
    num1, num2 = ingreseNumeros()
    print(f"{num1}+{num2} = {suma(num1, num2)}")