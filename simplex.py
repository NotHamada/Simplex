import numpy as np

Function = []
B = []
b = []

def Step1():
    print()

def Step2():
    print()

def Step3():
    print()

def Step4():
    print()

def Step5():
    print()

def Step6():
    print()

print("Insira os itens da função, separados por espaços:")
function = input()
values = function.split()
Function.extend(int(value) for value in values)

print("Agora, coloque a matriz das variáveis:")
while True:
    line = input()
    if line == "":
        break

    values = line.split()
    B.append([int(value) for value in values])

print("Por fim, a matriz b dos resultados:")
results = input()
values = results.split()
b.extend(int(value) for value in values)
print(b)
b = np.array(b).T

print(B)
print(np.linalg.inv(B))

print(Function)
