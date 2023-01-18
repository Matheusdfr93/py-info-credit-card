def movingAverage(invoice_card):
  med = 0
  moving_average = []
  for i in range(len(invoice_card)):
    if i == 0:
      med = invoice_card[i];
      moving_average.append(med);
    else:
      med = (med * (i) + invoice_card[i])/(i+1);
      moving_average.append(med)
  return moving_average

def staticAverage(invoice_card):
  med = 0
  average = []
  for i in range(len(invoice_card)):
    med = med + invoice_card[i];
  
  for i in range(len(invoice_card)):
    average.append(med/len(invoice_card))
  return average