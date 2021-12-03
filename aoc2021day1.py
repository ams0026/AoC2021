#aoc2021day1.py
from collections import deque

#part 1: in a list of 2000 numbers, count the number of times a number is larger than its predecessor. 
#part 2: in the same list, compute a rolling sum of 3 numbers. Count the number of times the current sum 
# is larger than the previous sum. 

#part 1
total = 0
ups = 0
cur = 0
old = None
#part 2
roll=deque()
# "deck" -- double-ended queue. enables popleft()
currollsum=0
oldrollsum=None
up3s = 0

with open("day1_1_input.txt", "r") as inputf:
  for value in inputf:
    #implied line read. read() will grab the whole file
    total += 1
    cur = int(value)
    roll.append(cur)
    if old != None:
      if cur > old:
        ups += 1 
    if len(roll) <4:
      currollsum = sum(roll)
      #sum() allows you to sum members of a list... like in Excel
    else:
      roll.popleft()
      oldrollsum = currollsum
      currollsum = sum(roll)
      if currollsum > oldrollsum:
        up3s += 1
    old = cur

print(f'Count of total elements {total}; Count of one-step increases {ups}; Count of 3-step increases {up3s}')
#nice mechanism to format output.

#breakpoint() in the code sets a breakpoint. also vscode does a nice job of watching specified variables



