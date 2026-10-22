"""
BioPulse Core Engine - Data Extraction & Validation Pipeline
Autor: Twoje Imię / Portfolio Projektowe
Opis: Moduł odpowiedzialny za bezpieczne wczytywanie, walidację i eksport danych strukturalnych.
"""

import csv
import sys
from typing import List, Dict, Any

class BioPulseEngine:
    def __init__(self, source_name: str):
        self.source_name = source_name
        self.raw_data: List[Dict[str, Any]] = []
        self.validated_data: List[Dict[str, Any]] = []

    def load_mock_data(self) -> None:
        """Symulacja wczytywania surowych danych z zewnętrznego źródła/pliku."""
        print(f"[INFO]: Łączenie ze źródłem danych: {self.source_name}...")
        # Przykładowe surowe dane biznesowe/analityczne wymagające walidacji
        self.raw_data = [
            {"id": 1, "kategoria": "Produkt A", "wartosc": 150.5, "status": "aktywny"},
            {"id": 2, "kategoria": "Produkt B", "wartosc": -20.0, "status": "bledny"}, # Anomalia do odrzucenia
            {"id": 3, "kategoria": "Produkt C", "wartosc": 300.0, "status": "aktywny"},
            {"id": 4, "kategoria": "Produkt D", "wartosc": 0.0, "status": "nieaktywny"}
        ]
        print(f"[INFO]: Pomyślnie wczytano {len(self.raw_data)} surowych rekordów.")

    def validate_and_process(self) -> None:
        """Silnik walidacji: odrzuca niepoprawne dane, przetwarza zdrowe rekordy."""
        print("[INFO]: Uruchamianie silnika walidacji reguł biznesowych...")
        valid_count = 0
        
        for item in self.raw_data:
            # Reguła biznesowa: wartość musi być większa od 0, a status aktywny
            if item["wartosc"] > 0 and item["status"] == "aktywny":
                self.validated_data.append(item)
                valid_count += 1
            else:
                print(f"[WARNING]: Odrzucono rekord ID {item['id']} z powodu niespełnienia norm.")
                
        print(f"[INFO]: Walidacja zakończona. Przetworzono poprawnie: {valid_count}/{len(self.raw_data)} rekordów.")

    def export_to_csv(self, filename: str) -> None:
        """Eksport zweryfikowanych danych do formatu CSV (Gotowe dla biznesu/Excela)."""
        if not self.validated_data:
            print("[ERROR]: Brak zweryfikowanych danych do eksportu.")
            return

        keys = self.validated_data[0].keys()
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as output_file:
                writer = csv.DictWriter(output_file, fieldnames=keys)
                writer.writeheader()
                for row in self.validated_data:
                    writer.writerow(row)
            print(f"[SUCCESS]: Pomyślnie wyeksportowano raport do pliku '{filename}'.")
        except Exception as e:
            print(f"[ERROR]: Nie udało się zapisać pliku CSV: {e}")

if __name__ == "__main__":
    print("=== START SYSTEMU BIOPULSE ===")
    
    # Inicjalizacja silnika dla przykładowego strumienia danych
    engine = BioPulseEngine(source_name="Stream-Data-API-v1")
    engine.load_mock_data()
    engine.validate_and_process()
    engine.export_to_csv("raport_biznesowy.csv")
    
    print("=== ZAKOŃCZONO DZIAŁANIE PROGRAMU ===")
