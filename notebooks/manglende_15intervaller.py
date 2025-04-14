
import pandas as pd
import kagglehub
from pandasql import sqldf

#Laster ned datasettene
pathGermany = kagglehub.dataset_download("l3llff/wind-power")
#Leser inn CSV-filene som DataFrames
df_germany = pd.read_csv(f"{pathGermany}/data.csv")


#Her finner koden om det mangler 15 min intervaller som mangler 

df_germany['datetime'] = pd.to_datetime(df_germany['dt'], errors='coerce')

# Her brukes list comprehension for å lage intervaller på 15 minutter
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

#Sjekker om det finnes manglende intervaller
if not manglende_intervaller_df.empty:
    print("\nFølgende 15-minutters intervaller mangler:\n")
    print(manglende_intervaller_df.to_string(index=False))
    print(f"\nAntall manglende 15-minutters intervaller: {len(manglende_intervaller_df)}")
    
    #Lagrer resultatene i en CSV-fil
    manglende_intervaller_df.to_csv("manglende_intervaller.csv", index=False)
    print("\nManglende intervaller er også lagret i 'manglende_intervaller.csv'.")
else:
    print("Ingen manglende 15-minutters intervaller")
