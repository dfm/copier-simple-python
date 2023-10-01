# How to release your (Python) code in October 2023

I'm giving a tutorial titled something like "How to Release Your Python Code" at
the [.Astronomy](https://www.dotastronomy.com/twelve) conference in October
2023, and I've been trying to collect my thoughts about best practices for
packaging, releasing, and publishing scientific Python libraries. This is
certainly a moving target, but I'm trying to capture my current knowledge here,
with the caveat that it'll probably be out of date by the time of the tutorial.

One of the biggest challenges in Python packaging is the huge number of possible
choices that can be made at every step of the process. In particular, for every
task there are typically several excellent tools that could be used. In this
tutorial, I'll try to identify these choices and explain my own preferences, but
this is not meant to be a one-size-fits-all solution.

## This repository

This repository contains a [`copier`](https://copier.readthedocs.io) template,
meant to be a starting point for generating the skeleton for a new Python
package. To use it, you'll need to [install `copier` as described in the
documentation](https://copier.readthedocs.io), and then run:

```bash
copier copy gh:dfm/copier-simple-python my-new-package
```

## Why release your code?

## What do we mean by "code"? Or "release"?

## How should you release your code?
