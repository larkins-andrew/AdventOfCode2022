f = open("input.txt")
elves = [0]
for l in f:
  if l == '\n':
    elves.append(0)
  else:
    elves[-1] += int(l)
final = max(elves)
elves.remove(max(elves))
final += max(elves)
elves.remove(max(elves))
final += max(elves)
print(final)
f.close()
