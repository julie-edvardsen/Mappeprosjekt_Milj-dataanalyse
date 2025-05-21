# Her må vi lage unittester for å teste at oppgave 2 og 3 fungerer

import unittest
import pandas as pd

def finn_duplikater(df):
    df['datetime'] = pd.to_datetime(df['dt'], errors='coerce')
    duplikater = df[df.duplicated('datetime', keep=False)]

    if not duplikater.empty:
        antall_duplikater = duplikater['datetime'].value_counts().reset_index()
        antall_duplikater.columns = ['datetime', 'Antall forekomster']
        return antall_duplikater
    else:
        return None
    

class TestDuplikatsjekk(unittest.TestCase):
    def test_finner_duplikater(self):
        # Lager en liten test-DataFrame med duplikater
        data = {
            'dt': ['2023-01-01 00:00', '2023-01-01 00:00', '2023-01-01 01:00'],
            'MW': [10, 12, 14]
        }
        df = pd.DataFrame(data)

        resultat = finn_duplikater(df)
        self.assertIsNotNone(resultat)
        self.assertEqual(resultat.iloc[0]['Antall forekomster'], 2)

    def test_ingen_duplikater(self):
        # Data uten duplikater
        data = {
            'dt': ['2023-01-01 00:00', '2023-01-01 01:00'],
            'MW': [10, 12]
        }
        df = pd.DataFrame(data)

        resultat = finn_duplikater(df)
        self.assertIsNone(resultat)

if __name__ == '__main__':
    unittest.main()