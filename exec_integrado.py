import time

inicio = ("\n\nInstruções gerais: \n\n"
      "1) O programa foi desenvolvido por um estudante; \n"
      "2) A inteção geral do programa é mostrar por meio de uma planilha e gráficos o resultado finânceiro mensal do seu negócio;\n"
      "3) Escreva -1 após informar um dado, irá encerrar a captação de informações;\n"
      "4) O programa é formado por duas partes 1.Fatura e 2.Despesas;\n"
      "5) Se você não possuir despesas ou não possuir faturas, apenas pule escrevendo -1;\n")
for letra in inicio:
    print(letra, end = '', flush = True)
    time.sleep(0.03)

import main as main
import planilha as planilha
import grafico_fatura as grafico_fatura
import grafico_despesa as grafico_despesa

fim = ("Dados Salvos \n Fim do Programa \n\n\nObrigado por utilizar :)\n\n")
for letras in fim:
    print(letras, end='', flush = True)
    time.sleep(0.03)
    