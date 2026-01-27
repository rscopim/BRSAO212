'''4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.'''

from datetime import date
def dias_de_vida(data_nascimento: date) -> int:
    hoje = date.today()
    return (hoje - data_nascimento).days
ano = int(input("Digite o ano de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
dia = int(input("Digite o dia de nascimento: "))
data_nascimento = date(ano, mes, dia)
total_dias = dias_de_vida(data_nascimento)
print(f"Você está vivo há aproximadamente {total_dias:,} dias.")
