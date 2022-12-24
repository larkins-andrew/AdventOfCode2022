f = open("input.txt")
# A - Rock - 1
# B - Paper - 2
# C - Scissors - 3
# X - Lose - 0
# Y - Draw - 3
# Z - Win - 6
score = 0
scores = {
'A':1,
'B':2,
'C':3,
'X':0,
'Y':3,
'Z':6
}
for l in f:
    score+=scores[l[2]]
    #draw
    if l[2] == 'Y':
        score+=scores[l[0]]
    #win
    elif l[2] == 'Z':
        score+=scores[l[0]]%3+1
    #loss
    elif l[2]=="X":
        score+=(scores[l[0]]-2)%3+1
print(score)
