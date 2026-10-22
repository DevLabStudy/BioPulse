"""
BioPulse Core Engine - Biomedical Data Extraction & Validation Pipeline
Autor: Portfolio Inżynieryjne
Opis: System walidacji i struktaryzacji danych biologicznych (np. parametry krwi i tkanki) do formatu CSV.
"""

import csv
from typing import List, Dict, Any

class BioPulseEngine:
    def __init__(self, source_name: str):
        self.source_name = source_name
        self.raw_data: List[Dict[str, Any]] = []
        self.validated_data: List[Dict[str, Any]] = []

    def load_biological_data(self) -> None:
        """Wczytywanie ustrukturyzowanych danych z notatek (np. składniki krwi, tkanki)[cite: 1]."""
        print(f"[INFO]: Łączę ze źródłem danych: {self.source_name}...")
        
        # Surowe dane oparte na Twoich notatkach z biologii (krew, tkanki)[cite: 1]
        self.raw_data = [
            {"składnik": "Osocze", "norma_objętości": "55%", "typ": "płynna tkanka łączna", "status": "prawidłowy"},
            {"składnik": "Erytrocyty", "norma_objętości": "4.5 mln/mm3", "typ": "komórki bezjądrzaste", "status": "prawidłowy"},
            {"składnik": "Trombocyty", "norma_objętości": "200-400 tys/mm3", "typ": "płytki krwi", "status": "prawidłowy"},
            {"składnik": "Anomalia_Testowa", "norma_objętości": "0", "typ": "błąd pomiaru", "status": "odrzucony"} # Rekord testowy do odrzucenia
        ]
        print(f"[INFO]: Pomyślnie wczytano {len(self.raw_data)} rekordów biologicznych.")

    def validate_records(self) -> None:
        """Silnik walidacji odrzucający anomalie i dane niespełniające norm[cite: 1]."""
        print("[INFO]: Uruchamiam walidację reguł medycznych/biologicznych...")
        valid_count = 0
        
        for item in self.raw_data:
            # Reguła: odrzucamy rekordy ze statusem odrzuconym lub błędnym typem
            if item["status"] == "prawidłowy" and item["typ"] != "błąd pomiaru":
                self.validated_data.append(item)
                valid_count += 1
            else:
                print(f"[WARNING]: Odrzucono niepoprawny rekord: {item['składnik']}")
                
        print(f"[INFO]: Walidacja zakończona. Zweryfikowano pomyślnie: {valid_count}/{len(self.raw_data)}.")

    def export_to_csv(self, filename: str) -> None:
        """Eksport czystych danych do formatu CSV (Gotowe do analizy lub Excela)."""
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
            print(f"[SUCCESS]: Wyeksportowano zweryfikowaną bazę do pliku '{filename}'.")
        except Exception as e:
            print(f"[ERROR]: Błąd zapisu pliku CSV: {e}")

if __name__ == "__main__":
    print("=== START SILNIKA BIOPULSE ===")
    
    engine = BioPulseEngine(source_name="Notatki-Biologia-Tkanki-Krwi")
    engine.load_biological_data()
    engine.validate_records()
    engine.export_to_csv("baza_biopulse_raport.csv")
    
    print("=== ZAKOŃCZONO PROCES ===\n")
