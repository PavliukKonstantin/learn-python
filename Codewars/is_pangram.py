# A pangram is a sentence that contains every single letter of the alphabet
# at least once. For example, the sentence
# "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).
#
# Given a string, detect whether or not it is a pangram.
# Return True if it is, False if not. Ignore numbers and punctuation.

# def is_pangram(s):
#     return set(string.lowercase) <= set(s.lower())

import string
from collections import Counter


def is_pangram(s):
    return not (Counter('abcdefghijklmnopqrstuvwxyz') - Counter(s.lower()))


# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# pangram = "The quick, brown fox jumps over the lazy dog!"
# c = Counter(alphabet) - Counter(pangram.lower())
# print(c)

print(string.ascii_lowercase)

# pangram = "The quick, brown fox jumps over the lazy dog!"
# Test.assert_equals(is_pangram(pangram), True)
