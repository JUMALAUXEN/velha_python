def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(s == jogador for s in linha):
            return True
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def verificar_empate(tabuleiro):
    return all(tabuleiro[linha][col] != " " for linha in range(3) for col in range(3))

def obter_jogada():
    while True:
        try:
            jogada = int(input("Escolha um espaço (1-9): "))
            if jogada < 1 or jogada > 9:
                raise ValueError
            return jogada
        except ValueError:
            print("Entrada inválida. Por favor, escolha um número entre 1 e 9.")

def converter_jogada(jogada):
    return (jogada - 1) // 3, (jogada - 1) % 3

def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    jogador_atual = 0

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogadores[jogador_atual]}")

        jogada = obter_jogada()
        linha, col = converter_jogada(jogada)

        if tabuleiro[linha][col] != " ":
            print("Espaço já ocupado! Tente novamente.")
            continue

        tabuleiro[linha][col] = jogadores[jogador_atual]

        if verificar_vitoria(tabuleiro, jogadores[jogador_atual]):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogadores[jogador_atual]} venceu!")
            break

        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = 1 - jogador_atual

if __name__ == "__main__":
    jogar()
