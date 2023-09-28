# Faça um Programa em Python que Leia uma matriz 10 x 3 com as notas de 10 alunos em 3 provas. Em seguida, escreva o numero de alunos cuja pior nota foi na prova 1, o número de alunos cuja pior nota foi na prova 2, e o numero de alunos cuja pior nota foi na prova 3. Em caso de empate das piores notas de um aluno, o critério de desempate  e arbitrário, mas o aluno deve ser contabilizado apenas uma vez.

def main():
    matriz = []
    for i in range(10):
        matriz.append([int(input("Digite a nota do aluno %d na prova 1: " % i)),
                      int(input("Digite a nota do aluno %d na prova 2: " % i)),
                      int(input("Digite a nota do aluno %d na prova 3: " % i))])

    alunos_prova_1 = 0
    alunos_prova_2 = 0
    alunos_prova_3 = 0

    for aluno in matriz:
        pior_nota = aluno[0]
        if pior_nota > aluno[1]:
            pior_nota = aluno[1]
        if pior_nota > aluno[2]:
            pior_nota = aluno[2]

        if pior_nota == aluno[0]:
            alunos_prova_1 += 1
        elif pior_nota == aluno[1]:
            alunos_prova_2 += 1
        else:
            alunos_prova_3 += 1

    print("O número de alunos cuja pior nota foi na prova 1 é:", alunos_prova_1)
    print("O número de alunos cuja pior nota foi na prova 2 é:", alunos_prova_2)
    print("O número de alunos cuja pior nota foi na prova 3 é:", alunos_prova_3)


if __name__ == "__main__":
    main()
