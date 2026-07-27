"""
Simula uma leitura completa de LiDAR: dispara vários raios igualmente
espaçados ao redor de uma posição, reaproveitando lancar_raio.
"""

import math
from raycasting import lancar_raio


def simular_lidar(pos_x, pos_y, numero_raios=360, distancia_maxima_celulas=50):
    """
    Devolve uma lista de dicionários, um por raio:
    {"angulo": ..., "distancia": ..., "encontrou_obstaculo": ...}
    """
    leituras = []

    espacamento_angular = 2 * math.pi / numero_raios

    for i in range(numero_raios):
        angulo = i * espacamento_angular

        distancia, encontrou = lancar_raio(pos_x, pos_y, angulo, distancia_maxima_celulas)

        leituras.append({
            "angulo": angulo,
            "distancia": distancia,
            "encontrou_obstaculo": encontrou,
        })

    return leituras


leituras = simular_lidar(pos_x=1.5, pos_y=1.5, numero_raios=16)

for leitura in leituras:
    graus = math.degrees(leitura["angulo"])
    status = "obstáculo" if leitura["encontrou_obstaculo"] else "livre (limite)"
    print(f"Ângulo {graus:6.1f}°  ->  distância {leitura['distancia']:.2f} células  ({status})")