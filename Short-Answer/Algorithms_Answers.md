#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)Linear - O(n): 
This is linear because n is a constant variable.


b)Quadratic - O(n^2):
Due to the nested for loops, this is quadratic due to n being a given range.


c)Linear - O(n):
This is linear because bunnies is always a set number, so despite being called recursively, bunnies goes down in a line to base.

## Exercise II

We know that the egg will break at floor 'f' or higher.  This means that we need to go through the floors until we find f.  A binary search will help us narrow it down until we can determine which of the floors is f.

So if the list of floors = n, we would start by dropping an egg off of n//2 (call that starting_floor). So starting_floor = n//2
If the egg breaks, we then move on to do the same with :starting_floor
If the egg does not break, we move on to do the same with starting_floor:
We run this loop until there are only two floors left.
If the current floor is j and the egg breaks, the answer is j-1, if it does not, the answer is j.

This is O(n) because we are splitting in half, the time goes in a straight line.
