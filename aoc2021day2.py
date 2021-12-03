#aoc2021day2.py
#from collections import deque

#part 1: given a list of vectors and values, compute the final distance and depth of travel. 
# Hash these by multiplying them together. 
#part 2: Rather than treating the depth values as a current state, treat them as a current angle. 
# modify both the distance and depth on "forward" commands. 

#part 1
from abc import abstractstaticmethod


distance = 0
depth = 0
cur = 0
step = 0
value = ""
command = []
#step 1

#step 2
aim = 0

step = 2

if step == 1: 
  with open("data/day2_input.txt", "r") as inputf:
    for value in inputf:
      step += 1
      command = value.split(" ")
      if command[0] == "forward":
        distance += int(command[1])
      elif command[0] == "down":
        depth += int(command[1])
      elif command[0] == "up":
        depth -= int(command[1])
      else:
        print(f"Error at step {step}")
      print(f"Step {step}: Command {command} distance {distance} depth {depth}")

  print(f'Number of steps {step}; final distance {distance}; final depth {depth}')
  print("Result: " + str(depth*distance))

if step == 2: 
  with open("data/day2_input.txt", "r") as inputf:
    for value in inputf:
      step += 1
      command = value.split(" ")
      if command[0] == "forward":
        distance += int(command[1])
        depth += int(command[1]) * aim
      elif command[0] == "down":
        aim += int(command[1])
      elif command[0] == "up":
        aim -= int(command[1])
      else:
        print(f"Error at step {step}")
      print(f"Step {step}: Command {command} distance {distance} aim {aim} depth {depth}")

  print(f'Number of steps {step}; final distance {distance}; final depth {depth}')
  print("Result: " + str(depth*distance))


