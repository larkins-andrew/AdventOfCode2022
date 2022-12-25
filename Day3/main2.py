f = open("input.txt")
lines = []
score = 0
for l in f:
    lines.append(l)
    if len(lines) == 3:
        for c in lines[0]:
            if c in lines[1] and c in lines[2]:
                if c.isupper():
                    score+=ord(c)-65+27
                else:
                    score+=ord(c)-96
                lines = []
                break
print(score)
f.close()
