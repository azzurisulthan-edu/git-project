import numpy as np

untung = np.array([200000, 500000, 250000, 300000, 350000, 150000, 780000, 700000, 150000, 100000, 900000, 400000, 450000, 390000])

rata = np.mean(untung)
untung_urut = np.sort(untung)
tertinggi = untung_urut[-1]
terendah = untung_urut[0]
indeks_tertinggi = np.where(untung == tertinggi)[0][0] + 1
indeks_terendah = np.where(untung == terendah)[0][0] + 1

print(f"Rata-rata keuntungan : Rp{rata:,.0f}")
print(f"Keuntungan tertinggi : Rp{tertinggi:,.0f} (hari ke-{indeks_tertinggi})")
print(f"Keuntungan terendah  : Rp{terendah:,.0f} (hari ke-{indeks_terendah})")