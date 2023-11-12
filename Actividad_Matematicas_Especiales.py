import numpy as np
import matplotlib.pyplot as plt

# Definir la función original
def f(t, T):
    return 90 * np.sin(2 * np.pi * t / T)

# Definir la aproximación de la serie de Fourier con N términos
def fourier_approx(t, T, N):
    result = 0
    for n in range(1, N + 1):
        result += (180 / (np.pi * n)) * (1 - (-1)**n) * np.sin(2 * np.pi * n * t / T)
    return result

# Parámetros
T = 4  # Período de la puerta
N_terms = 10  # Número de términos en la serie de Fourier

# Generar datos para la gráfica
t_values = np.linspace(0, T, 1000)
original_values = f(t_values, T)
approx_values = fourier_approx(t_values, T, N_terms)

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(t_values, original_values, label='Función original')
plt.plot(t_values, approx_values, label=f'Aproximación con {N_terms} términos')
plt.title('Aproximación con Serie de Fourier')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ángulo de la puerta')
plt.legend()
plt.grid(True)
plt.show()
