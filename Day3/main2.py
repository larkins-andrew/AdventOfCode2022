f = open("input.txt")
lines = []
score = 0
for l in f:
    lines.append(l)
    if len(lines) == 3:
        for c in lines[0]:
            if c in lines[1] and lines[2]:
                if c.isupper():
                    print(c, ord(c)-65+27)
                    score+=ord(c)-65+27
                else:
                    print(c, ord(c)-96)
                    score+=ord(c)-96
                lines = []
                break
print(score)
f.close()
