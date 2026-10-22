"""
BioPulse Core Engine - Ultimate Biomedical Exporter
Opis: Konwertuje pełną bazę wiedzy z notatek biologicznych (tkanki, krew, neuron) na plik JSON dla portfolio[cite: 1, 4].
"""

import json

class BioPulseEngine:
    def __init__(self):
        self.knowledge_base = []

    def build_database(self):
        """Pobiera kompletne dane z notatek i rysunków biologicznych[cite: 1, 4]."""
        self.knowledge_base = [
            # --- TKANKA NABŁONKOWA ---
            {
                "id": 1,
                "kategoria": "Tkanka Nabłonkowa",
                "nazwa": "Wielowarstwowy płaski",
                "lokalizacja": "Powierzchnia ciała, naskórek",
                "budowa": "Wiele warstw komórek, spłaszczających się ku powierzchni[cite: 1, 2]",
                "funkcja": "Głównie ochronna (przed urazami i wysychaniem)[cite: 1]"
            },
            {
                "id": 2,
                "kategoria": "Tkanka Nabłonkowa",
                "nazwa": "Jednowarstwowy wielorzędowy",
                "lokalizacja": "Drogi oddechowe",
                "budowa": "Komórki o różnej wysokości, wyposażone w rzęski[cite: 1, 2]",
                "funkcja": "Usuwanie zanieczyszczeń za pomocą rzęsek[cite: 1]"
            },
            {
                "id": 3,
                "kategoria": "Tkanka Nabłonkowa",
                "nazwa": "Jednowarstwowy walcowaty",
                "lokalizacja": "Żołądek, jelito cienkie[cite: 1, 2]",
                "budowa": "Wysokie komórki, często z mikrokosmkami[cite: 1, 2]",
                "funkcja": "Wchłanianie i wydzielanie substancji[cite: 1]"
            },
            {
                "id": 4,
                "kategoria": "Tkanka Nabłonkowa",
                "nazwa": "Jednowarstwowy sześcienny",
                "lokalizacja": "Przewody gruczołowe, kanaliki nerkowe[cite: 1, 2]",
                "budowa": "Komórki w kształcie sześcianów[cite: 1, 2]",
                "funkcja": "Wchłanianie i wydzielanie[cite: 1]"
            },
            {
                "id": 5,
                "kategoria": "Tkanka Nabłonkowa",
                "nazwa": "Jednowarstwowy płaski",
                "lokalizacja": "Pęcherzyki płucne, ściany naczyń[cite: 1, 2]",
                "budowa": "Płaskie komórki umożliwiające dyfuzję[cite: 1, 2]",
                "funkcja": "Transport i wymiana substancji (np. gazów)[cite: 1]"
            },

            # --- TKANKA MIĘŚNIOWA ---
            {
                "id": 6,
                "kategoria": "Tkanka Mięśniowa",
                "nazwa": "Poprzecznie prążkowana szkieletowa",
                "lokalizacja": "Mięśnie szkieletowe[cite: 1]",
                "budowa": "Długie, cylindryczne, wielojądrzyste włókna z widocznym prążkowaniem[cite: 1]",
                "funkcja": "Praca zależna od woli, silna i szybka[cite: 1]"
            },
            {
                "id": 7,
                "kategoria": "Tkanka Mięśniowa",
                "nazwa": "Poprzecznie prążkowana serca",
                "lokalizacja": "Serce[cite: 1]",
                "budowa": "Komórki widlasto rozgałęzione, połączone wstawkami, 1-2 jądra[cite: 1]",
                "funkcja": "Praca niezależna od woli, odporna na zmęczenie[cite: 1]"
            },
            {
                "id": 8,
                "kategoria": "Tkanka Mięśniowa",
                "nazwa": "Gładka",
                "lokalizacja": "Ściany narządów wewnętrznych (żołądek, jelita)[cite: 1]",
                "budowa": "Wrzecionowate komórki bez prążkowania, jedno jądro centralne[cite: 1]",
                "funkcja": "Powolne, długotrwałe skurcze niezależne od woli[cite: 1]"
            },

            # --- TKANKA ŁĄCZNA PŁYNNA (KREW) ---
            {
                "id": 9,
                "kategoria": "Tkanka Łączna Płynna",
                "nazwa": "Osocze (Plasma)",
                "lokalizacja": "Krew (ok. 55% objętości)[cite: 1]",
                "budowa": "Płynna macierz (90% wody, białka, sole)[cite: 1]",
                "funkcja": "Transportuje składniki odżywcze, hormony i odpady[cite: 1]"
            },
            {
                "id": 10,
                "kategoria": "Tkanka Łączna Płynna",
                "nazwa": "Erytrocyty (Krwinki czerwone)",
                "lokalizacja": "Krew (4,5 mln/mm³ / 4,5·10¹²/L)[cite: 1]",
                "budowa": "Komórki bezjądrzaste z hemoglobiną[cite: 1]",
                "funkcja": "Główna funkcja: transport tlenu ($O_2$) i częściowo $CO_2$[cite: 1]"
            },
            {
                "id": 11,
                "kategoria": "Tkanka Łączna Płynna",
                "nazwa": "Trombocyty (Płytki krwi)",
                "lokalizacja": "Krew (200-400 tys./mm³)[cite: 1]",
                "budowa": "Fragmenty cytoplazmy megakariocytów[cite: 1]",
                "funkcja": "Uczestniczą w procesie krzepnięcia krwi[cite: 1]"
            },
            {
                "id": 12,
                "kategoria": "Tkanka Łączna Płynna",
                "nazwa": "Leukocyty (Krwinki białe)",
                "lokalizacja": "Krew (4-10 tys./mm³)[cite: 1]",
                "budowa": "Posiadają jądro komórkowe[cite: 1]",
                "funkcja": "Ochrona organizmu i reakcje odpornościowe[cite: 1]"
            },

            # --- TKANKA NERWOWA (NEURON) ---
            {
                "id": 13,
                "kategoria": "Tkanka Nerwowa",
                "nazwa": "Struktura Neurona i Komórki Glejowe",
                "lokalizacja": "Układ nerwowy[cite: 1]",
                "budowa": "Dendryty, ciało komórkowe, jądro, akson (neuryt), osłonka mielinowa (lemocyty/komórki Schwanna), węzły Ranviera, kolbki synaptyczne[cite: 1, 4]",
                "funkcja": "Odbiór, przetwarzanie i przewodzenie impulsów nerwowych[cite: 1]"
            }
        ]

    def export(self):
        with open("biopulse_data.json", "w", encoding="utf-8") as f:
            json.dump(self.knowledge_base, f, ensure_ascii=False, indent=4)
        print("[SUCCESS]: Wygenerowano aktualny plik JSON z notatek biologicznych[cite: 1, 4]!")

if __name__ == "__main__":
    engine = BioPulseEngine()
    engine.build_database()
    engine.export()
