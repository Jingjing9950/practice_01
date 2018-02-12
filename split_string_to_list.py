# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source,splitlist):
    for spl in splitlist:
        for word in source:
            if word == spl:
                source = source.replace(spl,'abc')
    result = source.split('abc')
    while '' in result:
        result.remove('')
    return result


out = split_string("This is a test-of the,string separation-code!"," ,!-")
print(out)