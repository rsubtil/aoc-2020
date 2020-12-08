# Day 8: Handheld Halting

## Problem statement (part 1)

Given a list of "assembly" instructions, find out when the code is gonna loop itself, and at that time, return the value of the accumulator

### Input

The input looks liek this:

```
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
```

Each line is an "assembly" instruction. There are only three simple ones: `acc` increments *(or decrements)* the accumulator value, `jmp` jumps to a relative address from itself, and `nop` does nothing.

### Output

At the beginning, our PC *(program counter, that is, the line we're executing)* is 0, and the accumulator's value is 0 as well. The execution is delineated below:

- PC:0 -> `nop +0` -> PC:1, Acc:0
- PC:1 -> `acc +1` -> PC:2, Acc:1
- PC:2 -> `jmp +4` -> PC:6, Acc:1
- PC:6 -> `acc +1` -> PC:7, Acc:2
- PC:7 -> `jmp -4` -> PC:3, Acc:2
- PC:3 -> `acc +3` -> PC:4, Acc:5
- PC:4 -> `jmp -3` -> PC:1, Acc:5
- PC:1 -> `acc +1` -> HALT; this line has been executed already.

As we can see, with the input above, we have an infinite loop. For this part, we want the program to stop right before it begins it's second loop, and print it's accumulator value. In this example, the final result is `5`.

## Problem statement (part 2)

For part 2, we now have to actually fix the code to run past an infinite loop. We know there's a single instruction somewhere than, when changed, will make the code work. This instruction is either a `nop` ou a `jmp`, which needs to be swapped to it's counterpart.

### Output

For the same example, we try swapping `nop`s and `jmp`s, until the swap in line 7 *(from `jmp -4` to `nop -4`)* will make the program execute until the very end. When we get there, the final answer is the same: the amoun in the accumulator variable. In this case, `8`.

## Algorithm analysis

The algorithm is basically an "emulator": if fetches instructions and runs them. For the first part, I save a list of already visited addresses; if the code finds that we're visiting an already visited one, it halts. Then, we just grab the value stores in `acc` as our answer.

For part two, we have to modify instructions. We go line by line, modify it, and run the program. If it didn't success, we restore the original value and move on. If, however, we do success *(when PC is bigger than the input_list)*, we have reached the end; grab the `acc` as before, and return it as answer.

### Time and memory complexity

### Time and memory complexity

For the analysis below, the following variables have these meanings:

- `n` means the size of the input

**Time** complexity is simple: we run possibly `n` lines of code until we find a loop. For part one, that's **O(n)**. For part 2 though, since we possibly modify the code, we have to run that new code to check if it's the correct one. The code runs `n` lines, and we modify possible `n` lines. So, for part two, the complexity is **O(n²)**

**Memory** complexity is also trivial: we store the input data, and a temporary list of PC addresses, which can grow up to `n` values. Therefore, and for both parts, it's **O(n)**.