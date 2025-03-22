import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 10),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

plt.style.use('dark_background')

df = pd.read_csv('../input/wind-power/data.csv')
df['dt'] = pd.to_datetime(df['dt'])

# Laster ned nyeste versjonen til datasettet fra Tyskland 
pathGermany = kagglehub.dataset_download("l3llff/wind-power")

print("Path to dataset files:", pathGermany)