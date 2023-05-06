import main as t
import pandas as pd

Nome1 = t.lista_nome_fatura_ordenada
Qntd1 = t.lista_numero_fatura_ordenada
vSeparado1 = t.lista_valor_separado_ordenada
vTotal1 = t.lista_valor_fatura_ordenada

Nome2 = t.lista_nome_despesa_ordenada
Qntd2 = t.lista_numero_despesa_ordenada
vSeparado2 = t.lista_valor_separado_d_ordenada
vTotal2 = t.lista_valor_despesa_ordenada

tabela = pd.DataFrame({"Nome da Faturas" : Nome1, "Valor qntd Fatura" : vSeparado1, "Quantidade Fatura" : Qntd1, "Valor Total Fatura" : vTotal1, "Nome da Despesa" : Nome2, "Valor qntd Despesa" : vSeparado2, "Quantidade Despesa" :  Qntd2, "Valor Total Despesa" : vTotal2})

tabela.to_csv('tabela.csv', index = False)