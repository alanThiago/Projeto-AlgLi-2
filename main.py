from funcoes import *

print("++++++++++++++++++++++++++++++++++++++++++++")
print("        TRABALHO DE ÁLGEBRA LINEAR II       ")
print("++++++++++++++++++++++++++++++++++++++++++++")

n = int(input("Insira a dimensão da matriz: "))

print("Entre com os dados da matriz:")
A = receberMatriz(n)

print("[1] Determinante")
print("[2] Transposta")
print("[3] Traço")
print("[4] Inversa")
print("[5] Polinômio Característico")
print("[6] Autovalores")
print("[7] Autovetores")
print("[8] Matriz Diagonal")
funcao = int(input("Selecione uma das funções acima: "))

if funcao == 1:
    print(pivoteamentoParcialDeGauss(A, n, n))
elif funcao == 2:
    transposta(A, n)
    print(A)
elif funcao == 3:
    print(traco(A, n))
elif funcao == 4:
    print(linalg.inv(A))
elif funcao == 5:
    print(leverrierFaddeev(A, n)[0])
elif funcao == 6:
    print(metodoFrancis(A, n))
elif funcao == 7:
    print(autovetores(A, n))
elif funcao == 8:
    print(matrizDiagonal(A, n))
else:
    print("Opção inválida")
