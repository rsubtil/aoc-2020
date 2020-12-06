# Day 6: Custom Customs

## Problem statement (part 1)

Given a list of answers to specific questions, get the sum on the amount of questions people have answered, without repetitions.

### Input

The input is of the type:

```
abc

a
b
c

ab
ac

a
a
a
a

b
```

The input represents groups of people, and those people's answers to specific questions. Groups are separated by blank, empty newlines, and people's answers by newlines inside a group.

### Output

In the input above, we have a total of 5 groups:

- `abc` is group #1, and there's only one person on that group, that answered "yes" to `3` questions: `a`, `b` and `c`.
- `a\nb\nc` is group #2, and this one has three persons; their answers combined are `yes` to `3` questions: `abc`.
- `ab\nac` is group #3, with two people; the answer combined are `3` as well; notice we have a duplicated answer to `a`, but we're not interested in that.
- `a\na\na\na` is group #4, consisting of four people; this oen only answered `yes` to `1` question though: `a`.
- `b` is group #5 and the final one; it's only one person, and one answer: `b`.

In the end, we have a total of `3 + 3 + 3 + 1 + 1` unique answers per group. This sums up to `11`, which is the final answer.

## Problem statement (part 2)

The problem is the same, but the logic changes; insted of finding questions that anyone answered yes, we need to find question that **everyone** answered yes.

### Output

We have the same input as above. The output with this new logic is the following:

- `abc` represents one person, and they answered to `3` questions; so, everyone in this group answered `yes` to the `3` questions.
- `a\nb\nc` are the answers of three people; however, they all answered different things, so the total is `0`.
- `ab\nac` are two persons; we see that both of then said `yes` to question `a`, therefore everyone voted `yes` for `1` question.
- `a\na\na\na` are four people, and all answered only one; so, `1`
- `b` is one person, so `1`.

In the end, we also sum up the values like the first part; `3 + 0 + 1 + 1 + 1`. So, our final answer is `6`.

## Algorithm analysis

Originally, I had implemented the algorithm separately for *both* parts, but they reuse so much code, that I decided to **merge** the two. This shouldn't affect the final **time** and **memory** complexity analysis, as they belong to the same class.

The input is formatted in a similar way to **day 4**, *as in*, the input data is *scattered* over newlines and blank newlines. I then reused the pre-formatting code here to have the input *formatted* in a easy way to use. Then, the algorithm is straighforward: for *each* group, and for *each* person, collect **all** the answers that person has given. We store this in a dictionary `answer_map`, saving the **amount** of answers that have appeared in the group. Then, we can *solve* both parts at the **same** time: *for part 1*, simply **find** the amount of answers that exists; *for part 2*, filter to **only** add the answers that everyone answered.

### Time and memory complexity

For the analysis below, the following variables have these meanings:

- `n` means the size of the input

**Time** complexity is nothing extraordinary: we iterate over every line of input and process it in constant time. Therefore, **O(n)**.

**Memory** complexity is the same: we don't need to store significantly more than the input itself: **O(n)**.