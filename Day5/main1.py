f = open("input.txt")
boxes = ["" for i in range(9)]
#read boxes
for i in range(8):
    l = f.readline()
    index = 0
    for c in l:
        if c.isalpha():
            boxes[int((index)/4)]+=c
        index+=1

f.close()
