# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells
# and carries the "instructions" for the development and functioning of
# living organisms.

# If you want to know more http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other,
# as "C" and "G". You have function with one side of the DNA
# (string, except for Haskell); you need to get the other complementary side.
# DNA strand is never empty or there is no DNA at all
# (again, except for Haskell).


def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG", "TAGC"))


print(DNA_strand("ATTGC"))


# Test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
# Test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
# Test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")
