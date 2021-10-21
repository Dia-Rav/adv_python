
from itertools import combinations

def get_combinations(s, n):
    ans =[]
    for i in range (1, n+1):
        for x in combinations(s, i):
            ans.append (''.join(sorted(x)))
    ans = sorted(ans)
    ans.sort(key=lambda x: len(x))
    return ans

print(get_combinations("cat", 2)== ["a", "c", "t", "ac", "at", "ct"])
