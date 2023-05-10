import pandas as pd

import matplotlib.pyplot as plt

I = [2,5,10,20,30,35]

df = pd.read_excel('ebe.xlsx', usecols=['II', 'K', 'N', 'KC', 'UV', 'IV', 'US', 'IS', 'UC', 'IC', 'ULI', 'ILI'])

print(df.head(7))

"""plt.plot(df['K'],  df['II'],label = 'КД226')
plt.plot(df['N'],  df['II'],label = '1N5619')
plt.plot(df['KC'], df['II'],label = 'KC456')"""

#plt.plot(df['UV'], df['IV'], label='КД226')
#plt.plot(df['US'], df['IS'], label='1N5619')
#plt.plot(df['UC'], df['IC'], label='KC456')

plt.plot(df['ULI'], df['ILI'], label='Светодиод')

plt.xlabel('Напряжение U, В')
#plt.yticks(ticks=df['IS'], labels=df['IS'])

plt.yticks(ticks=df['ILI'], labels=df['ILI'])
plt.ylabel('Ток I, мА')

plt.title('ВАХ для светодиода')

plt.grid()
plt.legend(loc='upper left')


plt.savefig('plot.png')
#fig.savefig('plot.png')