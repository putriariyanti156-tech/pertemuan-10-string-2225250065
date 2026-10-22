teks = " belajar python untuk pendidikan "
teks = teks.strip()
while "  " in teks:  # Menggunakan dua spasi untuk membersihkan spasi ganda
    teks = teks.replace("  ", " ")
print(teks.capitalize())