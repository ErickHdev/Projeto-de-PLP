import random
def gerar_cartela():
    """Gera uma cartela de bingo com 25 números aleatórios."""
    cartela = []
    while len(cartela) < 25:
        numero = random.randint(0, 99)
        if numero not in cartela:
            cartela.append(numero)
    return cartela
# Função para exibir a cartela de bingo
def exibir_cartela(cartela):
    """Exibe a cartela de bingo na tela."""
    for i in range(5):
        for j in range(5):
            index = i * 5 + j
            print(f'{cartela[index]:2}', end='  ')
        print()
# Função principal
def main():
    """Gera e exibe as cartelas de bingo."""
    num_cartelas = int(input("Quantas cartelas você deseja gerar? "))
    for i in range(num_cartelas):
        cartela = gerar_cartela()
        print(f'\nCartela {i + 1}:\n')
        exibir_cartela(cartela)
# Verifica se o programa está sendo executado como um script
if __name__ == "__main__":
    main()