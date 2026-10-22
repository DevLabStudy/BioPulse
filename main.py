"""
BioPulse Enterprise Core Engine
Opis: Uniwersalny silnik walidacji i transformacji danych dla firm (od małych po korporacje).
"""

import csv
import json
from typing import List, Dict, Any

class BioPulseEngine:
    def __init__(self, source_name: str):
        self.source_name = source_name
        self.raw_data: List[Dict[str, Any]] = []
        self.clean_data: List[Dict[str, Any]] = []

    def ingest_stream(self) -> None:
        """Pobieranie surowych danych wejściowych ze strumienia lub pliku."""
        print(f"[INFO]: Łączenie ze źródłem danych: {self.source_name}...")
        
        # Przykładowe dane transakcyjne / systemowe wymagające walidacji
        self.raw_data = [
            {"id": 1001, "klient": "Partner A", "wartosc": 2500.00, "status": "aktywny"},
            {"id": 1002, "klient": "Partner B", "wartosc": -150.00, "status": "błąd"}, # Anomalia do odrzucenia
            {"id": 1003, "klient": "Partner C", "wartosc": 5400.20, "status": "aktywny"},
            {"id": 1004, "klient": "Partner D", "wartosc": 0.00, "status": "nieaktywny"}  # Nieaktywny do odrzucenia
        ]
        print(f"[INFO]: Wczytano {len(self.raw_data)} rekordów.")

    def validate_and_filter(self) -> None:
        """Silnik walidacji reguł biznesowych – odsiewa błędy i anomalie."""
        print("[INFO]: Uruchamianie reguł walidacyjnych...")
        passed = 0
        
        for item in self.raw_data:
            if item["wartosc"] > 0 and item["status"] == "aktywny":
                self.clean_data.append(item)
                passed += 1
            else:
                print(f"[WARNING]: Odrzucono niepoprawny rekord ID {item['id']}")
                
        print(f"[INFO]: Walidacja zakończona. Przepuszczono poprawnych: {passed}/{len(self.raw_data)}.")

    def export_reports(self) -> None:
        """Eksport zweryfikowanych danych do formatów biznesowych (CSV i JSON)."""
        if not self.clean_data:
            print("[ERROR]: Brak danych do eksportu.")
            return

        # Format CSV (idealny dla lokalnych biznesów / Excela)
        with open("biopulse_raport.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.clean_data[0].keys())
            writer.writeheader()
            writer.writerows(self.clean_data)

        # Format JSON (idealny dla dużych systemów i API korporacyjnych)
        with open("biopulse_raport.json", "w", encoding="utf-8") as f:
            json.dump(self.clean_data, f, ensure_ascii=False, indent=4)

        print("[SUCCESS]: Wygenerowano raporty biznesowe (CSV oraz JSON).")

if __name__ == "__main__":
    print("=== START SYSTEMU BIOPULSE ENTERPRISE ===")
    engine = BioPulseEngine(source_name="Enterprise-Data-Stream-v1")
    engine.ingest_stream()
    engine.validate_and_filter()
    engine.export_reports()
    print("=== PROCES ZAKOŃCZONY POMYŚLNIE ===")
