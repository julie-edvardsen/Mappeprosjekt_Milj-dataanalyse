
# Oppgave 2

Åpne API-er er offentlig tilgjengelige grensesnitt som gir tilgang til data eller funksjoner fra et system. I dette tilfelle betyr det at vi kan hente ut miljødata fra forskjellige datasett uten å måtte laste de ned manuelt. Disse API-ene lar oss programmere applikasjonene våre til å automatisk hente ut oppdaterte miljødata direkte fra kildene. 

Vi har funnet to forskjellige miljødatasett fra kaggle.no som vi har valgt å implementere. Kaggle er en nettside hvor dataforskere og utviklere kan hente og dele data for videre bruk i forskning og utviklingsprosjekter.

## Datasett 1
Det første datasettet vi fant er data hvert 10 minutt fra en vindturbin i Tyrkia for hele 2018. Datasettet ligger på rundt 50 000 linjer, og er ikke helt komplett når det mangler data fra noen av dagene. Brukeren bak datasettet har ikke en lisens på kaggle og der er dermed en faktor vi bruker når vi vurderer datasettet, og det står heller ingenting om hvor ofte datasettet vil bli oppdatert. Datafilen er på 2 MB, og er hentet ut med Scada Systems. 

Det andre datasettet vi fant er 

hvorfor valgt datasett

implementering:
vi har brukt kaggle, pd.read csv

hvorfor vi har valgt csv.


# Oppgave 3

## Metoder brukt for å identifisere og håndtere manglende verdier i datasettet

### For å sjekke om det er noen manglende dager sammenlikner koden en fullstendig dato rekke, med den dataen som faktisk finnes i datasettet.
- Bruker pd.to_datetime() for å konvertere strenger til tidsstempel 
- Bruker .dt.date for å hente ut bare dato delen av hver linje, uten klokkeslettene.
- Bruker pd.date_range() for å lage en tidsrekke mellom to datoer (01.01.2011-30.01.2021).
- Bruker difference() for å finne hvilke av datoene som mangler.
- I IF-løkken brukes .empty for å sjekke om resultatet er tomt eller ikke. I utskriften ser vi at det finnes ingen manglede dager.

### For å sjekke om det mangler tidsintervaller i datasettet brukes det en kombinasjon av Pandas, pandasql og list comprehension for å finne eventuelle manglende 15-minutters intervaller. 
- Først konverterer koden datoer til datetime
- Så lager koden en fullstendig tidsrekke med 15-minutters intervaller.
- Videre blir SQL brukt for å sammenlikne den fullstenidige listen med den faktiske dataen. 
- Etter det henter koden de eventuelle manglende verdiene å viser dem i en tabell. Her blir det brukt list comprehension.
- Til slutt skrives resultatet ut om det finnes manglende verdier, og lagrer dem i en ny CSV fil som skal brukes til å lage den fullstendige og riktige datasettet. Antallet som mangler blir også skrevet ut. 

### For å sjekke om det finnes to av samme klokkeslett er det blitt brukt Pandas.
- Først brukes dublicated() for å finne tidspunkter som kommer mer en en gang. Keep=False gjør slik at alle rader som er duplikater blir med.
- .value_counts() brukes til å telle hver gang det kommer dublikater. Så konverteres dataen til en DataFrame med kolonnenavn så det er lett å forstå dataen i den nye csv filen.
- Lagrer til slutt en ny csv fil som skal brukes til å lage det fullstenige og riktige datasettet. 

### For å lage et komplett datasett med manglene, samt uten dublikater, er igjen Pandas brukt.
- Først kombineres den orginale dataen med utflyte verdier. 
    - pd.concat([]) brukes for å slå sammen df_germany og manglende_intervaller.
    - .sort_values('datetime') brukes for å sortere radene i riktig rekkefølge.
    - .reset_index(drop=True) brukes for å fjerne den gamle indeksen
- Så fjernes dublikatene ved å bruke gjennomsnittet 
    - .groupby('datetime) brukes for å gruppere alle radene som har samme tidspunkt.
    - as_index=False brukes for å sørge for at datetime blir en vanlig kolonne.
    - .agg({'MW': 'mean'}) brukes for å finne gjennomsnittet av MW-verdiene ved dublikater, slik at ikke bare en av de eventuelle flere verdiene blir igjen, men gjennomsnittet av de. Det sikrer et mer riktig svar.
- Videre blir det nye datasettet lagret i en ny csv fil som skal brukes videre. 
- Til slutt blir den nye csv filen importert for videre bruk.
    - pd.read_csv blir brukt for importere filen. 
    - print(df_komplett.info()) blir brukt for å se hvordan csv filen ser ut. 

## Bruk av Pandas SQL (sqldf) til datamanipulering sammenliknet med tradisjonelle Pandas-operasjoner

Pandas SQL er enklere når man skal kode mer komplekse "spørringer". Som man for eksempel kan se i kode del 3 i oppgave 3. Dette er mye kortere og mer oversikkelig, samt enklere å lese, enn hvis man skulle gjort det samme med Pandas-operasjoner.

Pandas SQL har også noen begrensninger. Det er ikke optimalt for veldig store datasett, da det er tregere en "normal" Pandas. Og noen få funk  



## Uregelmessigheter man kan forvente å møte på og hvordan de kan bli håndtert







