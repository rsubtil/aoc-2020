# Day 3: Toboggan Trajectory

## Problem statement (part 1)

Given a map of the area, and the pattern on how we descend that map, find the amount of trees that are in the way.

### Input

The input is of this kind:

```
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
```

Where a `.` represents an open space, and `#` a tree. Note that this pattern repeats endlessly to the right, like so:

```
..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
```

Also, we are told from the beginning that our toboggan descends into a pattern of **3 right, 1 down**; meaning, for each space we go down, we go right three spaces.

### Output

The output must be the amount of trees we're gonna collide with on our path. Taking the example above, and starting from the leftmost corner, we trace our path:
```
..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
```

`O` represents an open space, and `X` a collision with a tree.

We come to the conclusion that we collide seven times with our pattern. Therefore, the final answer is `7`.

## Problem statement (part 2)

The problem is *exactly* the same, only now he have to test more, different patterns:

- Right 1, down 1.
- Right 3, down 1. (The same from the previous part)
- Right 5, down 1.
- Right 7, down 1.
- Right 1, down 2.

## Algorithm analysis

The algorithm traverses it's input map by the **Y** values; for each **Y** value we check *(starting from 0 to the last one; we just skip the first line)*, compute the corresponding **X** value. Then, it's just a matter of checking whether that coordinate in the input *(which essentially acts as a 2D grid)* has a tree.

The way this is implemented, adding new patterns is very straightforward; just add a new tuple to the `patterns` array. This was immensely helpful for part 2, as it was very simple to do; just iterate over all patterns and run the same code from before.

### Time and memory complexity

For the analysis below, the following variables have these meanings:

- `n` means the size of the input
- `m` means the amount of patterns to test

**Time** complexity is normal; for each pattern we have, we descend our input list depending on the Y requested: it could be **n** iterations, **n/2**, **n/3**, *etc...*, all of which belong to the **O(n)** class. Therefore, our final time complexity is **O(n\*m)**. *(for part one, since m = 1, then it's just **O(n)**)*

**Memory** complexity is straightforward too; we're not allocating any additional memory to process the algorithm. It is therefore, for both parts, **O(n+m)** = **O(n)**.