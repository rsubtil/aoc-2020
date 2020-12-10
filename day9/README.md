# Day 9: Encoding Error

## Problem statement (part 1)

Given a list of numbers, find the first number which is not a result of a sum of any of the previous 25 numbers.

### Input

The input looks like this:

```
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
```

For simplification, we're gonna use only the 5 previous numbers.

### Output

The first 5 numbers are `35`, `20`, `15`, `25` and `47`. We begin looking at numbers at the next position, so the 6th number, `40`. With the 5 numbers from before, we find that it's possible to get `40` by summing two of them: `15` and `25`. When we move to the next number, we always look at the 5 numbers from before; so, for our 7th number (`62`), the 5 numbers before are now `20`, `15`, `25`, `47` and `40`. We see that `47 + 15 = 62`, so this number is also valid.

We go on, and on, until we are at number `127`. The previous numbers are `95`, `102`, `117`, `150` and `182`. And there is no combination that yields `127`; therefore, we found our invalid number. We return it as the final answer.

## Problem statement (part 2)

Part 2 builds upon the results of part 1; having found the invalid number, we want to find the contiguous sequence before it. When we find it, we return the sum of the smallest and biggest numbers of that sequence.

### Output

With the same input as above, we know the invalid number is `127`. Now, we look at all the numbers below and start looking for a sequence that gives that number.

Starting from the first number `35`, we add up the next one. `35 + 20 = 55`. Still not our number, so we keep adding the next ones; `55 + 15 = 70`; `70 + 25 = 95`; `95 + 47 = 142`. At this point, `142` is bigger than our desired number, so we stop and start to test the next sequence, this time starting at the 2nd number: `20 + 15 = 35`; `35 + 25 = 60`; and so forth.

Eventually, we reach a sequence that start at the 3rd number that looks like `15 + 25 + 47 + 40 = 127`. We have reached our number. Now, we just return the sum of the smallest and biggest number: `15 + 47 = 62`, which is our final answer.

## Algorithm analysis

The algorithm implemented works as follows: iterating the array at idx=25, we check the sub-array before it (input[0:25]): we double iterate this array with **num1** *(from 0 to 23)* and **num2** *(from num1 to 24)* to find the sum. If we find one that equals our number, then we move on; if, however, after every possible combination, we can't replicate our number, we have found it, and return it immediately.

For part 2, we need to know the number from before. Having it, we create contiguous sub-sequences, starting from 0, and keep summing it up. If it surpasses our number, we know this sub-sequence doesn't not have it, so more to the next position. If if matches exactly our number, then we have found it; we just need to additionally compute the min and max values inside those elements, and finally returns it's sum.

### Time and memory complexity

For the analysis below, the following variables have these meanings:

- `n` means the size of the input

**Time** complexity is ugly, but probably very hard to overcome: we have to find a combination of numbers before it that sum up to our desired value. For that, we iterate **n-1** arrays **n** times. Therefore, our complexity is **O(n²)**. Likewise, for part 2, we have to find sub-sequences and sum the values, which is also **O(n²)**.

**Memory** complexity is normal though; we just need our input. So, **O(n)**.