#Michael Agaby's coding challange

import pandas as pd
import seaborn as sns
sns.set()

df = pd.read_csv('https://raw.githubusercontent.com/McGillAISociety/mais-202-coding-challenge/master/data.csv')

intRates = df.groupby(df['purpose']).int_rate.mean()
intRates = intRates.reset_index()

fig = sns.barplot(data = intRates,x = 'purpose', y = 'int_rate')
fig.set_xticklabels(fig.get_xticklabels(),rotation = 90)
fig.set(ylabel = 'mean(int_rate)')

print(intRates.to_string(justify = 'right'))

