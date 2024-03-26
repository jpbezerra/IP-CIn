x_tantan = int(input())
z_tantan = int(input())

distancia_hogsmeade = float(((x_tantan - 34) ** 2 + (220 - z_tantan) ** 2) ** 0.5)
distancia_hogsmeade = format(distancia_hogsmeade, ".2f")

distancia_kakariko = float(((x_tantan - 0) ** 2 + (z_tantan - 0) ** 2) ** 0.5)
distancia_kakariko = format(distancia_kakariko, ".2f")

distancia_solitude = float(((x_tantan - 140) ** 2 + (z_tantan - 456) ** 2) ** 0.5)
distancia_solitude = format(distancia_solitude, ".2f")

print("Distancia para Hogsmeade: " + str(distancia_hogsmeade))
print("Distancia para Kakariko: " + str(distancia_kakariko))
print("Distancia para Solitude: " + str(distancia_solitude))