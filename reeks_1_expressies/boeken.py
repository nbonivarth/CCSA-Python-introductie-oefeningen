prijs_boek = 24.95
korting_percentage = 40
verzendingskost_eerste_boek = 3
verzendingskost_volgend_boek = 0.75
aantal_boeken = 60

totale_prijs_zonder_korting = aantal_boeken * prijs_boek
korting = totale_prijs_zonder_korting * 40 / 100
totale_verzendingskosten = verzendingskost_eerste_boek + \
    (aantal_boeken - 1) * verzendingskost_volgend_boek

print(totale_prijs_zonder_korting - korting + totale_verzendingskosten)
