s = 'café'
b = s.encode('utf8')
print(len(s))
print(len(b))

cafe = bytes('café', encoding='utf-8')
print(cafe)
[print(c) for c in cafe]
