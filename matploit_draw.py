


# Визначте функції належності
# kr1 = np.interp(x1, [0, 5, 10, 15, 20, 25, 30, 35], [1, 1, 0.833, 0.667, 0.5, 0.333, 0.167, 0])
# n1 = np.interp(x1, [0, 5, 10, 15, 20, 25, 30, 35], [0, 0.5, 1, 1, 0.75, 0.5, 0.25, 0])
# s1 = np.interp(x1, [0, 5, 10, 15, 20, 25, 30, 35], [0, 0.25, 0.5, 0.75, 1, 1, 0.5, 0])
# v1 = np.interp(x1, [0, 5, 10, 15, 20, 25, 30, 35], [0, 0.167, 0.333, 0.5, 0.667, 0.833, 1, 1])

# функції належності Fe
# plt.figure()
# plt.plot(x1, kr1, 'b', linewidth=1.5, label='Кр')
# plt.plot(x1, n1, 'g', linewidth=1.5, label='Н')
# plt.plot(x1, s1, 'r', linewidth=1.5, label='С')
# plt.plot(x1, v1, 'c', linewidth=1.5, label='В')

# plt.title('Функції належності Fe')
# plt.ylabel('Ступінь належності')
# plt.xlabel('Універсальна змінна (x)')
# plt.legend(loc='upper right')
# plt.grid(True)
# plt.show()



# Визначте функції належності
# n2 = np.interp(x2, [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5], [1, 1, 1, 1, 0.75, 0.5, 0.25, 0])
# s2 = np.interp(x2, [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5], [0, 0.25, 0.5, 0.75, 1, 1, 0.5, 0])
# v2 = np.interp(x2, [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5], [0, 0.167, 0.333, 0.5, 0.667, 0.833, 1, 1])

# функції належності Ca
# plt.figure()
# plt.plot(x2, n2, 'g', linewidth=1.5, label='Н')
# plt.plot(x2, s2, 'r', linewidth=1.5, label='С')
# plt.plot(x2, v2, 'c', linewidth=1.5, label='В')

# plt.title('Функції належності Ca')
# plt.ylabel('Ступінь належності')
# plt.xlabel('Універсальна змінна (x)')
# plt.legend(loc='upper right')
# plt.grid(True)
# plt.show()



# Визначте функції належності
# n3 = np.interp(x3, [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2], [1, 1, 1, 0.833, 0.667, 0.5, 0.333, 0.167, 0])
# s3 = np.interp(x3, [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2], [0, 0.333, 0.667, 1, 1, 0.75, 0.5, 0.25, 0])
# v3 = np.interp(x3, [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2], [0, 0.167, 0.333, 0.5, 0.667, 0.833, 1, 1, 1])

# функції належності Mg
# plt.figure()
# plt.plot(x3, n3, 'g', linewidth=1.5, label='Н')
# plt.plot(x3, s3, 'r', linewidth=1.5, label='С')
# plt.plot(x3, v3, 'c', linewidth=1.5, label='В')

# plt.title('Функції належності Mg')
# plt.ylabel('Ступінь належності')
# plt.xlabel('Універсальна змінна (x)')
# plt.legend(loc='upper right')
# plt.grid(True)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

print("Визначаємо функції належності для Y...")
x0 = np.arange(0, 101, 10)
n = fuzz.trapmf(x0, [0, 0, 10, 40])
ns = fuzz.trimf(x0, [10, 20, 50])
s = fuzz.trimf(x0, [20, 40, 60])
vs = fuzz.trimf(x0, [30, 70, 100])
v = fuzz.trapmf(x0, [50, 90, 100, 100])
print(x0)
print(n)
print(ns)
print(s)
print(vs)
print(v)

print("\nВизначаємо функції належності для Fe...")
x1 = np.arange(0, 36, 1)
kr1 = fuzz.trapmf(x1, [0, 0, 5, 15])
n1 = fuzz.trimf(x1, [5, 10, 20])
s1 = fuzz.trimf(x1, [10, 20, 30])
v1 = fuzz.trapmf(x1, [20, 30, 35, 35])
print(x1)
print(kr1)
print(n1)
print(s1)
print(v1)

print("\nВизначаємо функції належності для Ca...")
x2 = np.arange(0, 3.6, 0.1)
n2 = fuzz.trapmf(x2, [0, 0, 1.5, 2.5])
s2 = fuzz.trimf(x2, [1, 2, 3])
v2 = fuzz.trapmf(x2, [1.5, 3, 3.5, 3.5])
print(x2)
print(n2)
print(s2)
print(v2)

print("\nВизначаємо функції належності для Mg...")
x3 = np.arange(0.4, 1.3, 0.1)
n3 = fuzz.trapmf(x3, [0.4, 0.4, 0.6, 0.8])
s3 = fuzz.trimf(x3, [0.5, 0.7, 1.1])
v3 = fuzz.trapmf(x3, [0.7, 1.1, 1.2, 1.2])
print(x3)
print(n3)
print(s3)
print(v3)

fig, axs = plt.subplots(4, figsize=(9, 10))

axs[0].plot(x0, n, 'b', linewidth=1.5, label='Н')
axs[0].plot(x0, ns, 'g', linewidth=1.5, label='НС')
axs[0].plot(x0, s, 'r', linewidth=1.5, label='С')
axs[0].plot(x0, vs, 'c', linewidth=1.5, label='ВС')
axs[0].plot(x0, v, 'm', linewidth=1.5, label='В')
axs[0].set_title('Функції належності Y')
axs[0].set_ylabel('Ступінь належності')
axs[0].legend(loc='upper right')
axs[0].grid(True)

axs[1].plot(x1, kr1, 'b', linewidth=1.5, label='Кр')
axs[1].plot(x1, n1, 'g', linewidth=1.5, label='Н')
axs[1].plot(x1, s1, 'r', linewidth=1.5, label='С')
axs[1].plot(x1, v1, 'c', linewidth=1.5, label='В')
axs[1].set_title('Функції належності Fe')
axs[1].set_ylabel('Ступінь належності')
axs[1].legend(loc='upper right')
axs[1].grid(True)

axs[2].plot(x2, n2, 'g', linewidth=1.5, label='Н')
axs[2].plot(x2, s2, 'r', linewidth=1.5, label='С')
axs[2].plot(x2, v2, 'c', linewidth=1.5, label='В')
axs[2].set_title('Функції належності Ca')
axs[2].set_ylabel('Ступінь належності')
axs[2].legend(loc='upper right')
axs[2].grid(True)

axs[3].plot(x3, n3, 'g', linewidth=1.5, label='Н')
axs[3].plot(x3, s3, 'r', linewidth=1.5, label='С')
axs[3].plot(x3, v3, 'c', linewidth=1.5, label='В')
axs[3].set_title('Функції належності Mg')
axs[3].set_ylabel('Ступінь належності')
axs[3].legend(loc='upper right')
axs[3].grid(True)

plt.tight_layout()
plt.show()
