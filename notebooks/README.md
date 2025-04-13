
# Oppgave 2

Åpne API-er er offentlig tilgjengelige grensesnitt som gir tilgang til data eller funksjoner fra et system. I dette tilfelle betyr det at vi kan hente ut miljødata fra forskjellige datasett uten å måtte laste de ned manuelt. Disse API-ene lar oss programmere applikasjonene våre til å automatisk hente ut oppdaterte miljødata direkte fra kildene. 

Vi har funnet to forskjellige miljødatasett fra nettsiden til Kaggle som vi har valgt å implementere. Kaggle er en nettside hvor dataforskere og utviklere kan hente og dele data for videre bruk i forskning og utviklingsprosjekter. https://www.kaggle.com/datasets 

### Datasett 1
Det første datasettet vi fant er data hvert 10 minutt fra en vindturbin i Tyrkia for hele 2018. Datasettet ligger på rundt 50 000 linjer, består av f.eks. vindhastighet, vindretning og generert energi. Datasettet er ikke helt komplett når det mangler data fra noen av dagene. Brukeren bak datasettet har ikke en lisens på kaggle og der er dermed en faktor vi bruker når vi vurderer datasettet, og det står heller ingenting om hvor ofte datasettet vil bli oppdatert. Datafilen er en csv fil på 2 MB, og er hentet ut med Scada Systems. Brukervennligheten er også realtivt lav når den ligger på 5.88. Dataene er lett å hente ut og inne på kaggle står det akkurtatt hva datafilen består av. 

Link til datasett: https://www.kaggle.com/datasets/berkerisen/wind-turbine-scada-dataset/data 

### Datasett 2
Det andre datasettet vi fant består av omfattende verdier fra vindkraftproduksjon i Tyskland hvert 15. minutt fra 2011 til 2020. Datasettet ligger på litt under 400 000 linjer, og har brukervennlighet 10.0 på kaggle. Det betyr at den er lett å bruke/forstå. Datafilen er en csv fil, på 10,5 MB og den vil bli oppdatert ukentlig. Datasettet er ikke komplett når det er feil og mangler i noen av linjene. Brukeren bak datasettet er lisensert fra CC0: Public Domain, denne lisensen har ingen copyright regler slik at vi kan kopiere, modifiserer og bruk dataene slik vi vil. Les mer om lisensen her: https://creativecommons.org/publicdomain/zero/1.0/ 

Link til datasett: https://www.kaggle.com/datasets/l3llff/wind-power/data 

### Valg av datasett
Etter å ha vurdert begge datasettene grundig, har vi valgt å gå videre med datasett 2 om vindkraftproduksjon i Tyskland. Vurderingene vi tok i betrakning var troverdighet til forfatteren/brukeren bak datasettet, om datasettet var komplett eller hadde feil og mangler som vi kunne filtrere ut og håndtere. Vi så også på hvor store filene var og ønsket å gå videre med en større fil for å gjøre det vanskeligere for oss selv og vise forståelse. Datasett 2 fylte også flere av kravene vi selv hadde sett for oss at vi skulle gå videre med i prosjektet. 


### Implementering
For å implementere datasettene har vi brukt ulike funksjoner i Python. 
- Pandas er et python bibliotek som vi har brukt til å analysere, behandle og manipulere dataene. Det er en veldig fin metode å bruke med tallbaserte data som csv-filer. 
- Kagglehub er en pakke vi har brukt for å laste ned datasett dirkete fra Kaggle til Python. Kagglehub forenkler tilgangen vår til datasettet slik at vi slipper å laste ned data manuelt fra siden. Den brukes sammen med en API-nøkkel fra Kaggle for autentisering. 
- .dataset_download er en funksjon fra kagglehub pakken vi har brukt for å få datafilene inn i prosjektet vårt. 
- pd.read_csv er en funksjon fra pandas som vi har brukt til å kunne lese csv filen og lage dataframes av det. 
- Errors = 'coerce', dette har vi brukt for å kunne lese tomme/feil i linejene. Det vil da bli printet Not a Time i stedenfor at koden krasjer. 
- .iloc har vi brukt for å hente ut rader og kolonner basert på posisjon i datasettet. 
- .loc gjør det samme som .iloc bare basert på etiketter/navn og ikke posisjon i datasettet.
- .iterrows() har vi brukt når vi vill gå gjennom datasettetet en linje om gangen for å finne de linjene som har bestemte betingelser.
- chunksize = 1000 har vi brukt for å dele opp datasettet i mindre "deler" når den blir lest igjennom i stedet for alle 400 000 på en gang. 
- .query() har vi brukt for å kunne skrive inn de utrykkene/betingelsene vi vil ha som filtrerer ut linjene i datasettet. 

### Valg av csv
Vi har valgt å bruke csv filer av flere grunner. Csv filer er enklere for oss å lese/forstå, de samarbeider ekstremt godt med pandas og dataframes når de er laget for datasett med rader og kolonner. Csv filer støttes nesten av alle dataverktøy som gjør de ekstremt fleksible i for eksempel python og excel. Når vi lette etter datafiler å bruke fant vi hovedsakelig flest csv filer og valgte på grunn av alt dette å gå videre med csv. 



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

Pandas SQL er enklere når man skal kode mer komplekse "spørringer". Som man for eksempel kan se i kode-del 3 i oppgave 3. Dette blir mye kortere, mer oversikkelig, samt enklere å lese, enn hvis man skulle gjort det samme med Pandas-operasjoner.

Pandas SQL har også noen begrensninger. Det er ikke optimalt for veldig store datasett, da det er tregere en "normal" Pandas. Og noen få funksjoner i Pandas, som for eksempel; .resample(), .pivot() og .rolling(), finnes ikke i SQL.

Man burde bruke SQL om man kjenner det godt fra før, jobber med mange sammenslåtte tabeller, eller om datasettet er litt mindre. Man burde bruke 'vanlig' pandas om man jobber med store datasett(flere millioner av rader), eller om man trenger veldig kraftige tidsseriefunksjoner.


## Uregelmessigheter man kan forvente å møte på og hvordan de kan bli håndtert

Vi forventer å møte på uregelmessigheter som manglende/ugyldige MW-verdier, feil med tidssone/tid-konvertering, og eventuelle overflødlige kolonner. I oppgave 3 har vi allerede funnet og fjernet dublikater, og identifisert manglende tidsintervaller og fylt de inn med gjenomsnittet av MW-verdiene som er i radene over og under. 



# Oppgave 4

## Håndtering av eventuelle skjevheter i dataen under videre analyse

Tidligere har det blitt gjennomført en grunndig datarensing. Dette innebærer å identifisere og håndtere manglende verdier, og fjerne dublikater som kan påvirke analysen senere. For å sikre at analysen er pålitelig vil statistiske mål som median, gjennomsnitt og standaravvik bli brukt. Dette vil gi et mer realistisk bilde av datastrukturen. Ulike perioder og segmenter i datasettet vil også bli sammenliknet for å se om dataen er konsistent. 
 
## Planlagte visualiseringer for å støtte analysen

For å støtte analysen vil linjediagram, søylediagram og boksplott bli brukt for ulike visualiseringer. Linjediagram brukes for å vise utviklingen i kraftprodukjsonen over tid. Denne type diagram er best for å vise forskjellen mellom to perioder. Søylediagram brukes for å sammenlikne totalprodukjsonen mellom forskjellige perioder. Denne er best hvis man vil se hvilke månder/år som produserer mest kraft, som gjør det enklere å trekke raske konklusjoner. Boksplott brukes for å analysere spredningen i dataene. Boksplott er fint å bruke når man vil vurdere stabiliteten i kraft produkjsonen. 

# Oppgave 5 - Visualisering av miljødata

# Oppgave 6 - Prediktiv analyse

# Refleksjonsnotat av prosjektet

I dette prosjektet har vi utforsket ulike metoder og funksjoner som innebærer i bruk av API-er, databehandling, dataanalyse og visualisering. 

Vurderingskriterier:

- Refleksjoner over hva du har lært om datainnsamling, databehandling, dataanalyse og visualisering.
- Beskrivelse av nye ferdigheter som ble tilegnet, for eksempel bruk av spesifikke biblioteker (Pandas, NumPy, Matplotlib, etc.) og programmeringskonsepter.
- Identifisering av spesifikke utfordringer som oppstod under prosjektet, for eksempel problemer med datakvalitet, håndtering av manglende verdier, eller tekniske problemer med API-er.
- Refleksjoner over samarbeidet i gruppen, inkludert hvordan oppgaver ble fordelt og hvordan kommunikasjonen fungerte.
- Vurdering av de endelige resultatene, inkludert kvaliteten på visualiseringene og analysene.
- Ideer til hvordan prosjektet kan forbedres i fremtiden, både i forhold til tekniske aspekter og prosjektledelse.
- Mulige retninger for videre forskning eller utvikling basert på erfaringene fra prosjektet.
- Oppsummering av de viktigste læringspunktene og hvordan prosjektet har bidratt til studentenes forståelse av datavitenskap og miljøstudier.
- Personlige tanker om hvordan erfaringene fra prosjektet kan anvendes i fremtidige studier eller yrkesliv.