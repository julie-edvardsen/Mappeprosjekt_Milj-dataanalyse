import json

# Åpne og les JSON-filen
with open("./src/globale_avvik.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)

# Hent datasettet fra JSON-strukturen
dataset = data["DataSet"]

# Ekstraher år og temperaturavvik
år = [int(item['År']) for item in dataset]
verdi = [float(item['Value']) for item in dataset]

# Beregn gjennomsnittlig temperaturavvik
gjennomsnitt = sum(verdi) / len(verdi)

# Finn året med høyest temperaturavvik
maks_avvik = max(verdi)
maks_år = år[verdi.index(maks_avvik)]

# Finn året med lavest temperaturavvik
min_avvik = min(verdi)
min_år = år[verdi.index(min_avvik)]

# Resultater
print(f"Gjennomsnittlig temperaturavvik: {gjennomsnitt:.2f} grader Celsius")
print(f"Året med høyest temperaturavvik: {maks_år} ({maks_avvik:.2f} grader Celsius)")
print(f"Året med lavest temperaturavvik: {min_år} ({min_avvik:.2f} grader Celsius)")

