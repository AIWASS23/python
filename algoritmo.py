import math
import numpy as np
import matplotlib.pyplot as plt

def log_function(x, b):
    if x < b:
        return 0  
    return 1 + log_function(x/b, b)

def log_natural(x):
    n = 10000.0
    return n * ((x ** (1/n)) - 1)

dados = np.arange(1, 51)
log_natural = np.log(dados)
log_base_2 = np.log2(dados)
log_base_10 = np.log10(dados)

plt.figure(figsize=(14,8))
plt.xlabel('Dados de entrada', fontsize=16)
plt.ylabel('Função Logarítmica', fontsize=16)
plt.title('Logaritmos', fontsize=25)
plt.grid()
plt.plot(dados, log_natural, linewidth=4, color='r', label='log natural')
plt.plot(dados, log_base_2, linewidth=4, color='b', label='log base 2')
plt.plot(dados, log_base_10, linewidth=4, color='g', label='log base 10')
plt.legend(fontsize=16)
plt.show()

