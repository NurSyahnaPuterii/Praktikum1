import math 

alas = 5
tinggi = 12
sisi_miring = (math.sqrt(tinggi*tinggi + alas*alas))

print ("Diketahui :")
print ("Alas = 5 cm")
print ("Tinggi = 12 cm")
print ("Jawab : ")
print ("\n")
print ("Sisi A = {} cm" .format(tinggi))
print ("Sisi B = {}cm". format (round(sisi_miring,)))
print ("Sisi C = {}cm". format (alas))
print ("Keliling = {}cm".format (round(alas + tinggi + sisi_miring,)))
print ("Luas = {}cm". format (round(alas * tinggi/2,)))