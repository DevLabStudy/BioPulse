"""
BioPulse Enterprise Core Engine - Advanced Biomedical Data Pipeline
Opis: Uniwersalny silnik walidacji, czyszczenia i eksportu danych biomedycznych.
"""

import csv
import json
from typing import List, Dict, Any

class BioPulseEnterpriseEngine:
    def __init__(self, source_name: str):
        self.source_name = source_name
        self.raw_data: List[Dict[str, Any]] = []
        self.validated_data: List[Dict[str, Any]] = []

    def ingest_biomedical_stream(self) -> None:
        """Pobieranie surowych struktur biomedycznych i danych laboratoryjnych."""
        print(f"[INFO]: Łączenie ze źródłem danych: {self.source_name}...")
        
        # Baza danych oparta na strukturach biologicznych
        self.raw_data = [
            {"id": 201, "kategoria": "Nabłonek", "obiekt": "Wielowarstwowy płaski", "parametr": "Ochrona naskórka", "status": "aktywny"},
            {"id": 202, "kategoria": "Krew", "obiekt": "Erytrocyty", "parametr": "4,5 mln/mm3", "status": "aktywny"},
            {"id": 203, "kategoria": "Krew", "obiekt": "Trombocyty", "parametr": "200-400 tys/mm3", "status": "aktywny"},
            {"id": 204, "kategoria": "Neuron", "obiekt": "Osłonka mielinowa", "parametr": "Lemocyty / Węzły Ranviera", "status": "aktywny"},
            {"id": 205, "kategoria": "Anomalia", "obiekt": "Błąd pomiaru", "parametr": "0", "status": "odrzucony"} # Do odrzucenia
        ]
        print(f"[INFO]: Wczytano surowo {len(self.raw_data)} rekordów.")

    def validate_records(self) -> None:
        """Silnik walidacji odrzucający anomalie i dane niespełniające norm."""
        print("[INFO]: Uruchamianie reguł walidacyjnych BioPulse...")
        passed = 0
        
        for item in self.raw_data:
            if item["status"] == "aktywny" and item["kategoria"] != "Anomalia":
                self.validated_data.append(item)
                passed += 1
            else:
                print(f"[WARNING]: Odrzucono anomalię/błąd ID {item['id']}")
                
        print(f"[INFO]: Walidacja ukończona. Zweryfikowano pomyślnie: {passed}/{len(self.raw_data)}.")

    def export_enterprise_reports(self) -> None:
        """Eksport zweryfikowanych danych do formatów biznesowych (CSV i JSON)."""
        if not self.validated_data:
            print("[ERROR]: Brak danych do eksportu.")
            return

        with open("biopulse_raport.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.validated_data[0].keys())
            writer.writeheader()
            writer.writerows(self.validated_data)

        with open("biopulse_raport.json", "w", encoding="utf-8") as f:
            json.dump(self.validated_data, f, ensure_ascii=False, indent=4)

        print("[SUCCESS]: Wygenerowano raporty analityczne w formacie CSV oraz JSON.")

if __name__ == "__main__":
    print("=== START SILNIKA BIOPULSE ENTERPRISE ===")
    engine = BioPulseEnterpriseEngine(source_name="Biomedical-Data-Pipeline-v2")
    engine.ingest_biomedical_stream()
    engine.validate_records()
    engine.export_enterprise_reports()
    print("=== ZAKOŃCZONO PROCES ===")
