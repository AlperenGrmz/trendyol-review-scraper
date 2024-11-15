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

**Otomatik Kurulum**: Alternatif olarak, tüm kütüphaneleri tek bir komutla kurmak için `requirements.txt` dosyasını kullanabilirsiniz:

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

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.
