totaal = 0
kaart = -1
while totaal != 21 and totaal < 21 and kaart != 0:
    kaart = int(input())

    if kaart < 1 or 11 < kaart:
        continue

    totaal = totaal + kaart

if (totaal == 21):
    print("Gewonnen!")
elif (totaal > 21):
    print(f"Verbrand ({totaal})")
else:
    print(f"Voorzichtig gespeeld ({totaal})")
