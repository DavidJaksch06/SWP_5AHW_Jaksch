class Person:
    def __init__(self, name, geschlecht):
        if not name or not isinstance(name, str):  # Fehler a) Neuer Fehler und behebar
            raise ValueError("Name muss ein nicht-leerer String sein.")
        if geschlecht not in ['m', 'w']:  # Fehler a) Neuer Fehler und behebar
            raise ValueError("Geschlecht muss 'm' oder 'w' sein.")
        self.name = name
        self.geschlecht = geschlecht


class Mitarbeiter(Person):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht)
        self.abteilung = abteilung


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht, abteilung)
        self.leitet_abteilung = abteilung


class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []

    def hinzufuegen_mitarbeiter(self, mitarbeiter):
        if not isinstance(mitarbeiter, Mitarbeiter):  # Fehler b) Hochblubber-Fehler und behebar
            raise TypeError("Nur Objekte der Klasse Mitarbeiter oder Abteilungsleiter können hinzugefügt werden.")
        self.mitarbeiter.append(mitarbeiter)

    def anzahl_mitarbeiter(self):
        return len(self.mitarbeiter)


class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def hinzufuegen_abteilung(self, abteilung):
        if not isinstance(abteilung, Abteilung):  # Fehler c) Neuer Fehler und NICHT behebar
            raise TypeError("Nur Objekte der Klasse Abteilung können hinzugefügt werden.")
        self.abteilungen.append(abteilung)

    def gesamtanzahl_mitarbeiter(self):
        return sum(abteilung.anzahl_mitarbeiter() for abteilung in self.abteilungen)

    def gesamtanzahl_abteilungsleiter(self):
        return sum(
            1 for abteilung in self.abteilungen if any(isinstance(m, Abteilungsleiter) for m in abteilung.mitarbeiter))

    def gesamtanzahl_abteilungen(self):
        return len(self.abteilungen)

    def groesste_abteilung(self):
        try:
            return max(self.abteilungen, key=lambda abt: abt.anzahl_mitarbeiter(), default=None)
        except ValueError as e:  # Fehler d) Hochblubber-Fehler und NICHT behebar
            raise RuntimeError("Es gibt keine Abteilungen in der Firma.") from e

    def prozentanteil_geschlechter(self):
        gesamt_mitarbeiter = self.gesamtanzahl_mitarbeiter()
        frauen = sum(1 for abteilung in self.abteilungen for m in abteilung.mitarbeiter if m.geschlecht == 'w')
        maenner = gesamt_mitarbeiter - frauen
        if gesamt_mitarbeiter == 0:
            return {"Frauen": 0, "Männer": 0}
        return {
            "Frauen": round((frauen / gesamt_mitarbeiter) * 100, 2),
            "Männer": round((maenner / gesamt_mitarbeiter) * 100, 2)
        }
