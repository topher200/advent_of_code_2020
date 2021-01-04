# Day 1: Report Repair, part B

## Problem
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

_the sample from before:_
```
1721
979
366
299
675
1456
```

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?


## Solution Thoughts

I don't see a way to do this which isn't O(n^2), which seems like I must be missing something.

To find the third value in a triple, it seems like you should analyze all the previous combinations of values. In pseudocode:

```
- start an empty set (S)
- iterate through the list
  - for each value (X), check if '2020 - X' appears in S. if found, that's the value we need
  - if it's not found, iterate through each of the previous values (Y). sum each X + Y and add the result to S <--- this part seems to be O(n^2)
```

The part highlighted above seems to be O(n^2) because we need to do something to every element of the list as each new element is compared. It also requires O(n^2) space to store S.

I'm going to go with this solution anyway while I try to thing of a better one.
