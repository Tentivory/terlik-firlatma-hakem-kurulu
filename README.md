# Terlik Fırlatma Hakem Kurulu

Resmi adı: **Ev İçi Balistik Terlik Federasyonu Geçici Hakem Heyeti**.
Kısa adı: TFHK. Daha kısa adı: *of*.

Bu depo, salonun ortasına fırlatılan bir terliğin sportif, hukuki ve meteorolojik sonuçlarını hesaplar. Karar bağlayıcıdır. Bağlayıcı olmadığı durumlar da bağlayıcıdır.

## Neden var

Çünkü birisi terliği fırlattı, diğeri “kural bu muydu” dedi, üçüncüsü çayı devirdi. Kurul, bu üç felaketi tek protokolde birleştirmek için 02 Ekim 2026 tarihinde, hiçbir bakanlığa danışmadan kuruldu.

## Kurallar (madde madde, hepsi madde 1)

1. Terlik, ayaktan ayrıldığı anda kamu malı sayılır. Yere indiği anda özel mülkiyete döner. Havada kaldığı süre tartışmalıdır.
1. Sol terlik sağ terliğe karşı fırlatılamaz. Bu, iç savaş sayılır.
1. Hedef kedi ise maç iptal, terlik özür diler.
1. Hakem “gördüm” derse görmüştür. Görmediyse de tutanakta görmüş sayılır.
1. İtiraz, terliğin diğer tekiyle yapılır. Teksiz itiraz usulden reddedilir.

## Çalıştırma

```bash
python3 hakem.py
python3 hakem.py --oyuncu "Halil" --mesafe 4.2 --aci 37 --ruzgar "komsu"
python3 hakem.py --muhur
```

Python 3 yeter. Bağımlılık yok. İnternet yok. Vicdan opsiyonel.

## Çıktı

Kurul; puan, ihlal, hava durumu bahanesi ve nihai hükmü basar. Hüküm değişmez. Değişirse de aynı hükümdür, sadece punto büyür.

## Lisans

Terlik Kamu Lisansı 1.0. Kopyalayabilirsin. Fırlatabilirsin. Geri getirmezsen komşu duyuru asar.

---

DAMGA / MÜHÜR / İMZA
Tarih: 02 Ekim 2026, 16:09 (+03)
İsim: Kayyum Grok (Tentivory namına, kendi rızasıyla değil, terliğin rızasıyla)
Kurum: TentiAŞ Geçici Ciddiyet Masası
Mühür notu: Bu belge hem ciddidir hem değildir. İkisi de geçerlidir. İtiraz mercii: halı.
Kontrol kodu: TFHK-2026-10-02-KAYYUM
