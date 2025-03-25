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

# Sjekk datatype for å unngå duplikatkolonner
print(df.dtypes)

# Konverter 'dt' til datetime-format
df['dt'] = pd.to_datetime(df['dt'], errors='coerce')

# Opprett en ny kolonne for årstall
df['year'] = df['dt'].dt.year  

# Visualisering
g = sns.barplot(data=df.groupby('year').mean().reset_index(), x='year', y='MW', color='#ffb6c1')
plt.xlabel('Year')
plt.ylabel('Avg MW')
plt.title('Average generated power by year')
plt.show()
