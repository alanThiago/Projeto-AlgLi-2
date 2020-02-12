from numpy import *

def receberMatriz(n):
    matriz = []

    for i in range(n):
        linha = input()
        linha = linha.split(" ")
        linha = [float(i) for i in linha]
        matriz.append(linha)

    return array(matriz)

def matToString(A, n):
    m = ''
    for i in range(n):
        for j in range(n):
            m += str(round(A[i][j], 2)) + '   '
        m += '\n'
    return m

def traco(A, n):
    t = 0.0
    for i in range(n):
        t += A[i][i]
    return t

def transposta(A, n):
    for i in range(n):
        for j in range(i+1, n):
            A[i][j], A[j][i] = A[j][i], A[i][j]

def pivoteamentoParcialDeGauss(A, l, c):
    det = 1
    for k in range(l-1):
        m = abs(A[k][k])
        ml = k
        for i in range(k+1, l):
            if m < abs(A[i][k]):
                m = abs(A[i][k])
                ml = i

        if ml != k:
            det *= (-1)
            for i in range(k, c):
                aux = A[ml][i]
                A[ml][i] = A[k][i]
                A[k][i] = aux

        if A[k][k] == 0:
            return 0
        else:
            for i in range(k+1, l):
                F = A[i][k]/A[k][k]
                A[i][k] = 0
                for j in range(k+1, c):
                    A[i][j] -= A[k][j]*F
    for x in range(l):
        det *= A[x][x]
    return det

def F_mais_tr(F, n, p):
    for i in range(n):
        F[i][i] += p

def leverrierFaddeev(A, n):
    F = array(A)
    polinomio = [1]
    matrizes = []
    for k in range(1, n+1):
        polinomio.append(-traco(F, n)/k)
        F_mais_tr(F, n, polinomio[k])
        matrizes.append(array(F.T))
        F = dot(A, F)
    return (polinomio, array(matrizes))

def precisaoTriangular(A, n):
    for i in range(1, n):
        for j in range(i):
            if abs(A[i][j]) > 0.0001:
                return 1
    return 0

def senCos(A, i, j):
    s = A[i][j] / ((A[0][0]**2 + A[i][j]**2)**(1/2))
    c = A[0][0] / ((A[0][0]**2 + A[i][j]**2)**(1/2))
    return (s, c)

def gerarU(A, n, i, j):
    U = identity(n)
    sc = senCos(A, i, j)
    U[i][i] = sc[1]
    U[j][j] = sc[1]
    U[i][j] = -sc[0]
    U[j][i] = sc[0]
    return U

def metodoFrancis(A, n):
    cont = 0
    while precisaoTriangular(A, n) and cont < 1000:
        Q = identity(n)
        for j in range(n-1):
            for i in range(j+1, n):
                if A[i][j] != 0:
                    U = gerarU(A, n, i, j)
                    Q = dot(U, Q)
                    A = dot(U, A)
        transposta(Q, n)
        A = dot(A, Q)
        cont += 1

    return [A[i][i] for i in range(n)]

def naoNulo(v, n):
    for i in range(n):
        if v[i] != 0:
            return 1
    return 0

def autovetores(A, n):
    matrizes = leverrierFaddeev(A, n)[1]
    autovalores = linalg.eig(A)[0]
    autovetores = zeros((n,n))
    I = identity(n)
    cont = 0
    linha = 0

    while cont < n and linha < n:
        v = array(I[linha])
        for i in range(n-1):
            v = autovalores[cont]*v + matrizes[i][linha]
        if naoNulo(v, n):
            autovetores[cont] = v
            cont += 1
        else:
            linha += 1
            cont = 0
    
    eigenvectors = []
    for i in range(n):
        eigenvectors.append((autovalores[i], autovetores[i]))
    return eigenvectors

def matrizDiagonal(A, n):
    matriz = zeros((n, n))
    autovalores = linalg.eig(A)[0]
    for i in range(n):
        matriz[i][i] = autovalores[i]
    return matriz