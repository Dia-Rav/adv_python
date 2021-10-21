from itertools import permutations

def get_permutations(s, n):
    ans = []
    for a, b in permutations(s, n):
        ans.append(a+b)
    return sorted(ans)

print (get_permutations("cat", 2) == ["ac", "at", "ca", "ct", "ta", "tc"] )
