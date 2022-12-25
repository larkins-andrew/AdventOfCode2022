f = open("input.txt")
score = 0
for l in f:
    item = ''
    c1 = l[:int(len(l)/2)]
    c2 = l[int(len(l)/2):]
    for c in c1:
        if c in c2:
            item = c
    if item.isupper():
        print(item, ord(item)-65+27)
        score+=ord(item)-65+27
    else:
        print(item, ord(item)-96)
        score+=ord(item)-96
print(score)
f.close()
