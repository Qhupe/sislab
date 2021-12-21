import matplotlib.pyplot as plt
import numpy as np

giris = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
cikis = np.array([1, 1, 1, 0])

plt.title('OR KAPISI', fontsize=16)
plt.scatter(giris[:,0], giris[:,1], s=400, c = cikis)
plt.grid()
plt.show()

ogrenme_orani = 0.1
iter_sayisi = 10


w = np.zeros(1 + giris.shape[1])
hatalar = []
for _ in range(iter_sayisi):
  hata = 0
  for xi, hedef in zip(giris, cikis):
    hesap = np.dot(xi, w[1:]) + w[0]
    tahmin = np.where(hesap >= 0.0, 1, 0)
    degisim = ogrenme_orani * (hedef - tahmin)
    w[1:] += degisim * xi
    w[0] += degisim
    hata += int(degisim != 0.0)
  hatalar.append(hata)

  hatalar

  w

  plt.plot(range(1, len(hatalar) + 1), hatalar)
  plt.xlabel('Deneme No')
  plt.ylabel('Hatalı tahmin sayısı')
  plt.show()