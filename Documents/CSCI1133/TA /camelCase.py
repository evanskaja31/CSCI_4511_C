def camelCaseSplit(string): return string[0] + "".join(map(lambda letter: [" a"," b"," c"," d"," e"," f",' g',' h',' i',' j',' k',' l',' m',' n',' o',' p',' q',' r',' s',' t',' u',' v',' w',' x',' y',' z','','','','','','',"a","b","c","d","e","f",'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'][ord(letter) - 65], list(string[1:])))

def camelCaseGen(string): return "".join(map(lambda word: word[0].upper() + word[1:], string.split(" ")))
