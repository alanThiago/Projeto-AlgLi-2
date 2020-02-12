from funcoes import *
from tkinter import *

def determinante():
    A = array(eval(edMatriz.get()))
    d = linalg.det(A)
    saida ['text'] = str(round(d, 2))

def traco1():
    A = array(eval(edMatriz.get()))
    n = len(A)
    saida ['text'] = traco(A, n)

def transposta1():
    A = array(eval(edMatriz.get()))
    n = len(A)
    transposta(A, n)
    saida ['text'] = matToString(A, n)

def inversa():
    A = array(eval(edMatriz.get()))
    if linalg.det(A):
        A = linalg.inv(A)
        n = len(A)
        saida ['text'] = matToString(A, n)
    else:
        saida ['text'] = 'Não admite inversa'

def polinomioCaracteristico():
    A = array(eval(edMatriz.get()))
    n = len(A)
    p = leverrierFaddeev(A, n)[0]
    
    polinomio = '1.0λ**' + str(n) + '   '
    exp = n-1
    for i in range(1, n):
        if p[i] > -1:
            polinomio += '+' + str(p[i]) + 'λ**' + str(exp) + '   '
        else:
            polinomio += str(p[i]) + 'λ**' + str(exp) + '   '
        exp -= 1
    if p[n] > -1:
        polinomio += '+' + str(p[n])
    else:
        polinomio += str(p[n])

    saida ['text'] = polinomio

def autovalores():
    A = array(eval(edMatriz.get()))
    n = len(A)
    av = metodoFrancis(A, n)
    valores = ''
    for i in range(n):
        valores += 'λ' + str(i+1) + ' = ' + str(round(av[i], 2)) + '\n'
    saida ['text'] = valores

def autovetores1():
    A = array(eval(edMatriz.get()))
    n = len(A)
    av = autovetores(A, n)
    lv = ''
    for i in range(n):
        lv += 'λ' + ' = ' + str(round(av[i][0], 2)) + ':    ('
        for j in range(n-1):
            lv += str(round(av[i][1][j], 2)) + ', '
        lv += str(round(av[i][1][n-1],2)) + ')\n'

    saida ['text'] = lv

def matrizDiagonal1():
    A = array(eval(edMatriz.get()))
    n = len(A)
    A = matrizDiagonal(A, n)
    saida ['text'] = matToString(A, n)

janela = Tk()
janela["bg"] = "black"
janela.title("Reprovacao em Algebra")

janela.geometry("1200x800")

lb2 = Label(janela, text="Campo de entrada", font="Times 20 bold", width=48, bg="white", fg="grey")
lb2.grid(row = 0, column = 0)

lbaux = Label(janela, text="Coloque as linhas e colunas da seguinte forma:", font="Times 20 bold ", bg = "black", fg="white")
lbaux.place(x=35,y=100)

edMatriz = Entry(janela, width = 30)
edMatriz.insert(INSERT, "[[0,0,0],"
                  "[0,0,0],"
                  "[0,0,0]]")
edMatriz.place(x=190,y=190)

lbaux2 = Label(janela, text="Selecione a funcao:", font="Times 20 bold", bg = "black", fg="white")
lbaux2.place(x=200,y=270)

bt = Button(janela,width=20,text="Determinante", relief=GROOVE, font=" Times 12", bg = "grey", activebackground="red", fg="white", command = determinante)
bt.place(x=100,y=330)

bt2 = Button(janela,width=20,text="Traco", relief=GROOVE, font=" Times 12", bg = "grey", activebackground="red", fg="white", command=traco1)
bt2.place(x=100,y=380)

bt3 = Button(janela,width=20,text="Transposta", relief=GROOVE, font=" Times 12", bg = "grey", activebackground="red", fg="white", command=transposta1)
bt3.place(x=100,y=430)

bt4 = Button(janela,width=20,text="Inversa", relief=GROOVE, font=" Times 12", bg = "grey", activebackground="red", fg="white", command=inversa)
bt4.place(x=100,y=480)

bt5 = Button(janela,width=20,text="Polinomio Caracteristico", relief=GROOVE, font=" Times 12", bg = "grey", activebackground="red", fg="white", command=polinomioCaracteristico)
bt5.place(x=340,y=330)

bt6 = Button(janela,width=20,text="Autovalores", relief=GROOVE, font=" Times 12", bg = "grey", activebackground="red", fg="white", command=autovalores)
bt6.place(x=340,y=380)

bt7 = Button(janela,width=20,text="Autovetores", relief=GROOVE, font=" Times 12", bg = "grey", activebackground="red", fg="white", command=autovetores1)
bt7.place(x=340,y=430)

bt8 = Button(janela,width=20,text="Matriz Diagonal", relief=GROOVE, font=" Times 12", bg = "grey", activebackground="red", fg="white", command=matrizDiagonal1)
bt8.place(x=340,y=480)


#outro lado

lb2_0 = Label(janela, width=65, bg="black")
lb2_0.grid(row = 0, column = 2)

lbaux13 = Label(janela, font="arial 1 ", bg = "black")
lbaux13.grid(row = 1, column = 2)

saida = Label(font="Times 20 bold", width=100, bg = "black", fg="white")
saida.grid(row=2, column = 2)

janela.maxsize(width=1520, height=800)
janela.mainloop()