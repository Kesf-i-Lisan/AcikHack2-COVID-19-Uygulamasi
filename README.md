<p align="center"> <a href="http://kesf-i-lisan.co/"><img id="radius_deneme" src="https://github.com/Kesf-i-Lisan/AcikHack2-C19-Ozel/blob/master/Dosyalar/kesf_i_lisan_logo.png" width="30%" height="30%" align="center"/></a> </p>
<p align="center"> <a href="http://kesf-i-lisan.co/"> Link </a> </p>


<p align="center"> <h1 align="center">  🎯 Açık Hack 2020 | COVID-19 Özel Uygulaması 🎯 </h1> </p>

<!--<p align="center">
 <a href="http://kesf-i-lisan.co/"><img id="radius_deneme" src="https://github.com/Kesf-i-Lisan/AcikHack2-C19-Ozel/blob/master/dosyalar/kesf_i_lisan_logo.png" style="border-radius:60% !important;  width:350px !important; height:20% !important; " align="center"/></a>
</p>-->
<p align="center">

  <a href="https://github.com/kefranabg/readme-md-generator/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
  </a>
</p>

<a href="http://kesf-i-lisan.co/Anasayfa/Kutuphane_Islevleri"> <img src="https://img.icons8.com/dusk/50/000000/open-source.png"/> Detaylar </a>

 
Gerekli Kütüphane ve Araçlar | Version
------------ | -------------
Python | 3.x
NLTK | 3.5
Re | 2020.7.14
Spacy | 2.3.2
Torch | 1.6.0
Pandas | 1.1.0
Numpy | 1.19.1
Networkx | 2.4
Scikit-learn | 0.23.1
Seaborn | 0.10.1
Requests | 2.24.0
Httplib2 | 0.18.1
Urllib3 | 1.25.10


## Ortam Kurulumu - Adım 0
Keşf-i Lisans projesi sıfırdan metin toplama, metin sınıflandırma ve metin özetleme gerçekleştirmenizi mümkün kılar. Proje süresince miniconda  https://docs.conda.io/en/latest/miniconda.html kullanılmasını öneriyoruz.
```sh
git clone https://github.com/Kesf-i-Lisan/AcikHack2-COVID-19-Uygulamasi
```
## 🚀 Kaynak Kökü Toplama - Adım 1
Veri toplamanın en önemli kısmı çok sayıda kaynağa sahip olmaktır. Yani tutarlı ve özgün içerik üreten web linklerine ulaşmaktır. Bunun için Adım 2 deki yöntemin dışında yani kök dizin vermek dışında, linkleri listeler halinde elde ederek kullanabilirsiniz.  

```python
def link_getirici_yontem_algoritma_1(arama_metni):
    sorgu_sayfa_sonucu = requests.get("https://www.google.dz/search?q="+str(arama_metni))
    soup_nesnesi = BeautifulSoup(sorgu_sayfa_sonucu.content)
    import re
    links = soup_nesnesi.findAll("a")
    for link in links:
        print(link["href"])
```

```python
def link_getirici_google_import(arama_metni):
    link_tamponu = []
    for yineleyici in search(arama_metni, tld="co.in", num=4, stop=100, pause=8):
        link_tamponu.append(j)
        print(yineleyici)
```
## 🚀 Metin Toplama - Adım 2
Ön gereksinimleri için text_scraping klasörü altında bulunan requirements.txt klasöründe bulunan kütüphaneler kurulmalıdır.
pip install -r requirements.txt
Metin özetleme aracı mevcut olarak 4 site desteklemektedir.
 -CNN
 -Milliyet
 -NTV
 -BBC
 
Metin toplayabilmek için list_of_link.txt dosyasına her satıra bir link gelecek biçimde kök linkleri yazınız. Ardından uygulama tüm kök link ve alt linkleri gezerek metin toplama işlemini gerçekleştirecektir.

```python
python get_text_from_CNN.py
```

## 🚀 Metin Toplama - Adım 2 - Önemli Opsiyonel
Veri toplama işlemi konusunda herhangi bir sınır yaşamak istemiyorsanız aşağıdaki yöntemi kullanarak normalizasyon süreçlerine ayrıca dallanmadan temiz veriler toplabilir. Toplanmış olan çıktıları özetleme algoritması içerisinde kullanabilirsiniz.
```python
from bs4 import BeautifulSoup,SoupStrainer
import urllib.request
import urllib
from lxml import html


normalizasyon_boyut_kriteri = 30
def linkden_metin_getir_Detayli_normalizasyon(giden_link):
    html_nesnesi = urllib.request.urlopen(giden_link)
    soup_nesnesi = BeautifulSoup(html)

    for script in soup_nesnesi(["script", "style"]):
        script.extract()

    metin = soup_nesnesi.get_text()
    satir_parcalari = (line.strip() for line in metin.splitlines())
    icerik_parcalari = (phrase.strip() for satir_parcasi in satir_parcalari for phrase in satir_parcasi.split("  "))
    for yineleyici_parcacik in icerik_parcalari:
        if len(yineleyici_parcacik) > normalizasyon_boyut_kriteri:
            print(yineleyici_parcacik)
```

## 🚀 Metin Normalizasyonu - Adım 3
Toplanan metinler genellikle NLP çalışmaları için istenmeyen pek çok karakter içerir. Normalizer.py modülünde yer alan fonksiyonlar yardımı ile toplanan metinleri kolaylıkla normalize etmek mümkün.

Basit Kullanım
```python
import Normalizer
text = "Bu bir - test Metnidir."
result = Normalizer.normalize(text)
print("Çıktı: ",result)

Çıktı: bu bir test metnidir
```
Geliştirilen Normalizasyon uygulaması Türkçe için özel normalizasyonlar içermektedir.
number2string -> Metin içerisinde yer alan bütün sayıları Türkçe kelime karşılığına dönüştürür.
date2string  -> Tarih formatında yazılan ifadeleri Türkçe gün-ay-yıl formatına dönüştürür.
time2string -> Saat formatonda yazılan ifadeleri Türkçe rakam formatına dönüştürür.

## 🚀 Extractive Özetleme - Adım 4

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

#### Harici dokümanlar üzerinde uygulanabilir:
```python
    def dokuman_ozetle(self,dosya_ismi):
        icerigi_yakalanan_dokuman = self.dokuman_icerigini_yakala(dosya_ismi)
        ayristirilmis_cumle_listesi = self._cumle_ayristirma_islemi(icerigi_yakalanan_dokuman)
        self.ozet = self.ozetle(ayristirilmis_cumle_listesi)
        return self.ozet
```

Kullanım
```python
import extractive_ozetleme

ozetleme = extractive_ozetleme.extractive_ozetleme()
dokuman = open("deneme.txt","r").readlines()
dokuman_ozeti = ozetleme.dokumen_ozetle(dokuman)
```
#### Doğrudan metinler üzerinde uygulanabilir:
```python
    def metin_ozetle(self,metin):
        ayristirilmis_cumle_listesi = self._cumle_ayristirma_islemi(metin)
        self.ozet = self.ozetle(ayristirilmis_cumle_listesi)
        return self.ozet
```
Kullanım
```python
import extractive_ozetleme

ozetleme = extractive_ozetleme.extractive_ozetleme()
metin = "Bir test metni"
ozet = ozetleme.metin_ozetle(metin)
```
## 🚀 Metin Sınıflandırma- Adım 5
Etiketsiz toplanan metinlerin sınıflandırılması için, etiketli Türkçe haber verilerinden oluşan veri kümesi kullanılarak PyTorch ile sınıflandırma çalışması gerçekleştirilmiştir.

Eğitim süresince 42bin_haber veri kümesi kullanılmıştır. Veri kümesini bu bağlantıdan indirebilirsiniz. https://drive.google.com/file/d/1wOoIHiQzCyk5p7ZieXkiDCHAtA3GmcUX/view?usp=sharing

Yapılan eğitimde dünya, ekonomi, genel, magazine, saglık, spor, Türkiye kategorilerindeki verilerden oluşan 7 farklı sınıf kullanulmıştır.
Eğitim sonucu %89 eğitim %71 test başarısı elde edilmiştir.
## ✨ Demo Bileşenleri
<p align="center"> <a href="http://kesf-i-lisan.co/"><img id="radius_deneme" src="https://github.com/Kesf-i-Lisan/AcikHack2-COVID-19-Uygulamasi/blob/master/Dosyalar/web_uygulamasi_ekran_ciktisi.png"align="center"/></a> </p>

<p align="center"> <a href="http://kesf-i-lisan.co/"><img id="radius_deneme" src="https://github.com/Kesf-i-Lisan/AcikHack2-COVID-19-Uygulamasi/blob/master/Dosyalar/web_uygulamasi_ekran_ciktisi_1.png"align="center"/></a> </p>
## 📝 Lisans
[[MIT](https://github.com/Kesf-i-Lisan/AcikHack2-C19-Ozel/blob/master/LICENSE)] <br/>
Copyright © 2020 [Kesf_i_Lisan](https://github.com/Kesf-i-Lisan).<br />


