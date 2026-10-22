"""
BioPulse Core Engine - Biomedical Data Extraction & Validation Pipeline
Autor: Portfolio Inżynieryjne / BioPulse Project
Opis: Silnik walidacji, strukturyzacji i eksportu danych biologicznych 
      (oparty na notatkach: tkanki zwierzęce, nabłonki, mięśnie, krew).
"""

import csv
from typing import List, Dict, Any

class BioPulseEngine:
    def __init__(self, source_name: str):
        self.source_name = source_name
        self.raw_data: List[Dict[str, Any]] = []
        self.validated_data: List[Dict[str, Any]] = []

    def load_biological_database(self) -> None:
        """Wczytywanie ustrukturyzowanej bazy wiedzy o tkankach i składnikach krwi."""
        print(f"[INFO]: Łączenie ze źródłem danych: {self.source_name}...")
        
        # Baza danych bezpośrednio z Twoich notatek z biologii
        self.raw_data = [
            # Tkanka Nabłonkowa
            {
                "kategoria": "Tkanka Nabłonkowa", 
                "obiekt": "Wielowarstwowy płaski", 
                "lokalizacja": "Powierzchnia ciała, naskórek", 
                "funkcja": "Ochronna (przed urazami i wysychaniem)", 
                "status": "aktywny"
            },
            {
                "kategoria": "Tkanka Nabłonkowa", 
                "obiekt": "Jednowarstwowy wielorzędowy", 
                "lokalizacja": "Drogi oddechowe", 
                "funkcja": "Usuwanie zanieczyszczeń rzęskami", 
                "status": "aktywny"
            },
            {
                "kategoria": "Tkanka Nabłonkowa", 
                "obiekt": "Jednowarstwowy walcowaty", 
                "lokalizacja": "Żołądek, jelito cienkie", 
                "funkcja": "Wchłanianie i wydzielanie", 
                "status": "aktywny"
            },
            {
                "kategoria": "Tkanka Nabłonkowa", 
                "obiekt": "Jednowarstwowy sześcienny", 
                "lokalizacja": "Przewody gruczołowe, kanaliki nerkowe", 
                "funkcja": "Wchłanianie i wydzielanie", 
                "status": "aktywny"
            },
            {
                "kategoria": "Tkanka Nabłonkowa", 
                "obiekt": "Jednowarstwowy płaski", 
                "lokalizacja": "Pęcherzyki płucne, ściany naczyń", 
                "funkcja": "Transport i wymiana gazowa", 
                "status": "aktywny"
            },
            
            # Tkanka Mięśniowa[cite: 1]
            {
                "kategoria": "Tkanka Mięśniowa", 
                "obiekt": "Poprzecznie prążkowana szkieletowa", 
                "lokalizacja": "Mięśnie szkieletowe", 
                "funkcja": "Praca zależna od woli, silna i szybka", 
                "status": "aktywny"
            },
            {
                "kategoria": "Tkanka Mięśniowa", 
                "obiekt": "Poprzecznie prążkowana serca", 
                "lokalizacja": "Serce", 
                "funkcja": "Praca niezależna od woli, odporna na zmęczenie", 
                "status": "aktywny"
            },
            {
                "kategoria": "Tkanka Mięśniowa", 
                "obiekt": "Gładka", 
                "lokalizacja": "Ściany narządów wewnętrznych (żołądek, jelita)", 
                "funkcja": "Powolne, długotrwałe skurcze niezależne od woli", 
                "status": "aktywny"
            },

            # Tkanka Łączna Płynna (Krew)[cite: 1]
            {
                "kategoria": "Tkanka Łączna Płynna", 
                "obiekt": "Osocze (Plasma)", 
                "lokalizacja": "Krew (ok. 55% objętości)", 
                "funkcja": "Transport składników odżywczych, hormonów i odpadów", 
                "status": "aktywny"
            },
            {
                "kategoria": "Tkanka Łączna Płynna", 
                "obiekt": "Erytrocyty (Krwinki czerwone)", 
                "lokalizacja": "Krew (4,5 mln/mm3)", 
                "funkcja": "Transport tlenu (O2) i częściowo CO2", 
                "status": "aktywny"
            },
            {
                "kategoria": "Tkanka Łączna Płynna", 
                "obiekt": "Trombocyty (Płytki krwi)", 
                "lokalizacja": "Krew (200-400 tys./mm3)", 
                "funkcja": "Uczestniczą w procesie krzepnięcia krwi", 
                "status": "aktywny"
            },
            {
                "kategoria": "Tkanka Łączna Płynna", 
                "obiekt": "Leukocyty (Krwinki białe)", 
                "lokalizacja": "Krew (4-10 tys./mm3)", 
                "funkcja": "Ochrona organizmu i reakcje odpornościowe", 
                "status": "aktywny"
            },

            # Rekord testowy do odrzucenia przez silnik walidacji
            {
                "kategoria": "Błąd", 
                "obiekt": "Anomalia testowa", 
                "lokalizacja": "Nieznana", 
                "funkcja": "Brak", 
                "status": "odrzucony"
            }
        ]
        print(f"[INFO]: Wczytano łącznie {len(self.raw_data)} rekordów z bazy wiedzy.")

    def validate_and_filter(self) -> None:
        """Silnik walidacji odrzucający anomalie i sprawdzający poprawność struktury[cite: 1]."""
        print("[INFO]: Uruchamiam system walidacji reguł biologicznych...")
        valid_count = 0
        
        for item in self.raw_data:
            # Reguła biznesowo-medyczna: przepuszczamy tylko rekordy ze statusem 'aktywny'
            if item["status"] == "aktywny" and item["kategoria"] != "Błąd":
                self.validated_data.append(item)
                valid_count += 1
            else:
                print(f"[WARNING]: Wykryto i odrzucono anomalię/błąd: {item['obiekt']}")
                
        print(f"[INFO]: Walidacja zakończona. Pomyślnie zweryfikowano: {valid_count}/{len(self.raw_data)} rekordów.")

    def export_to_csv(self, filename: str) -> None:
        """Eksport zweryfikowanych danych strukturalnych do pliku CSV."""
        if not self.validated_data:
            print("[ERROR]: Brak danych do eksportu.")
            return

        keys = self.validated_data[0].keys()
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                for row in self.validated_data:
                    writer.writerow(row)
            print(f"[SUCCESS]: Wyeksportowano czystą bazę wiedzy do pliku '{filename}'.")
        except Exception as e:
            print(f"[ERROR]: Nie udało się zapisać pliku CSV: {e}")

if __name__ == "__main__":
    print("=== START SILNIKA BIOPULSE (MODUŁ BIOLOGICZNY) ===")
    
    # Inicjalizacja silnika dla bazy notatek
    engine = BioPulseEngine(source_name="Notatki-Biologia-Tkanki-Zwierzece")
    engine.load_biological_database()
    engine.validate_and_filter()
    engine.export_to_csv("baza_tkanki_zwierzece.csv")
    
    print("=== ZAKOŃCZONO PROCES ==-\n")
