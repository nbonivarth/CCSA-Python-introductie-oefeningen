aantal_gekochte_stuks = int(input())
kostprijs_stuk = float(input())
aantal_barcodes_voor_coupon = int(input())
aantal_mijlen_per_coupon = int(input())

totale_kostprijs = aantal_gekochte_stuks * kostprijs_stuk
aantal_coupons = aantal_gekochte_stuks // aantal_barcodes_voor_coupon
aantal_mijlen = aantal_coupons * aantal_mijlen_per_coupon

print(
    f"Phillips spendeerde ${totale_kostprijs} voor {aantal_mijlen} frequent flyer mijlen.")
