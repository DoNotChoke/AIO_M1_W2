def count_dict(s):
    mp = {}
    for c in s:
        if c not in mp:
            mp[c] = 1
        else:
            mp[c] += 1
    mp = dict(sorted(mp.items()))
    return mp


s = "Happiness"
ans = count_dict(s)
# dict(sorted(ans.items(),key= lambda item:item[1])) : sort by value
# dict(sorted(ans.items()))  : sort by key
print(ans)
s = "smiles"
ans = count_dict(s)
print(ans)
