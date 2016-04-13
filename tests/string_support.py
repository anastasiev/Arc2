import io



def getStringFromSerialyser(fileName = "matches.json"):
    out = io.StringIO()
    with open(fileName, 'rt') as f:
        for line in f:
            out.write(line)

    return out