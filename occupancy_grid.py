"""
Occupancy Grid: representação probabilística do mapa, atualizada em
log-odds a partir de leituras simuladas de LiDAR (reaproveitando o
ray casting já implementado).
"""

import math
from grid import TAMANHO_CELULA_METROS
from grid import celula_esta_livre
from grid import grid

EVIDENCIA_OCUPADO = 0.85
EVIDENCIA_LIVRE = -0.4


def lancar_raio_com_caminho(pos_x, pos_y, angulo_radianos, distancia_maxima_celulas=50):
    """
    Mesma lógica de lancar_raio, mas retornando também TODAS as células
    livres atravessadas pelo caminho, e a célula de obstáculo (se houver).
    Retorna: (celulas_livres, celula_obstaculo_ou_None)
    celulas_livres é uma lista de tuplas (linha, coluna).
    """
    dx = math.cos(angulo_radianos)
    dy = math.sin(angulo_radianos)

    passo_unitario_x = float('inf') if dx == 0 else abs(1 / dx)
    passo_unitario_y = float('inf') if dy == 0 else abs(1 / dy)

    celula_x = int(pos_x)
    celula_y = int(pos_y)

    if dx < 0:
        step_x = -1
        comprimento_x = (pos_x - celula_x) * passo_unitario_x
    else:
        step_x = 1
        comprimento_x = (celula_x + 1 - pos_x) * passo_unitario_x

    if dy < 0:
        step_y = -1
        comprimento_y = (pos_y - celula_y) * passo_unitario_y
    else:
        step_y = 1
        comprimento_y = (celula_y + 1 - pos_y) * passo_unitario_y

    celulas_livres = []
    celula_obstaculo = None
    encontrou_obstaculo = False
    distancia = 0.0

    while not encontrou_obstaculo and distancia < distancia_maxima_celulas:
        if comprimento_x < comprimento_y:
            celula_x += step_x
            distancia = comprimento_x
            comprimento_x += passo_unitario_x
        else:
            celula_y += step_y
            distancia = comprimento_y
            comprimento_y += passo_unitario_y

        if not celula_esta_livre(celula_y, celula_x):
            encontrou_obstaculo = True
            celula_obstaculo = (celula_y, celula_x)
        else:
            celulas_livres.append((celula_y, celula_x))

    return celulas_livres, celula_obstaculo

def criar_occupancy_grid(num_linhas, num_colunas):
    """Cria um grid de log-odds, tudo iniciado em 0.0 (= 50% de chance, desconhecido)."""
    novo_occupancy_grid = [[0.0 for _ in range(num_colunas)] for _ in range(num_linhas)]
    return novo_occupancy_grid


def atualizar_occupancy_grid(occupancy_grid, celulas_livres, celula_obstaculo):
    """Aplica a evidência de UM raio (já processado) no occupancy_grid, in-place."""

    for linha, coluna in celulas_livres:
        occupancy_grid[linha][coluna] += EVIDENCIA_LIVRE

    if celula_obstaculo is not None:
        linha, coluna = celula_obstaculo
        occupancy_grid[linha][coluna] += EVIDENCIA_OCUPADO


def log_odds_para_probabilidade(log_odds):
    """Converte um valor de log-odds de volta para probabilidade (0 a 1)."""
    return 1 - 1 / (1 + math.exp(log_odds))

occupancy = criar_occupancy_grid(len(grid), len(grid[0]))

for i in range(16):
    angulo = i * (2 * math.pi / 16)
    celulas_livres, celula_obstaculo = lancar_raio_com_caminho(1.5, 1.5, angulo)
    atualizar_occupancy_grid(occupancy, celulas_livres, celula_obstaculo)

for linha in occupancy:
    print(" ".join(f"{log_odds_para_probabilidade(v):.2f}" for v in linha))