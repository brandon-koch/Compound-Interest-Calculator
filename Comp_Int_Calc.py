import time
from datetime import date
import pandas as pd
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

class text:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

year = str(date.today())[:4]
y = int(year)

print("Compound Interest Calculator\n")
while True:
  try:
    print("Enter initial investment")
    principal = input("--> $")
    try:
      float(principal)
    except ValueError:
      print("Error: use numbers or decimals only.\n")
      time.sleep(1.5)
    else:
      break
  except ValueError as e:
    print(e)

while True:
  try:
    print("\nEnter time span (years)")
    time = input("--> ")
    if not time.isnumeric():
      raise ValueError("Error: use integer value only.")
      time.sleep(1.5)
    else:
      break
  except ValueError as e:
    print(e)

while True:
  try:
    print("\nEnter interest rate (percent)")
    rate = input("--> ")
    try:
      float(rate)
    except ValueError:
      print("Error: use numbers or decimals only.\n")
      time.sleep(1.5)
    else:
      break
  except ValueError as e:
    print(e)

print("\nSelect a compound frequency")
print("1) Daily")
print("2) Weekly")
print("3) Biweekly")
print("4) Monthly")
print("5) Quarterly")
print("6) Annualy")

while True:
  try:
    compounds = input("--> ")
    if not compounds.isnumeric():
      raise ValueError("Error: use integer value only.")
      time.sleep(1.5)
    elif int(compounds) < 1 or int(compounds) > 6:
      raise ValueError(f'Error: option "{compounds}" does not exist.\n')
      time.sleep(1.5)
    else:
      break
  except ValueError as e:
    print(e)

p = float(principal)
t = int(time)
r = (float(rate)) / 100
if compounds == "1":
  n = 365
elif compounds == "2":
  n = 52
elif compounds == "3":
  n = 26
elif compounds == "4":
  n = 12
elif compounds == "5":
  n = 4
elif compounds == "6":
  n = 1

a1 = (1 + (r/n))
a2 = n * t
a = p * (a1**a2)
amounts = []
raw = []
span = []

for i in range(y, y+t+1):
  span.append(i)

p2 = round(p, 2)
p3 = "{:,.2f}".format(p2)
p4 = f"${p3}"
amounts.append(p4)
raw.append(p2)

for i in range (1, t + 1):
  a3 = (1 + (r/n))
  a4 = n * i
  a5 = p * (a3**a4)
  raw.append(round(a5, 2))
  a6 = "{:,.2f}".format(a5)
  amounts.append(f"${a6}")
  y += 1

end = raw[-1]
end2 = "{:,.2f}".format(end)
print("_____________________________")
print("\n" + text.UNDERLINE + text.BOLD + "RESULTS" + text.END)
print(f"Start value: \t{p4}")
print(f"End value: \t${end2}")
g = ((end / p2) - 1) * 100
g2 = "{:,.2f}".format(g)

if end > p2:
  print(f"Growth: \t+{g2}%\n")
else:
  print(f"Growth: \t{g2}%\n")

dict1 = {text.BOLD +'Year'+ text.END : span, text.BOLD +'Value'+ text.END : amounts}
df = pd.DataFrame(dict1)
print(tabulate(df, headers = 'keys', tablefmt = 'fancy_grid', showindex=False))
print()
plt.xlabel("Year")
plt.ylabel("Value")
plt.bar(span, raw)
plt.ylim(.9*p, 1.05*end)

if p <= 100:
  ticks = (end-p)/7
elif p > 100 and p <= 1112:
  ticks = round((end-p)/7, -1)
elif p > 1112 and p < 100000:
  ticks = round((end-p)/7, -2)
else:
  ticks = round((end-p)/7, -3)

plt.yticks(np.arange(p, 1.05*end, ticks))
plt.show()
