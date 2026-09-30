import calendar
print("---📅Gerador de Calendário📅---")
mes = int(input('Digite o número do mês (1-12):'))
ano = int(input('Digite o número do ano:'))
if mes < 1 or mes > 12:
    print('Mês inválido! Digite um número entre 1 e 12.')
else:
    print('\n SEU CALENDÁRIO')
    print(calendar.month(ano,mes))