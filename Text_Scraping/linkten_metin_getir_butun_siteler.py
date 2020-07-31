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
