def getScore(name, dic):
    try:
        return dic[name]
    except KeyError as i:
        return i, -1
