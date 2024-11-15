# Trendyol Yorum Veri Kazıyıcı

Bu proje, **Kocaeli Üniversitesi Bilişim Sistemleri Mühendisliği Yazılım Laboratuvarı** dersi kapsamında [Trendyol](https://www.trendyol.com/) web sitesinden **yorum verilerini** çekmek için geliştirilmiştir. Proje, Selenium, Requests ve BeautifulSoup kullanarak ürün yorumlarını toplar ve CSV formatında kaydeder.

## Özelikkler

- **Yorum Kazıyıcı**: Her ürünün yorum sayfasından kullanıcı yorumlarını ve puanlarını toplar.
- **Selenium, BeautifulSoup ve Requests ile Web Kazıma**: Dinamik içerik yüklemek için Selenium, HTML verilerini ayrıştırmak için ise BeautifulSoup ve sayfa içerikleri için requests kullanılır.
- **Hata Yönetimi**: Verilen kategoriler veya öğeler bulunamadığında işlem aksatılmadan devam eder.

## Kurulum ve Gereksinimler

**Python 3.11+** yüklü olduğundan emin olun.
Python sürümünü kontrol etmek için şu komutu kullanabilirsiniz:

```bash
python --version
```

### Gerekli Kütüphaneleri Yükleyin

Projeyi çalıştırabilmek için aşağıdaki Python kütüphanelerine ihtiyaç vardır.

**Otomatik Kurulum**: Tüm kütüphaneleri tek bir komutla kurmak için `requirements.txt` dosyasını kullanabilirsiniz:

```bash
pip install -r requirements.txt
```

**Manuel Kurulum**: Kütüphaneleri tek tek yüklemek isterseniz, şu komutları kullanabilirsiniz:

```bash
pip install selenium
pip install beautifulsoup4
pip install pandas
pip install requests
```

## Kullanım

1. Bu repoyu klonlayın:

   ```bash
   git clone https://github.com/AlperenGrmz/trendyol-review-scraper.git
   cd trendyol-review-scraper
   ```

2. Aşağıdaki kod parçasında, `range(1, 2)` parametresini değiştirerek kaç sayfadan veri çekileceğini ayarlayabilirsiniz:

    ```python
    for page_num in range(1, 2):
        page_url = f"{category_url}?pi={page_num}"
        print(f"İstek atılan sayfa URL: {page_url}")
    ```

3. Bash scripti çalıştırın:

    ```bash
    python scraper.py
    ```

## Kod Acıklaması

Bu proje kapsamında, Trendyol platformundan kullanıcı yorumlarını çekmek için Python programlama dili ve BeautifulSoup, Selenium, pandas, requests ve random kütüphaneleri kullanılmıştır. Proje üç ana adımdan oluşur:

### 1. Kategori ve Ürün Bağlantılarının Toplanması

`fetch_categories` fonksiyonu ile ana sayfadaki pop-up pencereler otomatik kapatılır ve ana kategoriler ile alt kategoriler listelenir. Kategorilere tıklanarak alt kategorilere erişilir, ve BeautifulSoup kullanılarak alt kategori bağlantıları elde edilir.

### 2. Ürün Yorumlarının Toplanması

Alt kategorilere ulaşıldıktan sonra, her bir kategori sayfasındaki ürün bağlantıları alınarak kullanıcı yorumlarının olduğu sayfaya gidilmiştir. `scrape_comments` fonksiyonu, comment-text ve comment-rating sınıflarına göre her üründeki yorumları seçer. `rating_count` fonksiyonu ise yıldız puanlarını doğru şekilde belirlemek için yorumlardaki oranları analiz eder.

### 3. Veri Yapılandırma ve Kaydetme

Toplanan yorum ve puanlar `comments_data` listesine eklenip, pandas ile bir DataFrame’e dönüştürülerek `comments.csv` dosyasına kaydedilir. Sunucu yükünü azaltmak için işlemler arasında rastgele bekleme süreleri eklenmiştir.

## Veri Seti

Bu projede kullanılan veri setine [Google Drive bağlantısı üzerinden](https://drive.google.com/drive/folders/127UIPZt-PtSNaxbG2G67CC7SCr50NEa_) erişebilirsiniz. Bu veriler, yalnızca eğitim ve analiz amaçlıdır.

> **Uyarı:** Veri seti, Trendyol platformundan çekilen yorumlardan oluşmaktadır. Verilerin yalnızca araştırma, analiz ve eğitim amacıyla kullanılması önerilir.

---

## Yorum Analiz ve Basitleştirme

`text-processing.py`, kullanıcı yorumlarını Türkçe doğal dil işleme teknikleriyle (Zemberek, NLTK) analiz eder ve yorumları sadeleştirir. Yorumları analiz ederek, kelimelerinin köklerini ve kelime türlerini çıkarır. Sonuçlar, yorumlar ve puanlarla birlikte `simplified_comments1.csv` dosyasına kaydedilir.

### Kurulum

Projeyi çalıştırabilmek için aşağıdaki Python kütüphanelerine ihtiyaç vardır.

```bash
pip install jpype
pip install nltk
```

Ayrıca, Zemberek kütüphanesini kullanabilmek için **zemberek-full.jar** dosyasını indirmeniz gereklidir. Bu dosyayı, aşağıdaki bağlantılardan temin edebilirsiniz:

- **Zemberek GitHub Deposu**: [Zemberek-NLP](https://github.com/ahmetaa/zemberek-nlp)
- **Google Drive Bağlantısı**: [Zemberek JAR Dosyası](https://drive.google.com/drive/folders/your-folder-link-here)

İndirilen dosyayı, proje dizininizde uygun bir konumda bulundurmanız ve doğru yol üzerinden yüklemeniz gerekecektir.

```python
zemberek_jar_path = "zemberek-full.jar"
```

### Acıklama

### 1.*Stop Words Temizleme*

Turkce diline ozgu stop words (anlam tasımayan sık kullanılan kelimeler) temizlenmistir.

### 2.*Tokenizasyon ve Kücük Harfe Donüstürme*

Yorumlar, kelime bazında bölümlere ayrılmıs ve tüm kelimeler kücük harfe dönüstürülmüstür.

### 3.*Zemberek ile Kök ve Tür Analizi*

Zemberek, her kelimenin kok halini (lemma) ve türünü (primaryPos) cıkararak Turkce diline ozgu dil bilgisi kurallarını dikkate almaktadır. Bu calısmada, Zemberek’in kelime analizi ozellikleri kullanılarak, yorumlar ic¸erisindeki kelimeler koklerine indirilmis ve turlerine gore sınıflandırılmıstır. Ornegin, ”yazıyorum” kelimesi kokune (”yaz”) indirgenmis ve turu (fiil) olarak belirlenmistir

### 4.*Islenmis Yorumaların Yapılandırılması*

Yorumların her biri, kök ve tür bilgileriyle birlikte yenidenen yapılandırımlıstır.

### 5.*Verilerin Kaydedilmesi*

Islenmis yorumlar ve analiz sonucları bir pandas DataFrame'ine dönüştürülmüş ve `simlified.comments.csv` dosyası olarak kaydedilmiştir. Bu dosya duygu analizi modeli için temiz ve tutarlı bir veri kaynağı oluşturmuştur.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.
