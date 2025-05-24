
import json
from collections import Counter

DOSYA_ADI = "selections.json"

def secimi_kaydet(yeni_secim):
    try:
        with open(DOSYA_ADI, "r") as f:
            veriler = json.load(f)
    except FileNotFoundError:
        veriler = []

    veriler.append(yeni_secim)

    with open(DOSYA_ADI, "w") as f:
        json.dump(veriler, f)

def oy_say():
    try:
        with open(DOSYA_ADI, "r") as f:
            veriler = json.load(f)
    except FileNotFoundError:
        return {}

    tum_gunler = [gun for secim in veriler for gun in secim]
    return Counter(tum_gunler)
