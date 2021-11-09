verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2 

def bereken_maandkosten(km_per_maand):
    maandkosten = (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand
    print("de het kosten zijn ", maandkosten, ' euro per maand.')
    return maandkosten 

km_per_maand = float(input("hoeveel km rijd u per maand??????????????????????????? "))
resultaat = bereken_maandkosten(km_per_maand)