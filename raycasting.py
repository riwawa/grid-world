"""
Ray Casting usando o algoritmo DDA (Digital Differential Analyzer),
adaptado de javidx9 (https://youtu.be/NbSee-XM7WA) para Python, reaproveitando
o grid e a função celula_esta_livre já implementados.

Convenção: x = coluna (horizontal), y = linha (vertical) -- mesma convenção
já usada em mundo_para_celula/celula_para_mundo.

Todas as distâncias neste arquivo são em UNIDADES DE CÉLULA (não metros)
durante o cálculo -- a conversão pra metros acontece só no final, multiplicando
por TAMANHO_CELULA_METROS.
"""

import math

from grid import TAMANHO_CELULA_METROS
from grid import celula_esta_livre as celula_esta_livre_grid
from grid import grid


def lancar_raio(pos_x, pos_y, angulo_radianos, distancia_maxima_celulas=50):

    dx = math.cos(angulo_radianos)
    dy = math.sin(angulo_radianos)

    if dx == 0:
        passo_unitario_x = float('inf')
    else:
        passo_unitario_x = abs(1 / dx)

    if dy == 0:
        passo_unitario_y = float('inf')
    else:
        passo_unitario_y = abs(1 / dy)

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

    # --- Loop de caminhada (walk) ---
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


        if not celula_esta_livre_grid(celula_y, celula_x):
            encontrou_obstaculo = True

    return distancia, encontrou_obstaculo


distancia, achou = lancar_raio(pos_x=1.5, pos_y=1.5, angulo_radianos=0)  # apontando para +X (direita)
print(f"Raio para a direita: distância={distancia:.2f} células, achou obstáculo={achou}")
print(f"Em metros: {distancia * TAMANHO_CELULA_METROS:.2f}m")