 <a href="http://kesf-i-lisan.co/"><img id="radius_deneme" src="https://github.com/Kesf-i-Lisan/AcikHack2-C19-Ozel/blob/master/dosyalar/kesf_i_lisan_logo.png" width="40%" height="40%" align="right"/></a>
# AcikHack2-C19-Ozel
<p align="center">
 <a href="http://kesf-i-lisan.co/"><img id="radius_deneme" src="https://github.com/Kesf-i-Lisan/AcikHack2-C19-Ozel/blob/master/dosyalar/kesf_i_lisan_logo.png" style="border-radius:60% !important;  width:350px !important; height:20% !important; " align="center"/></a>
</p>
<p align="center">

  <a href="https://github.com/kefranabg/readme-md-generator/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
  </a>
</p>


Gerekli Kütüphane ve Araçlar | Version
------------ | -------------
Python | 3.5
NLTK | x.x

```sh
git clone https://github.com/Kesf-i-Lisan/AcikHack2-C19-Ozel
```
## 🚀 Extractive Özetleme
```python
def ozetle(self,metin):
        vektor_islemleri = CountVectorizer()
        vektor_islemleri_matrisi = vektor_islemleri.fit_transform(metin)

        deger_matrisi = TfidfTransformer().fit_transform(vektor_islemleri_matrisi)
        cozunurluk_grafi = deger_matrisi * deger_matrisi.T
        cumle_vektor_graf_yapisi = graf_manipulasyonu.from_scipy_sparse_matrix(cozunurluk_grafi)
        graf_manipulasyonu.draw_circular(cumle_vektor_graf_yapisi)
        cumlelerin_graf_dereceleri = graf_manipulasyonu.pagerank(cumle_vektor_graf_yapisi)


        cikti_cumle_dizisi = sorted(((cumlelerin_graf_dereceleri[yineleyici_graf_2], s) for yineleyici_graf_2, s in enumerate(ayristirilmis_cumle_listesi)), reverse=True)
        cikti_cumle_dizisi = np.asarray(cikti_cumle_dizisi)

        derece_azami  = float(cikti_cumle_dizisi[self.indis_degeri_0][self.indis_degeri_0])
        derece_asgari = float(cikti_cumle_dizisi[len(cikti_cumle_dizisi) - 1][self.indis_degeri_0])


        if derece_azami - derece_asgari == 0:
            self.genel_islem_dizisi_tamponu.append(0)
            self.derece_durum_rolesi = 1
        if self.derece_durum_rolesi != 1:
            for yineleyici_ekleme in range(0, len(cikti_cumle_dizisi)):
                self.genel_islem_dizisi_tamponu.append((float(cikti_cumle_dizisi[yineleyici_ekleme][self.indis_degeri_0]) - derece_asgari) / (derece_azami - derece_asgari))

        uzunluklar_esigi_degeri = (sum(self.genel_islem_dizisi_tamponu) / len(self.genel_islem_dizisi_tamponu)) + 0.2

        ozetlenecek_cikti_cumleleri = []
        if len(self.genel_islem_dizisi_tamponu) > 1:
            for yineleyici_ozetleme in range(0, len(self.genel_islem_dizisi_tamponu)):
                if self.genel_islem_dizisi_tamponu[yineleyici_ozetleme] > uzunluklar_esigi_degeri:
                    ozetlenecek_cikti_cumleleri.append(cikti_cumle_dizisi[yineleyici_ozetleme][self.indis_degeri_1])
        else:
            ozetlenecek_cikti_cumleleri.append(cikti_cumle_dizisi[self.indis_degeri_0][self.indis_degeri_1])

        dokuman_ozeti = " ".join(str(x) for x in ozetlenecek_cikti_cumleleri)
        return dokuman_ozeti
```

## ✨ Demo Bileşenleri


## 🎓👀 Proje Geliştiricileri

## 📝 License

Copyright © 2020 [Kesf_i_Lisan](https://github.com/Kesf-i-Lisan).<br />
This project is [MIT](https://github.com/Kesf-i-Lisan/AcikHack2-C19-Ozel/blob/master/LICENSE) licensed.
