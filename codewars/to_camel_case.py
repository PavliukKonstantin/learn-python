# Complete the method/function so that it converts dash/underscore
# delimited words into camel casing. The first word within the output
# should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).
#
# Examples
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
#
# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
import re

# def to_camel_case(s):
#     return s[0] + s.title().translate(None, "-_")[1:] if s else s


def to_camel_case(text):
    return "".join((i.title(), i)[i == re.split("[-_]", text)[0]] for i in re.split("[-_]", text))


text = "the-stealth-warrior"
# text = ""
# text = "The_Stealth_Warrior"
# b = "".join((i.title(), i)[i == re.split("[-_]", text)[0]] for i in re.split("[-_]", text))
# b = "{0}{1}".format(
#     text[0],
#     text.title().translate(str.maketrans(dict.fromkeys('-_')))[1:]
# ) if text else text

print(b)

# test.describe("Testing function to_camel_case")
# test.it("Basic tests")
# test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
# test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
# test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
# test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")
