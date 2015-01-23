# tower-of-hanoi
A 'Tower of Hanoi' algorithm implemented in Python

## How to

Just run the script, and use as commandline argument the number of disks you have.

So for exmple if you play Tower of Hanoi with 4 disks, you write

```
python tower_of_hanoid.py 4
```

I will print the solution in the in format (example using 3 disks)

```
1 -> 3
1 -> 2
3 -> 2
1 -> 3
2 -> 1
2 -> 3
1 -> 3
```

1, 2, and 3 is indicating the pegs you use to store the disks; 1 being the peg to the left, 2 the peg in the middle, and 3 the peg to the right. This script assumes you play *Tower of Hanoi* using 3 pegs.

## Just for the fun of it

Read about recursion, and stumbled over a solution to the *Tower of hanoi* using recursion. It was originally written in Java, so I just quickly rewrote it in Python - just so I could send it to a friend.

Credits to:

http://www.mathcs.emory.edu/~cheung/Courses/170/Syllabus/13/hanoi.html
