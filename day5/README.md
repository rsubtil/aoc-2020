# Day 5: Binary Boarding

## Problem statement (part 1)

Given a list of boarding passes, find the biggest seat ID from the tickets you have.

### Input

The input are rows of ticket places of this format:

```
FBFBBFFRLR
```

The way this airline prints boarding passes might be weird for the common folks, but for computer guys this is a very pleasant way to codify it; the ticket is using **binary space partitioning**, that is, it codifies the steps to reach a specific seat.

The first 7 characters consist of either `F` *(lower half)* and `B` *(upper half)*. The remaining 3 consist of only `L` *(lower half)* and `R` *(upper half)*. From this information, we can deduct there exists a total of 128 rows of seats (2⁷), and that each row contains 8 seats (2³).

### Output

We begin by defining our range for the rows. There are, in total, 128 rows of seats, so we set our lower and upper limits *(note that seats begin at 0)*: `0`-`127`.

Our first character is `F`, meaning our seat is in the lower half of the division. Divisions are made in the middle *(hence the binary in binary partitioning)*, so our ranges are either `0`-`63` or `63`-`127`. Since the seat is in the lower part, we discard `63`-`127`, and work with `0`-`63`.

The next character is `B`, so now our seat is in the upper half of this new range. Therefore, we divide in half again and use the second part: `32`-`63`.

And so on:

- `F` -> `32`-`47`	*(16 spots)*
- `B` -> `40`-`47`	*(8 spots)*
- `B` -> `44`-`47`	*(4 spots)*
- `F` -> `44`-`45`	*(2 spots)*
- `F` -> `44`	*(1 spot)*

So, after seven iterations, we find that our seat is in row 44. Now we just need to find the column, which follows the exact same logic as above:

- Starting with range `0`-`7`	*(8 spots)*
- `R` -> `4`-`7`	*(4 spots)*
- `L` -> `4`-`5`	*(2 spots)*
- `R` -> `5`	*(1 spot)*

And so, our seat is in row `44`, column `5`. To conclude, we have to find this seat's ID, which is very simple: multiply the row by `8` and add it the column. For our example, `44 * 8 + 5` = `357`.

Since this example only uses one ticket for simplicity, this seat ID's is the biggest one. Final answer is `357`.

## Problem statement (part 2)

The problem, for part 2, builds upon the results of the first part; we now want to find our seat, which should be the missing seat among all the other we scanned. The whole list isn't occupied though, as some of the seats at the front and back don't actually exists.

## Algorithm analysis

The algorithm works like this: for each "ticket", compute the row and column using **binary partitioning** *(implemented with some kinda ugly math)*. Having those values, we can calculate the seat ID. For the first part, we're interested in knowing the biggest seat ID that exists.

The second part, *though*, was quite interesting; to implemented it, I added some additional logic to the first part to **mark** any seats that have been *taken*. So, for the second part, I already had a list of *vacant* spots. However, we're told that some of the very *first* or *last* seats we can calculate, don't *actually* **exist**. That means the list will contain rows and rows of seats that are marked as **empty**. To find our *true* spot, we simply check for any single value that is not **contiguous** to it's adjacent neighbors; this works because we're told that *"the seats with IDs +1 and -1 from yours will be in your list"*, meaning our spare seat should appear in *isolation* in that list. Finding it was pretty easy and straightforward, then.

### Time and memory complexity

For the analysis below, the following variables have these meanings:

- `n` means the size of the input, aka tickets
- `m` means the total amount of seats available

**Time** complexity is simple: for each line of input, we process the data to get the row and column, and compute the maximum seat ID value. Here, the time complexity is simply **O(n)**, as the calculations are quite simple. For part 2, and because we use the results from part 1, some work is already completed; what it does essentially is iterate the list of empty seats until it finds the vacant spot. That has complexity **O(m-n)** ~= **O(n)** *(because we iterate a list of non taken seats, aka seats without a ticket associated with)*

**Memory** complexity, although not out of the ordinary, has an interesting situation: it uses **O(n+m)** memory in the beggining, as it needs to contain the whole input data and a map of all the seats. During the algorithm's execution, it decreases usage by `n` values, as the map gets progressively smaller. So, although it starts big, it does descend as the algorithm goes on. Nevertheless, we consider the worst case. Therefore **O(n+m)** *(and yes, for both parts, as they are intertwined)*
