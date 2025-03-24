# 🚇 Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)

## 📌 Proje Açıklaması
Bu proje, bir metro ağı üzerinde **en hızlı** ve **en az aktarmalı** rotayı bulmaya yönelik bir simülasyon geliştirmektedir. 
Proje, **graf veri yapısı** kullanarak metro istasyonlarını ve hatlarını modelleyerek en uygun rotaları hesaplar.

## 🛠 Kullanılan Teknolojiler ve Kütüphaneler
- **Python**: Proje dili
- **collections** (deque, defaultdict): BFS algoritması ve istasyon bağlantıları için kullanıldı
- **heapq**: A* algoritması için öncelik kuyruğu yapısını sağlamak için kullanıldı

## 🔍 Algoritmaların Çalışma Mantığı

### 🔵 BFS (Breadth-First Search) – En Az Aktarmalı Rota
- Başlangıç istasyonu bir **kuyruğa (deque)** eklenir.
- **Ziyaret edilen istasyonlar takip edilir**.
- **Komşu istasyonlar keşfedilir**, aktarma noktaları kontrol edilerek en az durak sayısına sahip yol bulunur.
- **Sonuç**: En az aktarmalı rota listesi döndürülür.

### 🟢 A* (A-Star) – En Hızlı Rota
- **Öncelik kuyruğu (heapq)** ile en kısa sürede gidilebilecek istasyonları sıralar.
- **Toplam süreyi hesaplar** ve **en düşük süreli** rotayı tercih eder.
- **Ziyaret edilen istasyonlar takip edilir**, böylece gereksiz tekrarlar önlenir.
- **Sonuç**: En hızlı rota ve toplam süre döndürülür.

## 🔄 Örnek Kullanım ve Test Sonuçları
=== Test Senaryoları ===

1. Kızılay'dan OSB'ye En Az Aktarmalı Rota:
Kızılay -> Ulus -> Demetevler -> OSB

2. Kızılay'dan OSB'ye En Hızlı Rota:
En hızlı rota (18 dakika): Kızılay -> Ulus -> Demetevler -> OSB


