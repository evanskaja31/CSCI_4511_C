from functools import reduce

def wordlist(string):return list(set(("".join(list(filter(lambda x : x.isalpha() or x == " ", string.lower()))).split())))
