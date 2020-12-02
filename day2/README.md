# Day 2: Password Philosophy

## Problem statement (part 1)

Given a list of needed character occurrences and a password per line, we need to check if the password follows the condition specified before.

### Input

We receive a text file with this info on each line:

```
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```

The first part *(before the `:`)* represents the condition: what is the *minimum* and **maximum** number of ocurrences that character must appear in the password after. The second part is the password for that condition.

### Output

With the following example, we find that `abcde` and `ccccccccc` satisfy their conditions: `abcde` contains 1 `a`, which is valid, since there must be between 1 and 3; and `ccccccccc` contains 9 `c`'s, which also satisfies it's condition *(9 in **[2, 9]**)*. However, `cdefg` contains 0 `b`'s, which fails the condition, as there must be between 1 and 3. The final output is the number of valid passwords; in this case, `2`.

## Problem statement (part 2)

The problem is essentially the same; only the condition's *meaning* has changed; it now represents the character indexes to find the password on, and there must be only one occurence.

### Input

We receive a text file with this info on each line:

```
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```

The first part *(before the `:`)* represents the condition: what are the two positions in the string *(they start on 1)* where that character must appear only once in the password after. The second part is the password for that condition.

### Output

With the following example, we find that only `abcde` satisfies it's condition now: `1-3 a` means the password must contain a single `a` only on position 1 *(index 0)* or position 3 *(index 2)*. Looking at the other passwords, we see they both fail their conditions: `cdefg` doesn't have a `b` anyways, and `ccccccccc` has a `c` in both requested positions, when we can only have one occurence. Therefore, for this part, the expected output is `1`.

It's important to note that we're being asked about character occurences **only** in those said positions, and ignoring any content outside of it. This means that, for example, `2-9 c: ccccccccd` is a valid password; even with a total of 8 `c`'s, positions 2 and 9 contain `c` and `d`; there's only one occurence of character `c` on these positions, and therefore, the password is **valid**.
1

## Algorithm analysis

The algorithm I made is pretty simple; I process the data *line by line*, format the data to be "usable", and then all is implemented in a single if condition. For the first part, there's really not much to explain. For the second one, I took advantage of the XOR operation to implement it "cleanly".

### Time and memory complexity

For the analysis below, the following variables have these meanings:

- `n` means the size of the input

**Time** complexity is normal; both parts need to process each line, but apart from that there are no extra operations that inccur a cost. Therefore, the complexity is **O(n)**.

**Memory** complexity is the same; there's no need to allocate any more significant memory other that the input. Therefore, **O(n)**.