

# xp: це масив x-координат вихідних точок для інтерполяції.
# fp: це масив y-координат вихідних точок для інтерполяції. Його довжина повинна бути такою ж, як і xp.

# print("Визначаємо функції належності для Fe...")
# kr1 = fuzz.interp_membership(x1, [0, 5, 10, 15, 20, 25, 30, 35], [1, 1, 0.833, 0.667, 0.5, 0.333, 0.167, 0])
# n1 = fuzz.interp_membership(x1, [0, 5, 10, 15, 20, 25, 30, 35], [0, 0.5, 1, 1, 0.75, 0.5, 0.25, 0])
# s1 = fuzz.interp_membership(x1, [0, 5, 10, 15, 20, 25, 30, 35], [0, 0.25, 0.5, 0.75, 1, 1, 0.5, 0])
# v1 = fuzz.interp_membership(x1, [0, 5, 10, 15, 20, 25, 30, 35], [0, 0.167, 0.333, 0.5, 0.667, 0.833, 1, 1])

# print("Визначаємо функції належності для Ca...")
# n2 = fuzz.interp_membership(x2, [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5], [1, 1, 1, 1, 0.75, 0.5, 0.25, 0])
# s2 = fuzz.interp_membership(x2, [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5], [0, 0.25, 0.5, 0.75, 1, 1, 0.5, 0])
# v2 = fuzz.interp_membership(x2, [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5], [0, 0.167, 0.333, 0.5, 0.667, 0.833, 1, 1])

# print("Визначаємо функції належності для Mg...")
# n3 = fuzz.interp_membership(x3, [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2], [1, 1, 1, 0.833, 0.667, 0.5, 0.333, 0.167, 0])
# s3 = fuzz.interp_membership(x3, [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2], [0, 0.333, 0.667, 1, 1, 0.75, 0.5, 0.25, 0])
# v3 = fuzz.interp_membership(x3, [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2], [0, 0.167, 0.333, 0.5, 0.667, 0.833, 1, 1, 1])


# print("Визначаємо функції належності для Fe...")
# x1 = np.arange(0, 36, 1)
# kr1 = fuzz.interp_membership(x1, np.linspace(0, 35, 36), np.linspace(1, 0, 36))
# n1 = fuzz.interp_membership(x1, np.linspace(0, 35, 36), np.linspace(0, 1, 36))
# s1 = fuzz.interp_membership(x1, np.linspace(0, 35, 36), np.linspace(0, 1, 36))
# v1 = fuzz.interp_membership(x1, np.linspace(0, 35, 36), np.linspace(0, 1, 36))

# print("Визначаємо функції належності для Ca...")
# x2 = np.arange(0, 3.6, 0.1)
# n2 = fuzz.interp_membership(x2, np.linspace(0, 3.5, 36), np.linspace(1, 0, 36))
# s2 = fuzz.interp_membership(x2, np.linspace(0, 3.5, 36), np.linspace(0, 1, 36))
# v2 = fuzz.interp_membership(x2, np.linspace(0, 3.5, 36), np.linspace(0, 1, 36))

# print("Визначаємо функції належності для Mg...")
# x3 = np.arange(0.4, 1.3, 0.1)
# n3 = fuzz.interp_membership(x3, np.linspace(0.4, 1.2, 9), np.linspace(1, 0, 9))
# s3 = fuzz.interp_membership(x3, np.linspace(0.4, 1.2, 9), np.linspace(0, 1, 9))
# v3 = fuzz.interp_membership(x3, np.linspace(0.4, 1.2, 9), np.linspace(0, 1, 9))

import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

print("Визначаємо функції належності для Fe...")
x1 = np.arange(0, 36, 1)
kr1 = fuzz.trimf(x1, [0, 5, 15])
n1 = fuzz.trimf(x1, [5, 10, 20])
s1 = fuzz.trimf(x1, [10, 20, 30])
v1 = fuzz.trimf(x1, [20, 30, 35])

print("Визначаємо функції належності для Ca...")
x2 = np.arange(0, 3.6, 0.1)
n2 = fuzz.trimf(x2, [0, 1.5, 2.5])
s2 = fuzz.trimf(x2, [1, 2, 3])
v2 = fuzz.trimf(x2, [1.5, 3, 3.5])

print("Визначаємо функції належності для Mg...")
x3 = np.arange(0.4, 1.3, 0.1)
n3 = fuzz.trimf(x3, [0.4, 0.6, 0.8])
s3 = fuzz.trimf(x3, [0.5, 0.7, 1.1])
v3 = fuzz.trimf(x3, [0.7, 1.1, 1.2])


print("Створюємо нечіткі вхідні та вихідні змінні...")
fe = ctrl.Antecedent(x1, 'Fe')
mg = ctrl.Antecedent(x2, 'Mg')
ca = ctrl.Antecedent(x3, 'Ca')
ps = ctrl.Consequent(np.arange(0, 1, 0.1), 'Ps')
#ps = ctrl.Consequent(np.arange(0, 101, 1), 'Ps')

print("Визначаємо нечіткі множини...")
fe['Cr'] = kr1
fe['L'] = n1
fe['A'] = s1
fe['H'] = v1

mg['L'] = n2
mg['A'] = s2
mg['H'] = v2

ca['L'] = n3
ca['A'] = s3
ca['H'] = v3

# ps['L'] = fuzz.interp_membership(np.arange(0, 101, 1), [0, 10, 80], [1, 1, 0])
# ps['BA'] = fuzz.interp_membership(np.arange(0, 101, 1), [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [0, 0.5, 1, 1, 0.8, 0.6, 0.4, 0.2, 0, 0, 0])
# ps['A'] = fuzz.interp_membership(np.arange(0, 101, 1), [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [0, 0.25, 0.5, 0.75, 1, 1, 0.75, 0.5, 0.25, 0, 0])
# ps['AA'] = fuzz.interp_membership(np.arange(0, 101, 1), [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [0, 0.1666666667, 0.3333333333, 0.5, 0.6666666667, 0.8333333333, 1, 1, 0.5, 0, 0])
# ps['H'] = fuzz.interp_membership(np.arange(0, 101, 1), [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1, 1, 1])

ps['L'] = fuzz.interp_membership(np.arange(0, 1, 0.1), np.linspace(0, 1, 10), np.linspace(1, 0, 10))
ps['A'] = fuzz.interp_membership(np.arange(0, 1, 0.1), np.linspace(0, 1, 10), np.linspace(0, 1, 10))
ps['AA'] = fuzz.interp_membership(np.arange(0, 1, 0.1), np.linspace(0, 1, 10), np.linspace(0, 1, 10))
ps['BA'] = fuzz.interp_membership(np.arange(0, 1, 0.1), np.linspace(0, 1, 10), np.linspace(0, 1, 10))


print("Визначаємо правила...")
rule1 = ctrl.Rule(fe['Cr'] & mg['L'] & ca['L'], ps['L'])
rule2 = ctrl.Rule(fe['Cr'] & mg['A'] & ca['A'], ps['A'])
rule3 = ctrl.Rule(fe['L'] & mg['A'] & ca['A'], ps['AA'])
rule4 = ctrl.Rule(fe['L'] & mg['A'] & ca['L'], ps['AA'])
rule5 = ctrl.Rule(fe['L'] & mg['L'] & ca['L'], ps['BA'])
rule6 = ctrl.Rule(fe['L'] & mg['H'] & ca['L'], ps['AA'])
rule7 = ctrl.Rule(fe['A'] & mg['L'] & ca['L'], ps['BA'])
rule8 = ctrl.Rule(fe['A'] & mg['H'] & ca['A'], ps['A'])

print("Створюємо систему контролю та виконуємо обчислення...")
ps_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
tipping = ctrl.ControlSystemSimulation(ps_ctrl)

print("Вводимо вхідні значення...")
tipping.input['Fe'] = 1.909

tipping.input['Mg'] = 0.552

tipping.input['Ca'] = 18.57

print("Виконуємо обчислення...")
tipping.compute()

print("Виводимо результат...")
print(tipping.output['Ps']*100)