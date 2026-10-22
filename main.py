"""
BioPulse Enterprise Core Engine - Production-Grade Data Pipeline
Opis: Komercyjny silnik walidacji, wykrywania anomalii i eksportu strumieni danych biznesowych.
"""

import csv
import json
import logging
from typing import List, Dict, Any

# Konfiguracja profesjonalnego logowania korporacyjnego
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class EnterpriseDataPipeline:
    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        self.raw_stream: List[Dict[str, Any]] = []
        self.validated_records: List[Dict[str, Any]] = []
        self.anomalies_detected: List[Dict[str, Any]] = []

    def ingest_stream(self) -> None:
        """Etap 1: Pobieranie surowego strumienia danych (np. transakcje e-commerce / API)."""
        logging.info(f"Inicjalizacja strumienia danych dla pipeline: {self.pipeline_id}")
        
        # Symulacja wejściowego strumienia danych z zewnętrznych systemów klienta
        self.raw_stream = [
            {"transaction_id": "TRX-9001", "client": "Global Logistics Corp", "amount": 45000.00, "currency": "USD", "status": "active"},
            {"transaction_id": "TRX-9002", "client": "SMB Retail Shop", "amount": -1200.50, "currency": "EUR", "status": "flagged"}, # Anomalia (ujemna kwota)
            {"transaction_id": "TRX-9003", "client": "FinTech Partner X", "amount": 125000.00, "currency": "USD", "status": "active"},
            {"transaction_id": "TRX-9004", "client": "Local Vendor Y", "amount": 0.00, "currency": "PLN", "status": "inactive"}, # Pusta transakcja
            {"transaction_id": "TRX-9005", "client": "Enterprise Cloud Ltd", "amount": 89000.00, "currency": "GBP", "status": "active"}
        ]
        logging.info(f"Pomyślnie pobrano {len(self.raw_stream)} rekordów ze źródła.")

    def process_and_validate(self) -> None:
        """Etap 2: Rygorystyczna walidacja reguł biznesowych i wykrywanie oszustw/błędów."""
        logging.info("Uruchamianie silnika walidacji reguł biznesowych i detekcji anomalii...")
        
        for item in self.raw_stream:
            # Reguły biznesowe: kwota > 0 oraz status 'active'
            if item["amount"] > 0 and item["status"] == "active":
                self.validated_records.append(item)
            else:
                logging.warning(f"Odrzucono anomalny rekord [{item['transaction_id']}]: Klient {item['client']}")
                self.anomalies_detected.append(item)
                
        logging.info(f"Walidacja zakończona. Przepuszczono: {len(self.validated_records)}, Odrzucono anomalii: {len(self.anomalies_detected)}.")

    def export_reports(self) -> None:
        """Etap 3: Eksport zweryfikowanych danych do systemów zewnętrznych (CSV / JSON API)."""
        if not self.validated_records:
            logging.error("Brak zweryfikowanych danych do eksportu.")
            return

        # Eksport do CSV (dla tradycyjnych systemów / analityków)
        csv_filename = "biopulse_enterprise_report.csv"
        with open(csv_filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.validated_records[0].keys())
            writer.writeheader()
            writer.writerows(self.validated_records)

        # Eksport do JSON (dla mikroserwisów i korporacyjnego API)
        json_filename = "biopulse_enterprise_report.json"
        with open(json_filename, "w", encoding="utf-8") as f:
            json.dump(self.validated_records, f, ensure_ascii=False, indent=4)

        logging.info(f"Wygenerowano raporty komercyjne: {csv_filename}, {json_filename}")

if __name__ == "__main__":
    print("=== START SYSTEMU BIOPULSE ENTERPRISE ===")
    pipeline = EnterpriseDataPipeline(pipeline_id="Prod-Cluster-US-East")
    pipeline.ingest_stream()
    pipeline.process_and_validate()
    pipeline.export_reports()
    print("=== PROCES ZAKOŃCZONY POMYŚLNIE ===")
