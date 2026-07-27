"""
Grid World: 2d world
"""

# Defina o mapa como uma lista de strings.
# Use '#' para célula ocupada (obstáculo) e '.' para célula livre.
mapa_bruto = [
    "#########",
    "#.......#",
    "#..###..#",
    "#..#....#",
    "#..#.##.#",
    "#.......#",
    "#########",
]

TAMANHO_CELULA_METROS = 0.5  # cada célula representa 0.5m x 0.5m no mundo real

# converte 'mapa_bruto' (lista de strings) em uma estrutura mais
# fácil de indexar numericamente: uma lista de listas, onde cada elemento
# é True (ocupado) ou False (livre).
grid = []
for linha in mapa_bruto:
    grid.append([c == '#' for c in linha])


def celula_para_mundo(linha, coluna):
    x = (coluna + 0.5) * TAMANHO_CELULA_METROS
    y = (linha + 0.5) * TAMANHO_CELULA_METROS
    return x, y


def mundo_para_celula(x, y):
    linha = int(y // TAMANHO_CELULA_METROS)
    coluna = int(x // TAMANHO_CELULA_METROS)
    return linha, coluna


def celula_esta_livre(linha, coluna):
    """Devolve True se a célula existe no grid E está livre (não é obstáculo)."""
    if linha < 0 or linha >= len(grid) or coluna < 0 or coluna >= len(grid[0]):
        return False
    return not grid[linha][coluna]


# --- Testes -- não mexer, só rodar depois de preencher os TODOs acima ---
print("Grid carregado:", len(grid), "linhas x", len(grid[0]), "colunas")
print("Célula (1,1) livre?", celula_esta_livre(1, 1))   # deveria ser True
print("Célula (0,0) livre?", celula_esta_livre(0, 0))   # deveria ser False (é '#')
print("Célula (100,100) livre?", celula_esta_livre(100, 100))  # fora do grid

x, y = celula_para_mundo(1, 1)
print(f"Centro da célula (1,1) em metros: ({x}, {y})")

linha, coluna = mundo_para_celula(x, y)
print(f"Convertendo de volta: ({x}, {y}) -> célula ({linha}, {coluna})")