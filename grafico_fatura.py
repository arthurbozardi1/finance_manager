import matplotlib.pyplot as plt
import main as t

plt.bar(t.lista_nome_fatura_ordenada, t.lista_valor_fatura_ordenada)
plt.xlabel('Nome')
plt.ylabel('R$')
plt.title('Grafico de Faturas Mensais')
plt.show()