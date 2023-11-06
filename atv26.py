# Exercício Python 26: Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.
# Solicita o primeiro termo e a razão da PA ao usuário
a1 = int(input("Digite o primeiro termo da PA: "))
a2 = int(input("Digite a razão da PA: "))
for g in range(10):
    print(g)
    termo = a1 + g * a2
    print(f'Termo {g+1}: {termo}')