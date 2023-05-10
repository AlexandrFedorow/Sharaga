import pandas as pd

import matplotlib.pyplot as plt

colums = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']

df = pd.read_excel('data.xlsx', usecols=['t']+colums)

time = 0
plt.figure(figsize=(50, 10))
for i in colums:
    plt.plot(df['t']+time, df[i])
    time += 300

plt.xlabel('Время, с')
plt.ylabel('Температура, °C')
plt.title('График остывания капсулы №8')
plt.grid()
#plt.yticks(ticks=df['A0'][::4], labels=df['A0'][::4])
plt.savefig('plot.png')


#fig.savefig('plot.png')