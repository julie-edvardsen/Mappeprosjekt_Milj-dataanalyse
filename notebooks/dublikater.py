#Her sjekker koden om det er noen dublikater

import pandas as pd
import kagglehub
from pandasql import sqldf

#Laster ned datasettene
pathGermany = kagglehub.dataset_download("l3llff/wind-power")
#Leser inn CSV-filene som DataFrames
df_germany = pd.read_csv(f"{pathGermany}/data.csv")

df_germany['datetime'] = pd.to_datetime(df_germany['dt'], errors='coerce')

duplikater = df_germany[df_germany.duplicated('datetime', keep=False)]
# Sjekker om det finnes noen duplikater
if not duplikater.empty:
    print("Følgende datoer og tidspunkter forekommer flere ganger:")
    duplikater_visning = duplikater[['dt', 'MW']]
    print(duplikater_visning.to_string(index=False))
    # Skriver ut antall gzanger hver duplikat blir funnet på slutten av linjen (i den nye csv filen)
    antall_duplikater = duplikater['datetime'].value_counts().reset_index()
    antall_duplikater.columns = ['datetime', 'Antall forekomster']
    print("\nAntall ganger hvert tidspunkt forekommer:\n")
    print(antall_duplikater.to_string(index=False))
    # Lagrer resultatene i en CSV-fil til bruk senere
    antall_duplikater.to_csv("dupliserte_tidspunkter.csv", index=False)
    print("\nDuplikatene er også lagret i 'dupliserte_tidspunkter.csv'.")
else:
    print("Ingen dupliserte tidspunkter funnet.")

