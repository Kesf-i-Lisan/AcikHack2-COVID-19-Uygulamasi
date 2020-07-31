import numpy as np
import networkx as graf_manipulasyonu
from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer



class extractive_özetleme:
    def __init__(self):
        self.dokuman = None
        self.metin = None
        self.ozet = None
        self.indis_degeri_0             = 0
        self.derece_durum_rolesi        = 0
        self.genel_durum_txt_format     = 1
        self.genel_durum_binary_format  = 2
        self.genel_islem_dizisi_tamponu = []
    def dokuman_icerigini_yakala(dosya_ismi):
        if dosya_ismi.lower().endswith('.txt'):
            dosya_isleme_secimi = genel_durum_txt_format
        else:
            dosya_isleme_secimi = genel_durum_binary_format
        if dosya_isleme_secimi == genel_durum_txt_format:
            yakalanan_dosya = open(dosya_ismi, 'r')
            metin_belgesi = yakalanan_dosya.read()
            yakalanan_dosya.close()
        else:
            print('Dosya yukleme hatasi')
            return None
        self.dokuman = metin_belgesi
        return self.dokuman

    def _cumle_ayristirma_islemi(self,icerik):
        ayristici_nesne_bileseni = PunktSentenceTokenizer()
        dokuman_cumleleri = ayristici_nesne_bileseni.tokenize(icerik)
        return dokuman_cumleleri

    def özetle(self,metin):
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
            for i in range(0, len(cikti_cumle_dizisi)):
                self.genel_islem_dizisi_tamponu.append((float(cikti_cumle_dizisi[i][0]) - derece_asgari) / (derece_azami - derece_asgari))

        uzunluklar_esigi_degeri = (sum(self.genel_islem_dizisi_tamponu) / len(self.genel_islem_dizisi_tamponu)) + 0.2

        ozetlenecek_cikti_cumleleri = []
        if len(self.genel_islem_dizisi_tamponu) > 1:
            for i in range(0, len(self.genel_islem_dizisi_tamponu)):
                if self.genel_islem_dizisi_tamponu[i] > uzunluklar_esigi_degeri:
                    ozetlenecek_cikti_cumleleri.append(cikti_cumle_dizisi[i][1])
        else:
            ozetlenecek_cikti_cumleleri.append(cikti_cumle_dizisi[0][1])

        dokuman_ozeti = " ".join(str(x) for x in ozetlenecek_cikti_cumleleri)
        return dokuman_ozeti

    def dokuman_ozetle(self,dosya_ismi):
        icerigi_yakalanan_dokuman = self.dokuman_icerigini_yakala(dosya_ismi)
        ayristirilmis_cumle_listesi = self._cumle_ayristirma_islemi(icerigi_yakalanan_dokuman)
        self.ozet = self.özetle(ayristirilmis_cumle_listesi)
        return self.ozet
    def metin_ozetle(self,metin):
        print("burada")
        ayristirilmis_cumle_listesi = self._cumle_ayristirma_islemi(metin)
        self.ozet = self.özetle(ayristirilmis_cumle_listesi)
        return self.ozet
