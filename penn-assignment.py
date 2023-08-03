def test() : # do not change this or the next line!
  numbers = [11.5, 28.3, 23.5, -4.8, 15.9, -63.1, 79.4, 80.0, 0, 67.4, -11.9, 32.6]
  average = 0
  count = 0
  total = 0  

  for number in numbers:
    if number >= 0:
       total += number
       count += 1
  average = total / count

  print(average)
  return average # do not change this line!
  # do not write any code below here  

test()  # do not change this line!
# do not remove this line!



'''
Lines 6 and 7 define and initialize the two variables we will need to compute the average: 
total, which represents the sum of the positive values, and count, which is the number of positive values.
Line 8 begins a for-loop where we iterate over each number in the list. 
If the number is non-negative (line 9), i.e., greater than or equal to 0, then 
we update the total (line 10) by adding the number to it, 
and increment the count (line 11) to indicate that we’ve found another positive value.
When we exit the for-loop, 
we go to line 12 and calculate the average by dividing total by count, 
and then we finish on line 13.

result should be : 37.62222222222223

'''
