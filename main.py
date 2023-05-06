#Começo
start = input("Aperte 'ENTER' para iniciar:")
print("\n\n--INICIANDO DADOS DE FATURAS--\n\n")

#Lista Faturas
lista_nome_fatura = []
lista_numero_fatura = []
lista_valor_separado = []
lista_valor_fatura = []

#Listas Despesa
lista_nome_despesa = []
lista_numero_despesa = []
lista_valor_separado_d = []
lista_valor_despesa = []

sentinela = -1

#Captação de dados Faturas
nome_fatura = str(input("Digite o nome de uma fatura: "))#Nome do oque foi ganho
lista_nome_fatura.append(nome_fatura)

qntd_faturas = int(input("Digite a quantidade: "))#Número de vezes
lista_numero_fatura.append(qntd_faturas)

soma_faturas = 0
if (qntd_faturas > 1):
    fatura_mes = float(input("Digite o valor faturado R$: "))#valor
    lista_valor_separado.append(fatura_mes)
    fatura_mesT = (fatura_mes * qntd_faturas)
    lista_valor_fatura.append(fatura_mesT)
    soma_faturas += fatura_mesT
else:
    fatura_mes = float(input("Digite o valor faturado R$: "))#valor
    lista_valor_separado.append(fatura_mes)
    fatura_mesT = (fatura_mes * qntd_faturas)
    lista_valor_fatura.append(fatura_mes)
    soma_faturas += fatura_mesT
print("Salvo...\n")

while True:
    nome_fatura = str(input("Nome: "))#Nome do oque foi ganho
    if nome_fatura == str(sentinela):
        break
    else:
        lista_nome_fatura.append(nome_fatura)

        qntd_faturas = int(input("Quantidade: "))#Número de vezes
        lista_numero_fatura.append(qntd_faturas)
        
        if (qntd_faturas > 1):
            fatura_mes = float(input("Valor R$: "))#valor
            lista_valor_separado.append(fatura_mes)
            fatura_mesT = (fatura_mes * qntd_faturas)
            lista_valor_fatura.append(fatura_mesT)
            soma_faturas += fatura_mesT
        else:
            fatura_mes = float(input("Valor R$: "))#valor
            lista_valor_separado.append(fatura_mes)
            lista_valor_fatura.append(fatura_mes)
            soma_faturas += fatura_mes
    print("Salvo...\n")


#Captação de dados Despesas
print("\n\n--INICIANDO DADOS DE DESPESAS--\n\n")
inicio = input("Aperte 'ENTER' para continuar: ")

nome_despesa = str(input("Digite o nome da sua despesa: "))#Nome do oque foi gasto
lista_nome_despesa.append(nome_despesa)

qntd_despesas = int(input("Digite a quantidade: "))#Número de vezes
lista_numero_despesa.append(qntd_despesas)

soma_despesas = 0
if (qntd_despesas > 1):
    despesa_mes = float(input("Digite o valor da sua despesa R$: "))#valor
    lista_valor_separado_d.append(despesa_mes)
    despesa_mesT = (despesa_mes * qntd_despesas)
    lista_valor_despesa.append(despesa_mesT)
    soma_despesas += despesa_mesT
else:
    despesa_mes = float(input("Digite o valor da sua despesa R$: "))#valor
    lista_valor_separado_d.append(despesa_mes)
    lista_valor_despesa.append(despesa_mes)
    soma_despesas += despesa_mes
print("Salvo...\n")

while True:
    nome_despesa = str(input("Nome: "))#Nome do oque foi gasto
    if nome_despesa == str(sentinela):
        break
    else:
        lista_nome_despesa.append(nome_despesa)
        
        qntd_despesas = int(input("Quantidade: "))#Número de vezes
        lista_numero_despesa.append(qntd_despesas)
        
        if (qntd_despesas > 1):
            despesa_mes = float(input("Valor R$: "))#valor
            lista_valor_separado_d.append(despesa_mes)
            despesa_mesT = (despesa_mes * qntd_despesas)
            lista_valor_despesa.append(despesa_mesT)
            soma_despesas += despesa_mesT
        else:
            despesa_mes = float(input("Valor R$: "))#valor
            lista_valor_separado_d.append(despesa_mes)
            lista_valor_despesa.append(despesa_mes)
            soma_despesas += despesa_mes
    print("Salvo...\n")
#Fim captação de dados


#Tuplas ordenadas
tuplas = list(zip(lista_nome_fatura, lista_numero_fatura, lista_valor_separado, lista_valor_fatura, lista_nome_despesa, lista_numero_despesa, lista_valor_separado_d, lista_valor_despesa))

tuplas_ordenadas = sorted(tuplas, reverse = True, key = lambda x: x[5])

lista_nome_fatura_ordenada = [t[0] for t in tuplas_ordenadas]
lista_numero_fatura_ordenada = [t[1] for t in tuplas_ordenadas]
lista_valor_separado_ordenada = [t[2] for t in tuplas_ordenadas]
lista_valor_fatura_ordenada = [t[3] for t in tuplas_ordenadas]


lista_nome_despesa_ordenada = [t[4] for t in tuplas_ordenadas]
lista_numero_despesa_ordenada = [t[5] for t in tuplas_ordenadas]
lista_valor_separado_d_ordenada = [t[6] for t in tuplas_ordenadas]
lista_valor_despesa_ordenada = [t[7] for t in tuplas_ordenadas]

#Impressão de dados
print("\n        Resultados")
print("\n--------FATURAS--------")
print("Nome: ", lista_nome_fatura_ordenada)
print("Quantidade: ", lista_numero_fatura_ordenada)
print("Valor por quantidade: ", lista_valor_separado_ordenada)
print("Valor total: ", lista_valor_fatura_ordenada)

print("\n--------Despesas--------")
print("Nome: ", lista_nome_despesa_ordenada)
print("Quantidade: ", lista_numero_despesa_ordenada)
print("Valor por quantidade: ", lista_valor_separado_d_ordenada)
print("Valor total: ", lista_valor_despesa_ordenada)
print("\n")

ganho_total = soma_faturas - soma_despesas
if ganho_total < 0:
    print("\nVocê possui mais despesas do que faturas este mês, você perdeu R$ {}".format(ganho_total))
elif ganho_total == 0:
    print("\nVocê não obteve ganhos este mês, pois seu valor de faturas é o mesmo valor de despesas, ou seja, você faturou R$ 0,00")
else:
    print("\nVocê faturou este mês R$ {}\n".format(ganho_total))

print("Total das faturas: ", soma_faturas)
print("Total das despesa: ", soma_despesas)

ganho_diario = soma_faturas / 30
despesa_diaria = soma_despesas / 30

print("\nSeu valor de fatura diária é de R$ {:.2f} \n".format(ganho_diario))
print("Seu valor de despesa diária é de R${:.2f} \n".format(despesa_diaria))
