# For building the encrypted string:
# Take every 2nd char from the string, then the other chars,
# that are not every 2nd char, and concat them as new String.
# Do this n times!
#
# Examples:
#
# "This is a test!", 1 -> "hsi  etTi sats!"
# "This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
# Write two methods:
#
# def encrypt(text, n)
# def decrypt(encrypted_text, n)
# For both methods:
# If the input-string is null or empty return exactly this value!
# If n is <= 0 then return the input text.

# def encrypt(text, n):
#     if not text or n <= 0:
#         return text
#     letters = list(text)
#     for _ in range(n):
#         temp1 = []
#         temp2 = []
#         for n, _ in enumerate(letters):
#             if n & 1:
#                 temp1.append(letters[n])
#             else:
#                 temp2.append(letters[n])
#         letters = temp1 + temp2
#     return ''.join(letters)
# from itertools import zip_longest
# from itertools import chain


def decrypt(encrypted_text, n):
    half, text_list = len(encrypted_text) // 2, list(encrypted_text)
    for _ in range(n):
        text_list[1::2], text_list[::2] = text_list[:half], text_list[half:]
    return ''.join(text_list)


# def decrypt(encrypted_text, n):
#     half = len(encrypted_text)//2
#     for _ in range(n):
#         decr = zip_longest(encrypted_text[half:], encrypted_text[:half])
#         encrypted_text = ''.join(filter(None, chain.from_iterable(decr)))
#     return encrypted_text


def encrypt(text, n):
    for _ in range(n):
        text = text[1::2] + text[::2]
    return ''.join(text)


# print(encrypt("This is a test!", 2))
# print(decrypt("s eT ashi tist!", 2))
a = "123456789"
o, l = len(a) // 2, list(a)
print(o)
print(l)
l[1::2], l[::2] = l[:o], l[o:]
print(l)

# Test.describe('Basic Tests')
# Test.assert_equals(encrypt("This is a test!", 0), "This is a test!")
# Test.assert_equals(encrypt("This is a test!", 1), "hsi  etTi sats!")
# Test.assert_equals(encrypt("This is a test!", 2), "s eT ashi tist!")
# Test.assert_equals(encrypt("This is a test!", 3), " Tah itse sits!")
# Test.assert_equals(encrypt("This is a test!", 4), "This is a test!")
# Test.assert_equals(encrypt("This is a test!", -1), "This is a test!")
# Test.assert_equals(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")
#
# Test.assert_equals(decrypt("This is a test!", 0), "This is a test!")
# Test.assert_equals(decrypt("hsi  etTi sats!", 1), "This is a test!")
# Test.assert_equals(decrypt("s eT ashi tist!", 2), "This is a test!")
# Test.assert_equals(decrypt(" Tah itse sits!", 3), "This is a test!")
# Test.assert_equals(decrypt("This is a test!", 4), "This is a test!")
# Test.assert_equals(decrypt("This is a test!", -1), "This is a test!")
# Test.assert_equals(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")
#
# Test.assert_equals(encrypt("", 0), "")
# Test.assert_equals(decrypt("", 0), "")
# Test.assert_equals(encrypt(None, 0), None)
# Test.assert_equals(decrypt(None, 0), None)
