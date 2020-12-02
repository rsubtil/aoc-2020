# Day 1: Report Repair

## Problem statement (part 1)

Given a list of various numbers, find the one combination of two numbers that, when summed up, equal `2020`. Return those numbers multiplied.

### Input

We receive a text file with a number on each line:

```
1721
979
366
299
675
1456
```

### Output

With the input above, we find that `1721` and `299` are the only numbers that, when summed up, equal `2020`. With the numbers found, just return their product: `1721 * 299 = 514579`

## Problem statement (part 2)

The problem is the same in every way, with only **one** difference: it now wants to find the combination of three numbers that, summed up, equal `2020`.

## Algorithm analysis

The algorithm used to solve this is very naive. For the **first part**, it simply iterates through two indices:

- **i1**: from 0 to len(input) - 1
- **i2**: from i1+1 to len(input)

Having the loop traversing the array in this way, it's just a matter of testing whether those two numbers add up to `2020`; when they do, compute their product and finish.

For **part two**, the logic is the same, but since we now are searching for **three** numbers, we just add another loop to the previous one:

- **i1**: from 0 to len(input) - 2
- **i2**: from i1+1 to len(input) - 1
- **i3**: from i2+1 to len(input)

### Time and memory complexity

For the analysis below, the following variables have these meanings:

- `n` means the size of the input

**Time** complexity is very bad for this approach:

- For **part one**, we basically traverse the array for each array element, therefore **O(n²)**
- For **part two**, we traverse the array for any traversal from before, therefore **O(n³)**

**Memory** complexity, on the other hand, is **O(n)** on both, since we're not using any additional memory apart from holding our input array.