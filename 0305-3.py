# como fazer para contar a quantidade de numeros pares entre dois numeros aleatorios
a = int(input('digite o valor de a: '))
b = int(input('digite o valor de b: '))
par = 0
while a <= b or a >= b:
    if a%2 == 0:
        par += 1
    a +=1
print(f'temos {par} numeros pares')