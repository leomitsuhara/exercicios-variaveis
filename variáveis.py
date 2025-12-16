# LISTA DE EXERCÍCIOS - VARIÁVEIS

# 1. SOMA SIMPLES
# Peça dois números ao usuário, salve em variáveis e mostre a soma deles.
 
n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
soma = n1 + n2

print(f"A soma entre {n1} e {n2} é {soma}.")

# 2. Conversor de idade
# Peça a idade do usuário e mostre quantos dias isso representa (desconsidere anos bissextos).
idade = int(input("Digite sua idade: "))
dias = idade * 365
print(f"Sua idade em dias é aproximadamente {dias} dias.")

# 3. Área do retângulo
# Peça a largura e altura de um retângulo e calcule a área.
altura = float(input("Digite a altura do retângulo: "))
largura = float(input("Digite a largura do retângulo: "))
area = altura * largura
print(f"A área do retângulo é {area:.2f}")

# 4. Concatenar nome completo
# Peça nome e sobrenome e exiba o nome completo usando variáveis.
nome = str(input("Digite seu nome: ")).strip()  # .strip() remove espaços antes e depois do texto.
sobrenome = str(input("Digite seu sobrenome: ")).strip()
print(f"Seu nome completo é {nome} {sobrenome}")

# 5. Converter Celsius → Fahrenheit
# Peça a temperatura em Celsius e converta para Fahrenheit usando a fórmula:
# F = C × 1.8 + 32
celsius = float(input("Digite a temperatura em Celsius para converter para Fahrenheit: "))
fahrenheit = celsius * 1.8 + 32
print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F")

# 6. Cálculo de salário
# Peça o salário mensal e o número de meses trabalhados no ano. Mostre o total anual.
salario = float(input("Digite seu salário: R$"))
meses_trabalhados = int(input("Quantos meses você trabalhou? "))
total_anual = salario * meses_trabalhados
print(f"O seu total anual será de R${total_anual:.2f}")

# 7. Preço com desconto
# Peça o preço de um produto e um percentual de desconto. Mostre o preço final.
produto = float(input("Digite o valor do produto: R$"))
desconto = float(input("Digite o percentual de desconto (sem o %): "))
valor_desconto = produto * (desconto / 100)
valor_final = produto - valor_desconto
print(f"O produto de R${produto:.2f} com {desconto}% de desconto fica por R${valor_final:.2f}")

# 8. Média de três números
# Leia três números e calcule a média deles.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
media = (n1 + n2 + n3) / 3
print(f"A média dos números {n1}, {n2} e {n3} é {media}")


# 9. Conversor de tempo
# Peça um valor em segundos e converta para minutos e horas (somente cálculos, sem formatação bonita).
segundos = int(input("Digite os segundos: "))
minutos = segundos / 60
horas = minutos / 60
print(f"{segundos} segundos equivalem a {minutos:.2f} minutos ou {horas:.2f} horas.")

# 10. Cálculo de IMC
# Peça peso e altura e calcule o IMC:
# IMC = peso / (altura²)

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura**2)
print(f"Seu IMC é {imc:.2f}")
