# from os import sys
# sys.path.insert(0, ".")
# from codewars.top_3_words import top_3_words
from collections import Counter
from re import findall


def top_3_words(s):
    return [k for k, _ in Counter(findall("'?[a-z]+'*[a-z]*'?", s.lower())).most_common(3)]


def test_assert_equals():
    assert top_3_words("a a a  b  c c  d d d d  e e e e e") == ["e", "d", "a"]
    assert top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e") == [
        "e", "ddd", "aa"]
    assert top_3_words("  //wont won't won't ") == ["won't", "wont"]
    assert top_3_words("  , e   .. ") == ["e"]
    assert top_3_words("  ...  ") == []
    assert top_3_words("  '  ") == []
    assert top_3_words("  '''  ") == []
    assert top_3_words("  //wont won't won't ") == ["won't", "wont"]
    assert top_3_words("""In a village of La Mancha, the name of which I have
     no desire to call to mind, there lived not long since one of those
    gentlemen that keep a lance in the lance-rack, an old buckler, a lean
    hack, and a greyhound for coursing. An olla of rather more beef than
    mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays,
    and a pigeon or so extra on Sundays, made away with three-quarters
    of his income.""") == ["a", "of", "on"]
