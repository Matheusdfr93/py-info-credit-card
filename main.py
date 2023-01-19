#importando bibliotecas
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt
import media as average
import salary as sl

#trazendo dados do documento csv
credit = pd.read_csv('./info.csv');

#atribuindo dados em listas
invoice_card = list(credit['Fatura']);
ipca_per_month = list(credit['IPCA_mensal']);
salary = list(credit['Salario']);  

invoice_card = list(map(lambda x: x.replace(',', '.'), invoice_card))
invoice_card = [float(i) for i in invoice_card];
salary = [float(i) for i in salary];
ipca_per_month = [float(i) for i in ipca_per_month];
date = list(credit['Data'])

# Criando uma lista de variação da compra por mês 
variation_per_month_invoice = []
for i in range (len(invoice_card)):
  if i == 0:
    variation_per_month_invoice.append(0);
  else:
    variation_per_month_invoice.append((invoice_card[i] - invoice_card[i-1]) / invoice_card[i-1])


#Calculando a média móvel de 
moving = average.movingAverage(invoice_card)
static = average.staticAverage(invoice_card)

#Criar uma lista de anos
year = list(set(credit['ano']))
years = list(credit['ano'])

#Encontrar a proporção salário/gastos
percentage_salary = sl.percentageSalary(salary, invoice_card)

# Criar lista de gastos por ano
expenses_per_year = []
spending = 0
for i in range (len(invoice_card)):
  if i == 0:
    spending = invoice_card[i];
  else:
      if years[i] == years[i-1]:
        spending = spending + invoice_card[i];
      if years[i] != years[i-1]:
        expenses_per_year.append(spending);
        spending = 0;
        spending = spending + invoice_card[i];
        if i == len(invoice_card) - 1:
          expenses_per_year.append(spending);
       

#Subplot 1
plt.subplot(2, 2, 1)
plt.plot(date,invoice_card, marker = '', label = 'Gastos', color = 'black');
plt.plot(date, moving, label = 'Média móvel', color = 'green');
plt.plot(date, static, label = 'Média', color = '#112299', linestyle = 'dashdot')
plt.legend(loc='best');
plt.title('Gastos por mês vs Média');
plt.xlabel('Data');
plt.grid(True)
plt.ylabel('Valor em R$');

plt.subplot(2, 2, 2)
plt.plot(date,variation_per_month_invoice, color = 'blue', label = 'Faturas');
plt.plot(date,ipca_per_month, color = 'green', label = 'IPCA'); 
plt.legend(loc='best')
plt.title('Taxa de variação das faturas X IPCA');
plt.xlabel('Data');
plt.ylabel('Variação \% em IPCA e absoluto em Faturas');


plt.subplot(2, 2, 3)
plt.bar(year,expenses_per_year, color = '#990000', label = 'Faturas');
plt.grid(True)
plt.title('Gastos por ano');
plt.xlabel('Ano');
plt.ylabel('Gastos R$');

plt.subplot(2, 2, 4)
plt.plot(date,percentage_salary, color = '#990099', label = 'Faturas');
plt.grid(True)
plt.title('Relação salário/gastos em %');
plt.xlabel('Ano');
plt.ylabel('%');

plt.show()

