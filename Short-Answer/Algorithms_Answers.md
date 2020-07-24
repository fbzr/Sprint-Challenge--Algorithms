#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

```python
# time complexity is O(n)
a = 0
while (a < n * n * n):
    a = a + n * n

# after every comparation it gives to 'a' one part of the value that we are comparing 'a' to. That basically means that we are anulling that amount from the comparation
# O(3n - 2n) => O(n)
```

b)

```python
sum = 0
for i in range(n): # O(n)
    j = 1
    while j < n: # O(log n)
         # this will happen the number of times we can multiply j to 2 having that result smaller than 'n'
        j *= 2
        sum += 1

    # O(n) * O(log n) = O(n log n)
```

c)

```python
def bunnyEars(bunnies):
    if bunnies == 0:
    return 0

    return 2 + bunnyEars(bunnies-1)

# The function is being called 'n' times before reaching the base case. O(n)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

```python
# Objective: Find lowest floor that eggs get broken when dropped ('f').
#   - floors[i].drop() == 'break' and floors[i-1].drop() == 'does not break'
# Do that minimizing dropped + broken eggs

# Thoughts:
# We are calculating drops + breaks
# List of Floors are in order
# - If I start from the first floor to the last or untill find the right one, worst case is O(n) -
# - If I start from the middle and every time ignore half of 'n', wort case is O(log n) - Better than previous = Binary Search

# receive a ordered list representing the building of part of it and its floors (building)
  # find the middle of the building by splitting the length of the list by 2: len(building) // 2
  # save it in a variable (f)
  # drop an egg from that floor: building[f]
  # if egg breaks:
    # call same function passing current list from its start (index 0) to the current floor (non inclusive): function(building[:f])
  # else: // egg didn't break
    # throw another egg from floor above the current floor (f+1)
    # if egg breaks:
      # found the lowest floor that eggs get broken
      # return f+1
    # else:
      # call function passing list from floor above current floor (f+1) to the end of list: function(building[f+1:])
```
