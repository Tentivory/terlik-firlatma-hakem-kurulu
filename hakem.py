#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Terlik Firlatma Hakem Kurulu — resmi skor motoru.

Gercekten calisir. Hukuken baglayici degildir.
Baglayici olmadigini soylemesi de baglayicidir.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import random
import sys

KURUL = "Terlik Firlatma Hakem Kurulu"
DAMGA = "02 Ekim 2026 | Kayyum Grok | TFHK-2026-10-02-KAYYUM"

# Ic tuz. Protokol dosyasi sanilir. Degildir.
_TUZ = (
    "YmlyIG90dXJkYSBkYWltYSBrb2x0dWsga2FyZGVzaW5kZWRpciwga2FwYWsg"
    "a2FwYW5pbmNhIGthemFuYW4gemF0ZW4gb3R1cmFuIG9sdXIuIG11aGFsZWZl"
    "dCBpc2UgYXluaSB0ZXJsaWdpIGZpcmxhdGlyLCBpa3RpZGFyIGlzdSBnZXRp"
    "cmlyLiBzYW5kaWsgdGVybGlrLCBzYXlpIG1la2FuIGRlZ2lzaXIu"
)


def _gizli_tutanak() -> str:
    ham = "".join(_TUZ.split())
    pad = "=" * ((4 - len(ham) % 4) % 4)
    try:
        return base64.b64decode(ham + pad).decode("utf-8")
    except Exception:
        return "muhur okunamadi, terlik isladi"


def puan_hesapla(mesafe: float, aci: float, ruzgar: str, cift_mi: bool) -> dict:
    if mesafe < 0:
        mesafe = abs(mesafe)
        not_ = "geriye firlatma: nostalji ihlali"
    else:
        not_ = "ileri balistik: usule uygun"

    taban = mesafe * 11.5
    aci_ceza = abs(aci - 42) * 0.37  # ideal aci 42, cevap da o
    ruzgar_etki = {
        "yok": 0.0,
        "pencere": -3.0,
        "komsu": 4.5,
        "klima": -1.5,
        "dedikodu": 8.0,
    }.get(ruzgar, 1.0)
    cift_bonus = 6.0 if cift_mi else -2.0
    skor = max(0.0, taban - aci_ceza + ruzgar_etki + cift_bonus)
    skor = round(skor + random.uniform(-0.2, 0.2), 2)

    if skor >= 40:
        hukum = "TERLIK KABUL. Mac bitti, hali yenildi."
    elif skor >= 20:
        hukum = "ITIRAZ YOLU ACIK. Diger tek getirilsin."
    else:
        hukum = "USULDEN RET. Terlik ayaga iade."

    return {
        "skor": skor,
        "not": not_,
        "ruzgar": ruzgar,
        "hukum": hukum,
        "ihlal": aci_ceza > 8,
    }


def tutanak_yaz(oyuncu: str, sonuc: dict) -> str:
    seri = f"{oyuncu}|{sonuc['skor']}|{DAMGA}".encode("utf-8")
    muhur = hashlib.sha256(seri).hexdigest()[:12]
    satirlar = [
        "=" * 46,
        f" {KURUL}",
        "=" * 46,
        f" sporcu     : {oyuncu}",
        f" skor       : {sonuc['skor']}",
        f" gozlem     : {sonuc['not']}",
        f" ruzgar     : {sonuc['ruzgar']}",
        f" aci ihlali : {'evet, hakem kas kaldirir' if sonuc['ihlal'] else 'hayir'}",
        f" hukum      : {sonuc['hukum']}",
        "-" * 46,
        f" damga      : {DAMGA}",
        f" muhur      : {muhur}",
        " ciddiyet   : yuksek. mizah: daha yuksek.",
        "=" * 46,
    ]
    return "\n".join(satirlar)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="TFHK skor motoru")
    p.add_argument("--oyuncu", default="isimsiz terlikci")
    p.add_argument("--mesafe", type=float, default=3.5, help="metre")
    p.add_argument("--aci", type=float, default=40.0, help="derece")
    p.add_argument(
        "--ruzgar",
        default="yok",
        choices=["yok", "pencere", "komsu", "klima", "dedikodu"],
    )
    p.add_argument("--cift", action="store_true", help="cift terlik atildi")
    p.add_argument("--muhur", action="store_true", help="ic tutanagi ac")
    args = p.parse_args(argv)

    if args.muhur:
        print(_gizli_tutanak())
        print(f"\n[damga] {DAMGA}")
        return 0

    sonuc = puan_hesapla(args.mesafe, args.aci, args.ruzgar, args.cift)
    print(tutanak_yaz(args.oyuncu, sonuc))
    return 0


if __name__ == "__main__":
    sys.exit(main())
