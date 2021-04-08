import mathOps

print("HOLA")
x = 5
y = 10

print(mathOps.sum(x,y))

#agregando resto de calculos al programa

number1 = float(input("ingresar primer numero: "))
operation = input("ingresar operacion: ")
number2 = float(input("ingresar segundo numero: "))

status, result = mathOps.calculate(number1,number2,operation)

if status:
    print(f"{number1} {operation} {number2} = {result}")