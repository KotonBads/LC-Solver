def parse():
    with open('wordlist-hypixel.txt') as f:
        f = f.readlines()

    return f[0].split(',')

def solve(_blanks):
    blanks = _blanks.lower().split('_')
    ans = [
        i if len(_blanks) == len(i) else ''
        for i in parse()
        if i.startswith(blanks[0]) and i.endswith(blanks[len(blanks) - 1]) 
        and blanks[1] in i and blanks[len(blanks) - 1] in i
    ]
    return list(filter(None, ans))