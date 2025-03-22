import pandas as pd
import kagglehub
import seaborn as sns
import matplotlib.pyplot as plt


import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 10),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)
plt.style.use('dark_background')

# Last ned datasettet
path = kagglehub.dataset_download("l3llff/wind-power")

# Les inn CSV-filen som en DataFrame
df = pd.read_csv(f"{path}/data.csv")

# Konverter 'dt'-kolonnen til datetime-format
df['dt'] = pd.to_datetime(df['dt'])

# Visualisering
df['month'] = df['dt'].dt.month  # Oppretter en ny kolonne for månedsnummer
f = sns.barplot(data=df.groupby('month').mean().reset_index(), x='month', y='MW')

plt.xlabel('Month')
plt.ylabel('Avg MW')
plt.title('Average generated power by month')
f.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.show()



