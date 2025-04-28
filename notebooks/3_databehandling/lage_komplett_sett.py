import pandas as pd
import kagglehub
from pandasql import sqldf
import os
from pathlib import Path

#Vi vil at csv filen skal ligge i data mappen utenfor notebooks mappen.
BASE_DIR = Path(__file__).parent.parent
out_path = BASE_DIR / "data" / "komplett_data_med_utfylte_mengder.csv"

#Laster ned datasettene
pathGermany = kagglehub.dataset_download("l3llff/wind-power")
#Leser inn CSV-filene som DataFrames
df_germany = pd.read_csv(f"{pathGermany}/data.csv")


#Her finner koden om det mangler 15 min intervaller som mangler 

df_germany['datetime'] = pd.to_datetime(df_germany['dt'], errors='coerce')

#Her brukes list comprehension for å lage intervaller på 15 minutter
alle_intervaller_df = pd.DataFrame({
    'datetime': pd.date_range(start=df_germany['datetime'].min(),
                              end=df_germany['datetime'].max(),
                              freq='15min')
})
#Finner mangler med sql
query = """
    SELECT a.datetime
    FROM alle_intervaller_df a
    LEFT JOIN df_germany b
    ON a.datetime = b.datetime
    WHERE b.datetime IS NULL
"""
manglende_intervaller_df = sqldf(query, locals())

#List comprehension for å legge dataene i en DataFrame, så vi får ut en tabell
manglende_intervaller = [
    {'datetime': tidspunkt, 'MW': None}
    for tidspunkt in manglende_intervaller_df['datetime']
]
manglende_intervaller_df = pd.DataFrame(manglende_intervaller)


#Her lages det en ny csv fil som inneholder det komplette datasettet. Med informasjonen som mangler, samt uten dublikerte tidspunkter. 
#Her sørges det for at begge datarammer har datetime-format (litt krøll med dette tidligere)
df_germany['datetime'] = pd.to_datetime(df_germany['datetime'], errors='coerce')
manglende_intervaller_df['datetime'] = pd.to_datetime(manglende_intervaller_df['datetime'], errors='coerce')

#Kombiner df_germany og de manglende intervallene
df_komplett = pd.concat([df_germany, manglende_intervaller_df])

df_komplett = df_komplett.sort_values('datetime').reset_index(drop=True)
df_komplett = df_komplett.groupby('datetime', as_index=False).agg({'MW': 'mean'})
df_komplett = df_komplett.set_index('datetime')

#fyller inn manglende verdier ved ved bruk av interpolate
df_komplett['MW'] = df_komplett['MW'].interpolate(method='time')

df_komplett = df_komplett.reset_index()


#Lagrer resultatet til en ny csv fil 
df_komplett.to_csv(out_path, index=False)
print(f"Data lagret i {out_path}")

print("Data med utfylte verdier og fjernede duplikater er lagret som 'komplett_data_med_utfylte_mengder.csv'.")

