import numpy as np

nilai = np.array([75, 88, 62, 91, 78, 83, 55, 95, 70, 81, 77, 89, 68, 92, 73, 86, 60, 94, 79, 82, 65, 87, 72, 90, 63, 85, 71, 93, 58, 80])
nilai_urut = np.sort(nilai)
nilai_terbalik = nilai_urut[::-1]
nilai_terbesar = nilai_terbalik[:5]

print(f"Nilai diurutkan dari yang terbesar ke terkecil: \n{nilai_terbalik}")
print(f"5 Nilai terbesar: {nilai_terbesar}")