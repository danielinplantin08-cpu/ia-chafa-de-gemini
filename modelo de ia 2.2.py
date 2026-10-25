from operator import iadd
"""librerias externas"""
import math
import json
import os
import random
"""variables"""
sat = random
nu = os
ana = json
uwu = iadd
neurona1 = math
"""codigo"""
class Neurona:
    def __init__(self, n_entradas):
        self.pesos = [random.uniform(-1, 1) for _ in range(n_entradas)]
        self.sesgo = random.uniform(-1, 1)

