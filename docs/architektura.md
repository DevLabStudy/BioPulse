# Architektura Silnika

System opiera się na wydajnym i czystym kodzie w pliku `main.py`. Składa się z trzech niezależnych warstw:

1. **Ingest (Pobieranie):** Bezpieczny nasłuch lub odczyt surowych struktur wejściowych ze źródeł zewnętrznych.
2. **Transform & Validate (Walidacja):** Algorytm sprawdzający poprawność biznesową (np. dodatnie wartości, autoryzacja statusów) oraz odrzucający anomalie.
3. **Export (Generowanie raportów):** Automatyczny zapis przefiltrowanych rekordów do uniwersalnych formatów analitycznych (`.csv` dla standardowych narzędzi biurowych oraz `.json` dla systemów korporacyjnych).
