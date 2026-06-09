l = ["Hello", "Hii", "who", "are", "you?"]
v = "AEIOUaeiou"
k = list(map(lambda x: ''.join(c for c in x if c not in v), l))
print(k)

l = ["Hello", "Hii", "who", "are", "you?"]
v = "AEIOUaeiou"
k = list(map(lambda x: ''.join(filter(lambda c: c not in v, x)), l))
m = list(map(lambda x: sum(map(ord, x)), k))
print(k)
print(m)
print(sum(m))

