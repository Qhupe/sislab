import matplotlib.pyplot as plt
import numpy as np
import pandas

df = pandas.read_csv('data_0123.csv', header=None)#veri seti
df
cikis = df.iloc[0:100, 4].values#cikis satiri
cikis = np.where(cikis == 1, -1, 1)#Veri setindeki 0 lar -1, 1 ler 1 olarak cikis dizisinde.
giris = df.iloc[0:100, [1, 2]].values#giris değerleri

plt.title('2D görünüm', fontsize=16)#

plt.scatter(giris[:50, 0], giris[:50, 1], color='black', marker='o', label='allsifir')#0 sınıfına ait verilerin çizimi.
plt.scatter(giris[50:100, 0], giris[50:100, -1], color='green', marker='x', label='allbir')#1 sınıfına ait verilerin çizimi.
plt.xlabel('sapel length')#
plt.ylabel('petal length')#
plt.legend(loc='upper left')#

plt.show()#

class Perceptron(object):
    def __init__(self, ogrenme_orani=0.1, iter_sayisi=10):#
        self.ogrenme_orani = ogrenme_orani#
        self.iter_sayisi = iter_sayisi#

    def ogren(self, X, y):
        self.w = np.zeros(1 + X.shape[1])#
        self.hatalar = []#
        for _ in range(self.iter_sayisi):
            hata = 0#
            for xi, hedef in zip(X, y):
                degisim = self.ogrenme_orani * (hedef - self.tahmin(xi))#
                self.w[1:] += degisim * xi#
                self.w[0] += degisim#
                hata += int(degisim != 0.0)#
            self.hatalar.append(hata)#
        return self

    def net_input(self, X):
        return np.dot(X, self.w[1:]) + self.w[0]#

    def tahmin(self, x):
        return np.where(self.net_input(x) >= 0.0, 1, -1)#

        siniflandirici = Perceptron(ogrenme_orani=0.1, iter_sayisi=10)#

        siniflandirici.ogren(giris, cikis)#

        siniflandirici.w#

        siniflandirici.hatalar

        plt.plot(range(1, len(siniflandirici.hatalar) + 1), siniflandirici.hatalar)#

        plt.xlabel('Deneme')#

        plt.ylabel('Hatalı tahmin sayısı')#

        plt.show()