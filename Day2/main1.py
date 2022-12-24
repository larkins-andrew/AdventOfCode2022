f = open("input.txt")
# A, X - Rock
# B, Y - Paper
# C, Z - Scissors
score = 0
for l in f:
    if 'X' in l:
        score+=1
    elif 'Y' in l:
        score+=2
    elif 'Z' in l:
        score+=3
    if l == "A Y\n" or l=="B Z\n" or l=="C X\n":
        score+=6
    elif l=="A X\n" or l=="B Y\n" or l=="C Z\n":
        score+=3
print(score)
f.close()
