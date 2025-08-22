w = ["eat", "tea", "tan", "ate", "nat", "bat"]

a = {}
for word in w:
    s = ''.join(sorted(word))
    if s in a:
        a[s].append(word)
    else:
        a[s] = [word]
        
res = list(a.values())
print(res)