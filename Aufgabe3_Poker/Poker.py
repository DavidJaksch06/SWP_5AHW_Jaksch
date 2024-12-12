from collections import Counter
import random




class Karte:
    def __init__(self, zahl, farbe):
        self.zahl = zahl
        self.farbe = farbe

    def __str__(self):
        return f"{self.zahl}{self.farbe}"


def erstelle_hand(zahlen, farben):
    deck = [Karte(zahl, farbe) for zahl in zahlen for farbe in farben]
    hand = random.sample(deck, 5)
    return hand


def pruefe_hand(hand):
    karten_werte = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                    'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    zahlen = [karte.zahl for karte in hand]
    farben = [karte.farbe for karte in hand]

    zahlen_haeufigkeit = Counter(zahlen)

    werte = sorted(karten_werte[zahl] for zahl in zahlen)

    haeufigkeiten = sorted(zahlen_haeufigkeit.values(), reverse=True)

    # alle farben gleich
    flush = len(set(farben)) == 1

    straight = (len(set(werte)) == 5 and max(werte) - min(werte) == 4) or werte == [2, 3, 4, 5, 14]

    # Hand auswerten
    if flush and straight and min(werte) == 10:
        return "Royal Flush"
    if flush and straight:
        return "Straight Flush"
    if haeufigkeiten == [4, 1]:
        return "Vierling"
    if haeufigkeiten == [3, 2]:
        return "Full House"
    if flush:
        return "Flush"
    if straight:
        return "Straight"
    if haeufigkeiten == [3, 1, 1]:
        return "Drilling"
    if haeufigkeiten == [2, 2, 1]:
        return "Zwei Paare"
    if haeufigkeiten == [2, 1, 1, 1]:
        return "Paar"

    # also nichts
    return "Hohe Karte"


def main():
    zahlen = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    farben = ["\u2660", "\u2665", "\u2663", "\u2666"]

    while True:
        try:
            ziehungsanzahl = int(input("Bitte geben Sie die Anzahl der Ziehungen ein: "))
            break
        except ValueError:
            print("Ungültige Eingabe! Bitte geben Sie eine ganze Zahl ein.")

    poker_haende = \
        {
            "Hohe Karte": 0,
            "Paar": 0,
            "Zwei Paare": 0,
            "Drilling": 0,
            "Straight": 0,
            "Flush": 0,
            "Full House": 0,
            "Vierling": 0,
            "Straight Flush": 0,
            "Royal Flush": 0
        }

    for i in range(ziehungsanzahl):
        hand = erstelle_hand(zahlen, farben)

        print("Gezogene Hand:", ' '.join(str(karte) for karte in hand))

        ergebnis = pruefe_hand(hand)
        poker_haende[ergebnis] += 1

    # Name der Pokerhände
    haende = list(poker_haende.keys())

    # anzahl der häufigkeiten
    zaehlungen = list(poker_haende.values())

    # gesamte Ziehungen
    gesamt_zaehlungen = sum(zaehlungen)

    prozentsaetze = [(zaehlung / gesamt_zaehlungen) * 100 for zaehlung in zaehlungen]

    print("\nPoker Hände Häufigkeiten und Prozentsätze:")
    for hand, zaehlung, prozentsatz in zip(haende, zaehlungen, prozentsaetze):
        print(f"{hand}: {zaehlung} ({prozentsatz:.3f}%)")


if __name__ == "__main__":
    main()


#class Auto:
 #   def __init__(self, marke, modell):
  #      self.marke = marke
   #     self.modell = modell

    #def start(self):
     #   print("Das Auto startet.")

#class ElektroAuto(Auto):
 #   def __init__(self, marke, modell, batteriekapazitaet):
  #      super().__init__(marke, modell)
   #     self.batteriekapazitaet = batteriekapazitaet

    #def start(self):
     #   print("Das Elektroauto startet lautlos!")

# Test
#e_auto = ElektroAuto("Tesla", "Model S", 100)
#e_auto.start()
