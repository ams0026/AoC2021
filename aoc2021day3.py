#aoc2021day3.py
#https://adventofcode.com/2021/day/3

#part 1: each of the lines in your input is a binary number. Process the data by byte position (column)
#for each column, set the same column in "gamma" to the predominant value in that column in the data. "epsilon" 
#will get the opposite value. Convert "gamma" and "epsilon" to decimal, multiply them, and return the result. 

from typing import ValuesView

rawdata = []
res = 0
maxpower = 0
rows = 0
gamma = 0
epsilon = 0

with open("data/day3_input.txt", "r") as inputf:
  for value in inputf:
    rows += 1
    value = value.strip()
    if maxpower == 0: maxpower = len(value)
    revvalue = ''.join( i for i in reversed(value))
    power, res = 0, 0
    for i in revvalue:
      res += int(i) * pow(2,power)
      power += 1
    rawdata.append(res)

# Part 1: Power consumption
for i in reversed(range(maxpower)):
  count = 0
  mask = pow(2, i)
  for x in rawdata:
    count += ( x >> i) & 1
  if count > (rows/2):
    gamma += mask
  else:
    epsilon += mask

print ("Part 1: gamma is " + str(gamma) + " and epsilon is " + str(epsilon) +". Result is: " + str(gamma * epsilon))

# Part 2: Life support

oxydata = rawdata.copy()
oxynext = []

for i in reversed(range(maxpower)):
  count = 0
  for x in oxydata:
    count += (( x >> i) & 1)
  if count >= (len(oxydata)/2):
    #more 1s than 0s (or equal #s)
    for x in oxydata:
      if (( x >> i) & 1) == 1:
        oxynext.append(x)
  else:
    #more 0s than 1s
    for x in oxydata:
      if (( x >> i) & 1) == 1:
        pass
      else:
        oxynext.append(x)
  oxydata = oxynext 
  oxynext = []
  if len(oxydata) == 1: break
print (f"Final oxydata is: {oxydata}")

co2data = rawdata.copy()
co2next = []
for i in reversed(range(maxpower)):
  count = 0
  for x in co2data:
    count += ( x >> i) & 1
  if count >= (len(co2data)/2):
    #more 1s than 0s (or equal #s)
    for x in co2data:
      if (( x >> i) & 1) == 1:
        pass
      else:
        co2next.append(x)
  else:
    #more 0s than 1s
    for x in co2data:
      if (( x >> i) & 1):
        co2next.append(x)
  co2data = co2next 
  co2next = []
  if len(co2data) == 1: break
print (f"Final co2data is: {co2data}")
print ("Life support rating is: " + str(oxydata[0] * co2data[0]))

