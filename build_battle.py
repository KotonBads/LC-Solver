def parse():
    with open('wordlist-hypixel.txt') as f:
        f = f.readlines()

    return f[0].split(',')

def solve(_blanks):
    blanks = _blanks.split('_')
    for i in parse():
        if i.startswith(blanks[0]) and i.endswith(blanks[len(blanks) - 1]):
            print(i)

solve('cal__d_r')