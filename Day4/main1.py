f = open("input.txt")
count = 0
for l in f:
    asgn = [i.split('-') for i in l.strip().split(',')]
    asgn = [[int(i[0]), int(i[1])] for i in asgn]
    if asgn[0][0]>= asgn[1][0] and asgn[0][1] <= asgn[1][1] or asgn[0][0]<=asgn[1][0] and asgn[0][1] >= asgn[1][1]:
        count+=1
print(count)

f.close()
