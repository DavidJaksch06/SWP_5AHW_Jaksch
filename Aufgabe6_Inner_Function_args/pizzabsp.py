def bestelle_pizza(*zutaten, **optionen):
    def zusammenfassung():
        zutaten_text = ", ".join(zutaten) if zutaten else "Standardzutaten"
        groesse = optionen.get("groesse", "mittel") #mittel wenn groesse nicht vohanden
        lieferung = "Ja" if optionen.get("liefern", False) else "Nein"
        return f"Pizza ({groesse}): {zutaten_text}. Lieferung: {lieferung}."

    return zusammenfassung()

def main():
    bestellung = bestelle_pizza("Salami", "Pilze", "Käse", groesse="groß", liefern=True)
    print(bestellung)
    bestellung2 = bestelle_pizza(liefern=True)
    print(bestellung2)

if __name__ == "__main__":
    main()