def strip_and_remove(string, word):
    newStr= string.replace(word, " ")
    return newStr.strip()
h="   Rajan is a good boy   "
n=strip_and_remove(h, "Rajan")
print(n)
 