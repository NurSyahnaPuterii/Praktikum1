kelilingtaman = 5
jaraktempuh = 14
phi = 3.14
kelilinglingkaran = jaraktempuh/kelilingtaman
jarijari = (kelilinglingkaran/(phi*2))

print("Diketahui :")
print("Pak Dengklek mengelilingi taman = {} putaran".format (kelilingtaman))
print("Jarak tempuh Pak Dengklek = {} kilomemeter".format (jaraktempuh))
print("Jawaban :")
print("Jari-jari taman yang dikelilingi Pak Dengklek adalah {} kilometer".format (round (jarijari,2)))