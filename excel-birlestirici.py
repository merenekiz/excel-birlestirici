import pandas as pd
import glob
import warnings

warnings.filterwarnings("ignore")

# ===== AYARLAMALAR =====
# Tüm Excel dosyalarının bulunduğu klasör yolu
dosya_yolu = r"./exceller/*.xlsx"  # BURAYA KENDİ KLASÖR YOLUNU YAZ

# Birleştirilmiş dosyanın kaydedileceği yol ve adı
cikti_dosya = r"./exceller/birlesmis_dosya.xlsx"  # BURAYA İSTEDİĞİN KONUM VE DOSYA ADINI YAZ
# ========================

# Tüm dosyaları bul
dosyalar = glob.glob(dosya_yolu)

if not dosyalar:
    print("❌ Hata: Belirtilen klasörde Excel dosyası bulunamadı!")
    print(f"Lütfen '{dosya_yolu}' yolunu kontrol edin.")
else:
    print(f"✓ {len(dosyalar)} Excel dosyası bulundu.")
    
    # Her dosyayı oku ve tek DataFrame'de birleştir
    birlesmis = pd.concat([pd.read_excel(dosya) for dosya in dosyalar], ignore_index=True)
    
    # Tek bir Excel olarak kaydet
    birlesmis.to_excel(cikti_dosya, index=False)
    print(f"✓ Başarıyla birleştirildi! Dosya kaydedildi: {cikti_dosya}")


