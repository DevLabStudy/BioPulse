# Architektura Systemu (`main.py`)

Silnik opiera się na wydajnym procesie potokowym (Data Pipeline):
1. **Ingest:** Pobieranie i strumieniowanie danych biomedycznych.
2. **Validate:** Algorytmiczna detekcja anomalii i odrzucanie błędnych rekordów.
3. **Export:** Automatyczne generowanie raportów analitycznych (`.csv` / `.json`).
