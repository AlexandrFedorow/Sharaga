import pandas as pd

import matplotlib.pyplot as plt

colums = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']

df = pd.read_excel('data.xlsx', usecols=['t']+colums)
print(df.head(8))

fig, axs = plt.subplots(nrows=1, ncols=4)

#add title
fig.suptitle('Банк 0')

#add data to plots
axs[0].plot(df['t'], df['A0'])
axs[1].plot(df['t'], df['A0'])
axs[2].plot(df['t'], df['A0'])
axs[3].plot(df['t'], df['A0'])


"""plt.xlabel('Время, с')
plt.ylabel('Температура, °C')
plt.title('График остывания капсулы №0')
plt.grid()"""
plt.savefig('plot.png')

