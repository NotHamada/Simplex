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
    global Inverse_B, Function, B, N, CBT, CNT, Equation, BIndexes, NIndexes
    
    print("\nSelecione as colunas para a base, separados por espaços:")
    print(np.array(Equation))
    indexes = input()
    values = indexes.split()
    BIndexes.extend(int(value)-1 for value in values)
    NIndexes.extend(i for i in range(len(Function)) if i not in BIndexes)
    for index in BIndexes:
        B.append(GetColumn(Equation, index))
        CBT.append(Function[index])
    for index in NIndexes:
        N.append(GetColumn(Equation, index))
        CNT.append(Function[index])
    B = Transpose(B)
    N = Transpose(N)
    print("\nB = ")
    print(np.array(B))

    print("\nN = ")
    print(np.array(N))
    
    if np.linalg.det(B) == 0:
        print("\nA matriz escolhida possui determinante 0!")
        return
    
    Inverse_B = np.linalg.inv(B)

    print("\nInversa de B = ")
    print(Inverse_B)

    print("\nCBT =")
    print(CBT)
    print("\nCNT = ")
    print(CNT)
    
    Step1()

def Step1():
    print("\nPasso 1:")
    global XB
    XB = Inverse_B @ b

    print("\nXB = Inversa de B * b")    
    print("\nXB = {}".format(XB))
    
    Step2()
    

def Step2():
    print("\nPasso 2:")
    global CBT, Inverse_B, N, Enters_Base, CNT
    
    # i)
    λ = CBT @ Inverse_B
    
    print("\nλ = CBT * Inversa de B")
    print("\nλ = {}".format(λ))
    
    # ii)
    CN = []
    counter = 0
    for item in CNT:
        CN.append(item - (λ @ np.transpose(GetColumn(N, counter))))
    
    print("\nĈNK = CNK - λ * an")
    print("\nCNK's = {}".format(CN))
    
    # iii)
    Enters_Base = NIndexes[CN.index(min(CN))]
    print("\nValor mínimo = {}".format(min(CN)))
    
    
    Step3(min(CN)) 

def Step3(min_value):
    print("\nPasso 3:")
    print("\n{} < 0?".format(min_value))
    if min_value >= 0:
        counter = 0
        print("\nSolução final:")
        for index in BIndexes:
            print("x{} = {}".format(index + 1, XB[counter]))
            counter = counter + 1
        for index in NIndexes:
            print("x{} = 0".format(index + 1))
        
        return
    else:
        print("\nNão satisfez a condição, segue o algoritmo")
        Step4()

def Step4():
    print("\nPasso 4:")
    
    y = Inverse_B @ GetColumn(N, Enters_Base)
    print("\ny = Inversa de B * CNK menor")
    print("\ny = ")
    print(y)
    Step5(y)

def Step5(y):
    print("\nPasso 5:")
    print("\nVerificar se os números são menores que zero")
    
    global Quits_Base
    
    has_Solution = False
    for number in y:
        if number > 0:
            has_Solution = True
            break
    
    if has_Solution == False:
        print("O sistema não tem solução!")
        return 
    
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
    
    print("\nÊ = min(XBn/Yn...)")
    print("\nÊ =", E)
    print(values)
    Step6()
            
def Step6():
    print("\nPasso 6:")
    
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
    
    print("\nB =")
    print(B)
    
    print("\nN =")
    print(N)

    print("\nInversa de B =")
    print(Inverse_B)
    
    print("\nCBT = ")
    print(CBT)
    
    print("\nCNT = ")
    print(CNT)
    
    Enters_Base = Quits_Base = 0
        
    Step1()    

print("Insira os itens da função, separados por espaços:")
function = input()
values = function.split()
Function.extend(int(value) for value in values)
print(Function)

print("\nAgora, coloque a matriz das variáveis:")
while True:
    line = input()
    if line == "":
        break

    values = line.split()
    Equation.append([int(value) for value in values])
print(np.array(Equation))

print("\nPor fim, a matriz b dos resultados:")
results = input()
values = results.split()
b.extend(int(value) for value in values)
b = np.transpose(b)
print(b)

DefBase()