from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması ile en az aktarmalı rotayı bulur."""
        
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        
        kuyruk = deque([(baslangic, [baslangic])])
        ziyaret_edildi = set()
        
        while kuyruk:
            mevcut, yol = kuyruk.popleft()
            
            if mevcut == hedef:
                return yol  # En az aktarmalı rota bulundu
            
            if mevcut in ziyaret_edildi:
                continue
            
            ziyaret_edildi.add(mevcut)
            
            for komsu, _ in mevcut.komsular:
                if komsu not in ziyaret_edildi:
                    kuyruk.append((komsu, yol + [komsu]))
        
        return None  # Rota bulunamazsa None döndürülür

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması ile en hızlı rotayı bulur."""
        
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        
        pq = [(0, id(baslangic), baslangic, [baslangic])]
        ziyaret_edildi = {}
        
        while pq:
            toplam_sure, _, mevcut, yol = heapq.heappop(pq)
            
            if mevcut == hedef:
                return yol, toplam_sure  # En hızlı rota bulundu
            
            if mevcut in ziyaret_edildi and ziyaret_edildi[mevcut] <= toplam_sure:
                continue
            
            ziyaret_edildi[mevcut] = toplam_sure
            
            for komsu, sure in mevcut.komsular:
                heapq.heappush(pq, (toplam_sure + sure, id(komsu), komsu, yol + [komsu]))
        
        return None  # Rota bulunamazsa None döndürülür

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Bağlantılar ekleme
    metro.baglanti_ekle("K1", "K2", 4)
    metro.baglanti_ekle("K2", "K3", 6)
    metro.baglanti_ekle("K3", "K4", 8)
    
    # Test Senaryoları
    print("\n=== Test Senaryoları ===")
    
    print("\n1. Kızılay'dan OSB'ye En Az Aktarmalı Rota:")
    rota = metro.en_az_aktarma_bul("K1", "K4")
    if rota:
        print(" -> ".join(istasyon.ad for istasyon in rota))
    else:
        print("Rota bulunamadı!")
    
    print("\n2. Kızılay'dan OSB'ye En Hızlı Rota:")
    sonuc = metro.en_hizli_rota_bul("K1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(istasyon.ad for istasyon in rota))
    else:
        print("Rota bulunamadı!")
