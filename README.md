 <a href="http://kesf-i-lisan.co/"><img id="radius_deneme" src="https://github.com/Kesf-i-Lisan/AcikHack2-C19-Ozel/blob/master/dosyalar/kesf_i_lisan_logo.png" width="30%" height="30%" align="right"/></a>
# Açık Hack 2020|COVID-19 Özel Uygulaması 🎯

<!--<p align="center">
 <a href="http://kesf-i-lisan.co/"><img id="radius_deneme" src="https://github.com/Kesf-i-Lisan/AcikHack2-C19-Ozel/blob/master/dosyalar/kesf_i_lisan_logo.png" style="border-radius:60% !important;  width:350px !important; height:20% !important; " align="center"/></a>
</p>-->
<p align="center">

  <a href="https://github.com/kefranabg/readme-md-generator/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
  </a>
</p>

<a href="http://kesf-i-lisan.co/Anasayfa/Kutuphane_Islevleri"> <img src="https://img.icons8.com/dusk/50/000000/open-source.png"/> Detaylı Anlatım Yazımız </a>

Gerekli Kütüphane ve Araçlar | Version
------------ | -------------
Python | 3.5
NLTK | x.x

```sh
git clone https://github.com/Kesf-i-Lisan/AcikHack2-C19-Ozel
```
## 🚀 Extractive Özetleme

<h3 text-align="justify">Algoritmamız Türkçe haber metinleri üzerinde özetleme yapan algoritma aşağıdaki şekildedir. Bu algoritma metin içerisindeki en önemli cümleleri kelime sıklık matrisleri oluşturarak seçmektedir.</h3>

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
### Harici dokümanlar üzerinde uygulanabilir.
```python
    def dokuman_ozetle(self,dosya_ismi):
        icerigi_yakalanan_dokuman = self.dokuman_icerigini_yakala(dosya_ismi)
        ayristirilmis_cumle_listesi = self._cumle_ayristirma_islemi(icerigi_yakalanan_dokuman)
        self.ozet = self.ozetle(ayristirilmis_cumle_listesi)
        return self.ozet
```
### Doğrudan metinler üzerinde uygulanabilir.
```python
    def metin_ozetle(self,metin):
        ayristirilmis_cumle_listesi = self._cumle_ayristirma_islemi(metin)
        self.ozet = self.ozetle(ayristirilmis_cumle_listesi)
        return self.ozet
```
## ✨ Demo Bileşenleri


## 🎓👀 Proje Geliştiricileri

## 📝 License

Copyright © 2020 [Kesf_i_Lisan](https://github.com/Kesf-i-Lisan).<br />
[MIT](https://github.com/Kesf-i-Lisan/AcikHack2-C19-Ozel/blob/master/LICENSE) tarafından lisanslanmıştır.
