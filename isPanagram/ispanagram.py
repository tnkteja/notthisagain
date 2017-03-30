# Complete the function below.
from collections import Counter
from string import ascii_lowercase

def  isPangram(strings):
    out=[]
    for string in strings:
        keys=Counter(string).keys()
        keys.sort()
        if keys[0]==' ':
            del keys[0]
        out.append(str(int(''.join(keys)==ascii_lowercase)))
    return ''.join(out)
        