import pandas as pd
import kagglehub


# Last ned datasettene
pathGermany = kagglehub.dataset_download("l3llff/wind-power")

# Les inn CSV-filene som DataFrames
df_germany = pd.read_csv(f"{pathGermany}/data.csv")


# Sjekk de første radene for å forstå datastrukturen
print("Data fra Tyskland:")
print(df_germany.head())


print("--------------------------------")


# Konverter 'dt'-kolonnen til datetime-format
df_germany['dt'] = pd.to_datetime(df_germany['dt'], errors='coerce')

#Dato og MW fra en spesifikk selvvalgt rad 
print(df_germany.iloc[299959][['dt', 'MW']])


print("--------------------------------")


# Filtrer data for spesifikk dato og tid
target_time = '2015-03-20 05:00:00'
mw_value = df_germany.loc[df_germany['dt'] == target_time, 'MW'].values
# Sjekk om verdien ble funnet
if len(mw_value) > 0:
    print(f"MW-verdien kl. 05:00 den 20.03.2015 er: {mw_value[0]} MW")
else:
    print("Ingen data funnet for denne datoen og klokkeslettet.")


print("--------------------------------")


#Eksempel om jeg vil skrive ut hvor mange ganger MW verdien går under 100:
# Filtrer ut verdier som er under 100
mw_under_100_count = (df_germany['MW'] < 100).sum()
# Vis resultatet
print(f"Antall ganger MW er under 100: {mw_under_100_count}")


print("--------------------------------")


# Filtrer de siste 5000 radene og velg rader der MW < 100
filtered_data = df_germany.iloc[-5000:][df_germany['MW'] < 100][['dt', 'MW']]
# Vis resultatet som en pent formatert tabell
print(filtered_data.to_string(index=False))  # For en ryddig terminalvisning


print("--------------------------------")


#List comprehensions
mw_values = [(row['dt'], row['MW']) for _, row in df_germany.iloc[-5000:].iterrows() if row['MW'] < 100]
# Vis resultatet
print(mw_values)

print("--------------------------------")

#Iritator for å finne første forekomst der MW < 50
chunk_iter = pd.read_csv(f"{pathGermany}/data.csv", chunksize=1000)
# Finn første rad der MW er under 50
for chunk in chunk_iter:
    chunk['dt'] = pd.to_datetime(chunk['dt'], errors='coerce')  # Konverter 'dt' til datetime
    result = chunk[chunk['MW'] < 50]
    if not result.empty:
        print(result[['dt', 'MW']].head(1))
        break  # Stopper når første treff er funnet


print("--------------------------------")

#SQL - inspirert spørring for MW < 100 på spesifikke datoer 
# Filtrer data med Pandas SQL (query)
filtered_data = df_germany.query("MW < 100 and dt >= '2015-03-01' and dt <= '2015-03-31'")
# Vis resultatet
print(filtered_data[['dt', 'MW']])