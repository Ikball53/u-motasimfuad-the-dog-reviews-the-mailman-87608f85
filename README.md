# The Dog Reviews the Mailman

A make.fun one-liner entry: one funny one-line review that a dog gives the
mailman, under 200 characters.

## The line

> He comes six days a week, knows my name, and has never once scratched behind my ear. One star.

The joke is the dog's grievance: the mailman is the one stranger who shows
up every single day and knows the dog by name, yet has never once done the
one thing every dog wants — an ear scratch. The rating lands last, so the
line reads as an actual review.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/dog-review python3 main.py
cat /tmp/dog-review/entry.txt
```

`main.py` (Python 3.13, stdlib only) writes the line — exactly, with no
trailing newline — to `<output dir>/entry.txt`. If `MAKEFUN_OUTPUT_DIR` is
not set, it defaults to `/output`.
