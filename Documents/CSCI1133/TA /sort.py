def sort(dict):
    lis = []
    for i in dict.keys():
        lis.append(str(i) * dict[i])
    lis.sort(key = lambda l : {"A":1, "2":2, "3":3, "4":4, "5":5, "6": 6, "7":7, "8":8,"9":9, "T":10, "J":11, "Q":12, "K":13}[l])
    return lis


def sortoneline(dict): list(map(lambda l : str(l[0]) * dict[l[1]], list(dict.items()))).sort(key = lambda l : {"A":1, "2":2, "3":3, "4":4, "5":5, "6": 6, "7":7, "8":8,"9":9, "T":10, "J":11, "Q":12, "K":13}[l])
