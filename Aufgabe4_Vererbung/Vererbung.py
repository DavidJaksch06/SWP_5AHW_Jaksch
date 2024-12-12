class Person:
    def __init__(self, name, geschlecht):
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
        self.mitarbeiter.append(mitarbeiter)

    def anzahl_mitarbeiter(self):
        return len(self.mitarbeiter)

class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def hinzufuegen_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def gesamtanzahl_mitarbeiter(self):
        return sum(abteilung.anzahl_mitarbeiter() for abteilung in self.abteilungen)

    def gesamtanzahl_abteilungsleiter(self):
        return sum(1 for abteilung in self.abteilungen if any(isinstance(m, Abteilungsleiter) for m in abteilung.mitarbeiter))

    def gesamtanzahl_abteilungen(self):
        return len(self.abteilungen)

    def groesste_abteilung(self):
        return max(self.abteilungen, key=lambda abt: abt.anzahl_mitarbeiter(), default=None)

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