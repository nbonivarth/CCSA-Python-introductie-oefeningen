x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
x6 = int(input())
x7 = int(input())
x8 = int(input())
x9 = int(input())
x10 = int(input())

getallen = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]

controlegetal = (x1 + 2 * x2 + 3 * x3 + 4 * x4 + 5 * x5 +
                 6 * x6 + 7 * x7 + 8 * x8 + 9 * x9) % 11

is_ok = 1  # Default is OK
for getal in getallen:
    if not (0 <= getal and getal <= 9):
        is_ok = 0  # FOUT
    else:
        if (x10 != controlegetal):
            is_ok = 0  # FOUT

if is_ok:
    print("OK")
else:
    print("FOUT")
