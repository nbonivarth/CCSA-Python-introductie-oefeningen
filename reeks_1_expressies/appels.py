aantal_appels = int(input())

AANTAL_APPELS_PER_KIST = 20
AANTAL_KISTEN_PER_PALLET = 35

aantal_palletten_gevuld = aantal_appels // (
    AANTAL_APPELS_PER_KIST * AANTAL_KISTEN_PER_PALLET)
overgebleven_appels_temp = aantal_appels % (
    AANTAL_APPELS_PER_KIST * AANTAL_KISTEN_PER_PALLET)
aantal_kisten_gevuld = overgebleven_appels_temp // 20
totaal_overgebleven_appels = overgebleven_appels_temp % 20

print(f"{aantal_palletten_gevuld}\n{aantal_kisten_gevuld}\n{totaal_overgebleven_appels}")
