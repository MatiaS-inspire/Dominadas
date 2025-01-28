
Dias = 366
Cantidad_dominadas = 1
Dominadas_hechas = 0 # ESTA ES LA VARIABLE ACUMULADORA LA QUE ME PERMITE COMPILAR EL MONTO EN CADA ITERACIÓN

for Cantidad_dominadas in range(Dias):
   Dominadas_hechas += Cantidad_dominadas

print("Gero Arias hizo " + str(Dominadas_hechas) + " dominadas")
