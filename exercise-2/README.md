# Exercise 2

In this exercise, you'll practice writing conditional statements in Python. In particular, you should complete the following questions on [Codingbat](http://codingbat.com/python), which a website (one of many) for practicing basic programming.

1. [no_teen_sum](http://codingbat.com/prob/p100347)

def fix_teen(number): 
  if number >=13 and number <=19 and number != 15 and number != 16: 
    number = 0
  else: 
    number
  
  return number

def no_teen_sum(a, b, c):
  sum = fix_teen(a) + fix_teen(b) + fix_teen(c)
  return sum
  

2. [lucky_sum](http://codingbat.com/prob/p107863)

def lucky_sum(a, b, c):
  if a == 13: 
    sum = 0
  elif b == 13: 
    sum = a
  elif c == 13: 
    sum = a+b
  else: 
    sum = a+b+c
  return sum

3. [make_brick](http://codingbat.com/prob/p118406). Note that you may not need to use conditional statements for this, but it's good practice at the kind of logical, abstract thinking used in programming!

def make_bricks(small, big, goal):
	num_big = min(goal//5,big)
	num_small = goal - num_big*5
	return num_small <= small

Feel free to practice with the other problems as well!
