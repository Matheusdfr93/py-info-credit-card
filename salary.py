def percentageSalary(salary, invoice_card):
  percentage_salary = []
  average = []
  for i in range(len(invoice_card)):
    if salary[i] == 0:
      percentage_salary.append(0)
    else:
      percentage_salary.append(invoice_card[i]*100/salary[i])
  return percentage_salary