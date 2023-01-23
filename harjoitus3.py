from pprint import pprint
from time import ctime
import time

aikaleima = time.time()

esimerkki_kuvio = {
    "nimi": "Esimerkki",
    "tyyppi": "monikulmio",
    "luotu": ctime(aikaleima),
    "pisteet": [
        {"x": 10, "y": 20, "z": 30},
        {"x": 20, "y": 5, "z": 10},
        {"x": 30, "y": 15, "z": 20},
    ]
}

pprint(esimerkki_kuvio, sort_dicts=False)
