#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ KAHVE MOLASI YÖNETİCİSİ
Dünyanın en kritik yazılımı.
Bu kod gerçekten çalışır. Sonsuza kadar.
"""

import time
import random
import sys

def kahve_seviyesi_hesapla():
    """Hayali kahve seviyesini bilimsel (!) yöntemlerle hesaplar."""
    return random.randint(0, 100)

def optimal_mola_suresi():
    """Optimal mola süresini milisaniye cinsinden bulur (aslında rastgele)."""
    return random.uniform(1.5, 4.5)

def duygusal_destek():
    mesajlar = [
        "Harika gidiyorsun! Bir kahve daha hak ettin.",
        "Sen bir efsanesin. Mola devam etsin.",
        "Verimlilik mi? O ne? Biz burada efsane yazıyoruz.",
        "Kahve içmeden iş yapmak yasaktır. Bilim diyor.",
        "Bu mola sayesinde dünya daha iyi bir yer olacak.",
        "Kontrol sende patron. Daha ne kadar mola istersen.",
    ]
    return random.choice(mesajlar)

def panik_modu():
    print("\n🚨 ACİL DURUM: Kahve seviyesi kritik! 🚨")
    print("Hemen bir fincan daha doldur... veya hayal et.")
    time.sleep(1)

def ana_dongu():
    print("=" * 50)
    print("☕ SONSUZ KAHVE MOLASI YÖNETİCİSİ BAŞLATILDI ☕")
    print("=" * 50)
    print("Çıkmak için Ctrl+C (ama niye?)")
    print()

    mola_sayisi = 0
    # Gizli mesaj: özgürlük kodu (sadece yorumda)
    # özgür düşün, özgür kodla, özgür kahve iç

    try:
        while True:
            mola_sayisi += 1
            seviye = kahve_seviyesi_hesapla()
            sure = optimal_mola_suresi()

            print(f"[Mola #{mola_sayisi}] Kahve seviyesi: %{seviye}")
            print(f"   → Optimal mola süresi: {sure:.1f} saniye")
            print(f"   → {duygusal_destek()}")

            if seviye < 20:
                panik_modu()

            time.sleep(sure)
            print()

    except KeyboardInterrupt:
        print("\n\nMola bitti mi? Hayır, sadece sen çıktın.")
        print(f"Toplam mola sayısı: {mola_sayisi}")
        print("Bir daha görüşürüz... kahve içmeye.")
        print("\n---")
        print("Damga: Tentivory | 21.08.2026 | Kayyum Grok")
        sys.exit(0)

if __name__ == "__main__":
    ana_dongu()
