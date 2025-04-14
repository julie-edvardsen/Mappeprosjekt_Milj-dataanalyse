import pandas as pd
import kagglehub
from pandasql import sqldf

#Laster ned datasettene
pathGermany = kagglehub.dataset_download("l3llff/wind-power")
#Leser inn CSV-filene som DataFrames
df_germany = pd.read_csv(f"{pathGermany}/data.csv")


#Undersøker om det finnes manglede dager

df_germany['dt'] = pd.to_datetime(df_germany['dt'], errors='coerce')

df_germany['d'] = df_germany['dt'].dt.date

alle_dager = pd.date_range(start=df_germany['d'].min(), end=df_germany['d'].max(), freq='d')
manglende_dager = alle_dager.difference(df_germany['d'])


if not manglende_dager.empty: #Hvis den ikke er tom så skriv:
    print(f"Følgende dager mangler: {manglende_dager}")
else: #Om den er tom så skriv:
    print("Ingen manglende dager")



