# KUDET: İkinci El Araç Değerleme Sistemi

## Özet
Bu çalışmada, Türkiye'deki ikinci el araç piyasasındaki fiyat tahminlemesi problemi ele alınmıştır. Web scraping yöntemiyle toplanan veriler üzerinde makine öğrenmesi teknikleri uygulanarak, araç özelliklerine dayalı fiyat tahmin modeli geliştirilmiştir.

## 👥 AUTHORS
- Binnur Soztutar (210316084) 
- Mert Çolakoğlu (220316081) 
- Emrah Tunç (210316082) 

##  Metodoloji
### Veri Seti
- Veri Kaynağı: arabam.com
- Örnek Sayısı: 1419 araç verisi
- Özellikler: 11 farklı araç özelliği:
  - model
  - model_detay
  - model_yili
  - sehir
  - ilce
  - ilan_turu
  - tip
  - marka
  - motor_hacmi
  - motor_tipi
  - donanim

### Model Performansı
1. Lineer Regresyon
   - R² Skoru: 0.88
   - RMSE: 144,789.99 TL
   - MSE: 20,964,140,158.92
   - Tolerance R² (±10.000 TL): 0.88
   - Tolerance % R² (±%50 fark): 0.95

   > 💡 Tolerance değerleri, modelin farklı hata tolerans seviyelerindeki performansını gösterir:
   > - ±10.000 TL toleransta R² = 0.88 → Model bu aralıkta tutarlı tahminler yapıyor
   > - ±%50 toleransta R² = 0.95 → Model geniş fiyat aralıklarında daha başarılı

2. Sınıflandırma (Random Forest)
   - Doğruluk Oranı: 0.82  
   - F1-Score: 0.81
   - Precision: 0.82 
   - Recall: 0.82

### 📈 Hata Analizi
- Ortalama Hata: 13,709 TL
- Medyan Hata: -0.80 TL
- Standart Sapma: 144,393 TL
- Minimum Hata: -749,767 TL
- Maksimum Hata: 703,801 TL

### 🔍 Model Özellikleri
- Özellik sayısı: 11 (1 sayısal, 10 kategorik)
- Veri seti büyüklüğü: 1419 araç
- Train/Test split: 80/20
- Pipeline kullanımı: StandardScaler ve OneHotEncoder

### 📊 Görselleştirmeler
- Gerçek vs Tahmin karşılaştırması
- Hata dağılımı histogramı
- Box plot analizi
- Fiyat aralıklarına göre performans grafikleri

### 🔄 Veri Ön İşleme
1. Aykırı Değer Analizi
   - IQR yöntemi ile aykırı değer tespiti
   - İstatistiksel analiz ve temizleme
2. Kategorik Değişken Dönüşümleri
   - One-Hot Encoding
   - Label Encoding
3. Özellik Mühendisliği
   - Özellik seçimi
   - Özellik ölçeklendirme

## Teknik Gereksinimler
### Yazılım Gereksinimleri
- Python 3.8.7
- Jupyter Notebook
- Gerekli kütüphaneler:
```bash
numpy>=1.24.3
pandas>=2.0.3
matplotlib>=3.7.1
seaborn>=0.12.2
scikit-learn>=1.3.0
jupyter>=1.0.0
```

## Kurulum ve Çalıştırma
1. Repoyu klonlayın:
```bash
git clone https://github.com/kudetx/kudet-arac-degerleme.git
cd kudet-arac-degerleme
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

3. Jupyter Notebook'ları çalıştırın:
```bash
jupyter notebook
```

### Karşılaştırmalı Analiz
#### Model Karşılaştırması
1. **Lineer Regresyon**
   - ✅ Yüksek R² skoru (0.88)
   - ✅ Düşük RMSE değeri (144,789.99 TL)
   - ✅ Geniş fiyat aralıklarında tutarlı performans
   - ⚠️ Aykırı değerlerden etkilenebilir

2. **Random Forest**
   - ✅ Yüksek doğruluk oranı (0.82)
   - ✅ Dengeli F1-Score (0.81)
   - ✅ Aykırı değerlere karşı dayanıklı
   - ⚠️ Hesaplama maliyeti daha yüksek

#### Kullanım Senaryoları
- **Lineer Regresyon:**
  - Genel fiyat tahminlemesi
  - Hızlı sonuç gerektiren durumlar
  - Veri seti temiz ve aykırı değerler temizlenmiş ise

- **Random Forest:**
  - Fiyat aralığı sınıflandırması
  - Aykırı değerlerin tam temizlenemediği durumlar
  - Daha yüksek doğruluk gerektiren özel durumlar

#### Performans Karşılaştırması
| Metrik | Lineer Regresyon | Random Forest |
|--------|------------------|---------------|
| R² / Accuracy | 0.88 | 0.82 |
| RMSE | 144,789.99 TL | - |
| Tolerans (±10k TL) | 0.88 | - |
| Tolerans (±%50) | 0.95 | - |
| F1-Score | - | 0.81 |
| Precision | - | 0.82 |
| Recall | - | 0.82 |

> 💡 **Tolerans Metrikleri Hakkında:**
> - ±10.000 TL toleranslı R² = 0.88: Model, 10 bin TL'lik hata payı içinde tutarlı tahminler yapıyor
> - ±%50 toleranslı R² = 0.95: Model, geniş fiyat aralıklarında daha başarılı performans gösteriyor
> - Bu değerler, modelin farklı hata tolerans seviyelerindeki güvenilirliğini gösterir

#### Model Seçim Kriterleri
- **Hız Öncelikli İse:** Lineer Regresyon
- **Doğruluk Öncelikli İse:** Random Forest
- **Dengeli Performans İçin:** Modellerin ensemble kullanımı

###  Güncellemeler ve Sürüm Bilgisi
- Versiyon: 1.0.0
- Son Güncelleme: Haziran 2023
- Python Versiyonu: 3.8.7+

## 📝 Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.