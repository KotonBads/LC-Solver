def RemoveFromList(thelist, val):
    return [value for value in thelist if value != val]

def GetDic():
    try:
        with open("./DL.txt", "r") as dicopen:
            dicraw = dicopen.read()
        diclist = dicraw.split("\n")
        diclist = RemoveFromList(diclist, '')
        return diclist
    except FileNotFoundError:
        print("No Dictionary!")
        return 
    
def Word2Vect(word):
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    w = word.lower()
    wl = list(w)
    for item in wl:
        if item in l:
            ind = l.index(item)
            v[ind] += 1
    return v

def Vect2Int(vect):
    pv = 0
    f = 0
    for i in range(len(vect)):
        wip = (vect[i]*(2**pv))
        f += wip
        pv += 4
    return f
    
def Ints2Dic(dic):
    d = {}
    for i in range(len(dic)):
        v = Word2Vect(dic[i])
        Int = Vect2Int(v)
        if Int in d:
            tat = d.get(Int)
            tat.append(dic[i])
            d[Int] = tat
        else:
            d[Int] = [dic[i]]
    return d

def unscramble(word):
    """
    Original Code from https://github.com/tinmarr/Word-Unscrambler
    """
    return Ints2Dic(GetDic()).get(Vect2Int(Word2Vect(word.lower())))

# print(unscramble('lleh'))
# dic = GetDic()
# int2dic = Ints2Dic(dic)
# word = 'nopyht'
# print(int2dic.get(Vect2Int(Word2Vect(word))))