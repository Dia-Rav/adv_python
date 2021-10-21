from itertools import groupby

def compress_string(s):
    ans = []
    for i, j in groupby(s):
        ans.append((len(list(j)), i))
    return ans
print (compress_string('1222311') )
#[(1, '1'), (3, '2'), (1, '3'), (2, '1')]
