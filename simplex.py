import numpy as np

Function = []
Equation = []
B = []
Inverse_B = []
N = []
b = []
CBT = []
CNT = []
BIndexes = []
NIndexes = []
XB = []
Enters_Base = 0
Quits_Base = 0

def GetColumn(matrix, i):
    return [row[i] for row in matrix]

def Transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def DefBase():
    global Inverse_B, Function, B, N, CBT, CNT
    
    print("Selecione as colunas para a base, separados por espaços:")
    matrix = np.array(Equation)
    print(matrix)
    indexes = input()
    values = indexes.split()
    BIndexes.extend(int(value)-1 for value in values)
    NIndexes.extend(i for i in range(len(Function)) if i not in BIndexes)
    matrix_B = []
    matrix_N = []
    for index in BIndexes:
        matrix_B.append(GetColumn(Equation, index))
        CBT.append(Function[index])
    for index in NIndexes:
        matrix_N.append(GetColumn(Equation, index))
        CNT.append(Function[index])
    B = Transpose(matrix_B)
    N = Transpose(matrix_N)
    print("B = ")
    print(np.array(B))

    print("N = ")
    print(np.array(N))
    Inverse_B = np.linalg.inv(B)

    print("Inversa de B = ")
    print(Inverse_B)

    print("CBT =")
    print(CBT)
    print("CNT = ")
    print(CNT)
    
    Step1()

def Step1():
    global XB
    XB = Inverse_B @ b
    
    print("XB = ")
    print(XB)
    
    Step2()
    

def Step2():
    global CBT, Inverse_B, N, Enters_Base, CNT
    
    # i)
    λ = CBT @ Inverse_B
    
    print("λ =")
    print(λ)
    
    # ii)
    CN = []
    counter = 0
    for item in CNT:
        CN.append(item - (λ @ np.transpose(GetColumn(N, counter))))
    
    print("CNK's = ")
    print(CN)
    
    # iii)
    Enters_Base = NIndexes[CN.index(min(CN))]
    Step3(min(CN)) 

def Step3(min_value):
    if min_value >= 0:
        print(XB)
        return
    else:
        Step4()

def Step4():
    y = Inverse_B @ GetColumn(N, Enters_Base)
    print("y = ")
    print(y)
    Step5(y)

def Step5(y):
    global Quits_Base
    
    has_Solution = False
    for number in y:
        if number > 0:
            has_Solution = True
            break
    
    if has_Solution == False:
        return ArithmeticError
    
    values = []
    counter = 0
    
    for item in y:
        if item <= 0:
            values.append(float('inf'))
        else:
            values.append(XB[counter]/ item)
            counter = counter + 1
    
    E = min(values)
    
    Quits_Base = values.index(E)
    
    print("E = ", E)
    print(values)
    Step6()
            
def Step6():
    global B, N, CBT, CNT, Inverse_B, Enters_Base, Quits_Base, BIndexes, NIndexes
    
    transpose_B = Transpose(B)
    transpose_N = Transpose(N)
    
    quit_Base = transpose_B[Quits_Base]
    enter_Base = transpose_N[Enters_Base]
    
    transpose_B[Quits_Base] = enter_Base
    transpose_N[Enters_Base] = quit_Base
        
    B = Transpose(transpose_B)
    N = Transpose(transpose_N)
    
    quit_Index = BIndexes[Quits_Base]
    enter_Index = NIndexes[Enters_Base]
    BIndexes[Quits_Base] = enter_Index
    NIndexes[Enters_Base] = quit_Index
    

    cbt_Index = CBT[Quits_Base]
    cnt_Index = CNT[Enters_Base]
    CBT[Quits_Base] = cnt_Index
    CNT[Enters_Base] = cbt_Index
    
    
    Inverse_B = np.linalg.inv(B)
    print(Inverse_B)
    
    Enters_Base = Quits_Base = 0
        
    Step1()    

print("Insira os itens da função, separados por espaços:")
function = input()
values = function.split()
Function.extend(int(value) for value in values)
print(Function)

print("Agora, coloque a matriz das variáveis:")
while True:
    line = input()
    if line == "":
        break

    values = line.split()
    Equation.append([int(value) for value in values])
print(np.array(Equation))

print("Por fim, a matriz b dos resultados:")
results = input()
values = results.split()
b.extend(int(value) for value in values)
b = np.transpose(b)
print(b)

DefBase()