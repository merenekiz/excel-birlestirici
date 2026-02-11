# Excel Birleştirici 📊

Birden fazla Excel dosyasını kolayca tek bir dosyada birleştiren basit ve etkili bir Python aracı.

## Özellikler ✨

- 📁 Klasördeki tüm Excel dosyalarını otomatik olarak bulur
- 🔗 Birden fazla Excel dosyasını tek bir dosyada birleştirir
- ⚡ Hızlı ve verimli işlem
- 🛡️ Veri bütünlüğünü korur
- ⚠️ Uyarı mesajlarını bastırır (daha temiz çıktı)

## Gereksinimler 📋

- Python 3.6+
- pandas
- openpyxl (pandas tarafından otomatik olarak yüklenir)

## Kurulum 🚀

1. Projeyi klonlayın:
```bash
git clone https://github.com/merenekiz/excel-birlestirici.git
cd excel-birlestirici
```

2. Gerekli paketleri yükleyin:
```bash
pip install pandas openpyxl
```

## Kullanım 💻

### Adım 1: Excel Dosyalarını Hazırlayın

Birleştirmek istediğiniz tüm Excel dosyalarını aynı klasöre koyun.

### Adım 2: Dosya Yollarını Ayarlayın

`excel-birlestirici.py` dosyasında bulunan **AYARLAMALAR** bölümünü düzenleyin:

```python
# ===== AYARLAMALAR =====
# Tüm Excel dosyalarının bulunduğu klasör yolu
dosya_yolu = r"./exceller/*.xlsx"  # BURAYA KENDİ KLASÖR YOLUNU YAZ

# Birleştirilmiş dosyanın kaydedileceği yol ve adı
cikti_dosya = r"./exceller/birlesmis_dosya.xlsx"  # BURAYA İSTEDİĞİN KONUM VE DOSYA ADINI YAZ
# ========================
```

#### 📍 Yol Örnekleri

**Windows Kullanıcıları:**
```python
dosya_yolu = r"C:\Users\KullanıcıAdı\Desktop\exceller\*.xlsx"
cikti_dosya = r"C:\Users\KullanıcıAdı\Desktop\exceller\birlesmis_dosya.xlsx"
```

**Mac/Linux Kullanıcıları:**
```python
dosya_yolu = r"/Users/KullanıcıAdı/Desktop/exceller/*.xlsx"
cikti_dosya = r"/Users/KullanıcıAdı/Desktop/exceller/birlesmis_dosya.xlsx"
```

**İlgili Klasör (Programla Aynı Klasör):**
```python
dosya_yolu = r"./exceller/*.xlsx"
cikti_dosya = r"./exceller/birlesmis_dosya.xlsx"
```

#### 💡 Yol Yazarken İpuçları

1. **Mutlak Yol (Tam Yol) Kullanın** - Tam klasör yolunu yazın (C:\ veya /Users/... ile başlayan)
2. **Eğik Çizgi Yönü** - Windows'ta `\` yerine `/` da kullanabilirsiniz
3. **Raw String** - Yoldan önce `r` yazın: `r"C:\klasor\..."`
4. **`*.xlsx`** - Tüm Excel dosyalarını bulmak için `*.xlsx` yazmalısınız
5. **Çıktı Dosya Adı** - İstediğiniz bir dosya adı yazabilirsiniz (örn: `birlestirilmis.xlsx`)

### Adım 3: Programı Çalıştırın

```bash
python excel-birlestirici.py
```

Eğer hata alırsanız, kontrol edin:
- Excel dosyalarının klasörünün doğru yolda olduğundan emin olun
- Dosya yolunda yazım hatası olup olmadığını kontrol edin
- Çıktı klasörünün var olduğundan emin olun

## Örnek Kullanım 📝

**Başlangıç durumu:**
```
📁 exceller/
  ├─ dosya1.xlsx (100 satır)
  ├─ dosya2.xlsx (150 satır)
  └─ dosya3.xlsx (200 satır)
```

**Sonuç:**
```
📁 exceller/
  ├─ dosya1.xlsx
  ├─ dosya2.xlsx
  ├─ dosya3.xlsx
  └─ hepsiburada_birlesmis_dosya.xlsx (450 satır)
```

## Nasıl Çalışır? 🔧

1. **Dosyaları Bulma**: Belirtilen klasördeki tüm `.xlsx` dosyalarını bulur
2. **Okuma**: Her bir Excel dosyasını pandas DataFrame'e yükler
3. **Birleştirme**: Tüm DataFrameleri tek bir DataFrame'de birleştirir
4. **Kaydetme**: Birleştirilmiş veriyi yeni bir Excel dosyasına kaydeder

## Dikkat Edilmesi Gerekenler ⚠️

- Birleştirilecek Excel dosyaları **aynı sütun başlıklarına** sahip olmalıdır
- Program, belirtilen klasördeki **tüm `.xlsx` dosyalarını** otomatik olarak bulur
- Mevcut dosya varsa, üzerine yazılır
- `ignore_index=True` parametresi, satır numaralarını sıfırdan başlatır

## Sorun Giderme 🔍

### Python bulunamadı hatası
```bash
# Doğru Python versiyonunu kullanın
python3 excel-birlestirici.py
```

### ModuleNotFoundError: No module named 'pandas'
```bash
# pandas'i yükleyin
pip install pandas openpyxl
```

### Dosya yolu hatası
- Windows'ta: `r"C:\Kullanıcı\Klasör\*.xlsx"` format kullanın
- Mac/Linux'ta: `r"/Kullanıcı/Klasör/*.xlsx"` format kullanın
- Klasör yolunun doğru olduğundan emin olun

## Lisans 📄

MIT License - [LICENSE](LICENSE) dosyasına bakın

## Katkıda Bulunma 🤝

Katkılarınız hoşa gider! Lütfen:

1. Repository'i fork edin
2. Özellik dalı oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Dalı push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

## İletişim 📧

- **GitHub**: [@merenekiz](https://github.com/merenekiz)

## Destek 💬

Eğer bu proje işinize yaradıysa, lütfen ⭐ vermeyi unutmayın!

---

**Son Güncelleme**: 11 Şubat 2026
