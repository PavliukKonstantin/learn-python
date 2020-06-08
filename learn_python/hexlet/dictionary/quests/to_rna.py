# ДНК и РНК это последовательности нуклеотидов.
#
# Четыре нуклеотида в ДНК это аденин (A), цитозин (C), гуанин (G) и тимин (T).
#
# Четыре нуклеотида в РНК это аденин (A), цитозин (C), гуанин (G) и урацил (U).
#
# Цепь РНК составляется на основе цепи ДНК последовательной
# заменой каждого нуклеотида:
#
# G -> C
# C -> G
# T -> A
# A -> U
# to_rna.py
# Напишите функцию to_rna, которая принимает на вход цепь ДНК
# и возвращает соответствующую цепь РНК (совершает транскрипцию РНК).


def to_rna(dna):
    dna_to_rna = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }
    rna = []
    for nucl in dna:
        rna.append(dna_to_rna[nucl])
    return ''.join(rna)


print(to_rna('ACGTGGTCTTAA'))


def test_to_rna():
    assert to_rna("C") == "G"
    assert to_rna("G") == "C"
    assert to_rna("T") == "A"
    assert to_rna("A") == "U"
    assert to_rna("ACGTGGTCTTAA") == "UGCACCAGAAUU"


test_to_rna()
