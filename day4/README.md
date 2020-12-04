# Day 4: Passport Processing

## Problem statement (part 1)

Given a list of information passports, identify which ones have all the required fields to be valid, that is, which ones have the info about:

- `byr` *(Birth Year)*
- `iyr` *(Issue Year)*
- `eyr` *(Expiration Year)*
- `hgt` *(Height)*
- `hcl` *(Hair Color)*
- `ecl` *(Eye Color)*
- `pid` *(Passport ID)*

`cid` *(Country ID)*, however, for the purposes of this problem, is considered optional

### Input

The given input contains this type of data:

```
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
```

Information is spread unevenly on either the same or a new line. A blank line indicates the end of info for that passport, and the start of a different one. Note that the information that comes after the key is not validated; all we need to check are the keys present

### Output

Looking at the example above, we see that the first and third passports are valid: the first one contains every key, while the third one lacks the `cid` key, which is optional. The other two passports are invalid: the second one is missing the `hgt` field, and the forth one the `cid` and `byr`; despite `cid` being an optional key, `byr` is mandatory. Therefore, the final output is `2`.

## Problem statement (part 2)

The problem is the same structure, but we now just need to add more validation on top; specifically, the information has constraints now:

- `byr` *(Birth Year)* - four digits; at least `1920` and at most `2002`.
- `iyr` *(Issue Year)* - four digits; at least `2010` and at most `2020`.
- `eyr` *(Expiration Year)* - four digits; at least `2020` and at most `2030`.
- `hgt` *(Height)* - a number followed by either `cm` or `in`:
	- If `cm`, the number must be at least `150` and at most `193`.
	- If `in`, the number must be at least `59` and at most `76`.
- `hcl` *(Hair Color)* - a `#` followed by exactly six characters `0`-`9` or `a`-`f`.
- `ecl` *(Eye Color)* - exactly one of: `amb` `blu` `brn` `gry` `grn` `hzl` `oth`.
- `pid` *(Passport ID)* - a nine-digit number, including leading zeroes.
- `cid` *(Country ID)* - ignored, missing or not.

### Output

With the same input, we now have to validate the values given. Here's some examples of valid and invalid values:

```
byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789
```

Invalid passports:
```
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
```

Valid passports:
```
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
```

## Algorithm analysis

Before we can even start the algorithm, I took the approach of **pre-formatting** the data; since the info for one passport can be scattered in **multiple** and *single* lines, I implemented a method to collect that information into a single `string`, with `key:val` pairs separated by ` `s. Then I save it in a list, `passport`, where each entry corresponds to info about a given **passport**. Now, we're ready.

For the first part, all we need to check is if the necessary **keys** are present. I've coded a tuple of keys and created an associative map of keys and booleans. Now, all I need to do is fetch a key, mark it as `True` in the map, and when I'm done, check if any entry in the map is still `False`; if it **is**, then it's missing a necessary key, and therefore is **invalid**. Rinse and repeat.

For the second part, we now need to **also** validate the value associated with the key, with some very specific *conditions*; for that, I've used a helper method to return a boolean to see whether that value, for that key, satisfies the **restrictions** imposed above. Code-wise, it was mostly adding new stuff than replacing, so I'm quite happy with this approach. I really did use and abuse array slices and string splits for this approach though, so there are a lot of assumptions of some *preformatted* data *(such as for height, it assumes the last two chars represent units.)*. But, *overall*, I'm pretty happy with my implementation.

### Time and memory complexity

For the analysis below, the following variables have these meanings:

- `n` means the size of the input
- `m` means the amount of passports

**Time complexity** is simple: we need to pre-format each line of input, and then test each passport for the conditions; those tests run in more or less **O(1)** time, so it doesn't add to the complexity. The final complexity, for both parts, is **O(n+m)** = **O(n)** *(`n` is always bigger than `m`)*

**Memory complexity** also hasn'y anything to point out: we need to store the input, and processed data. Therefore, for both parts, **O(n+m)** = **O(n)**.