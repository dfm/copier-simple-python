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

- Want to reuse your own code in other places
  - So that you can find your code even when not on your usual machine
  - Also in cloud/cluster/remote environments
  - Encourage good coding practices
  - Reduce need for copy pasting code snippets between projects
- Want to let other people use and learn from your code
  - To save everyone from reimplementing the wheel
- To get feedback on your code
- To get help improving code from others
- Reproducibility & transparency
- Credit?
  - Some work towards code citation and tracking
- Some definitions of "release" might also save on your support costs
- Because you have to - aligned with funding agency priorities
- Can help reduce fear of releasing "bad code"

_Why shouldn't you release your code_:

- Copyright issues - organization IP policy
- Risk of getting scooped
- Can be a lot of work - support requests, feature requests, bug reports, ...
- Shame and fear of judgement
- Insufficiently tested code cause issues if others use _wrong_ code
- Insufficient documentation

## What do we mean by "code"? Or "release"?

_Code_:

- A package: not just loose code in a directory, something that can be installed
- Modular and general
- Script to generate figure for paper
- Set of scripts for personal data reduction
- Documentation is part of the code
- Notebook walking through what you did
- Anything that you can install that then _does something_
- Queries to online(e.g.) archives
- Directory structure of a project
- A paper
- ...

_Release_:

- On GitHub
- Publishing in a refereed journal
- Snapshot of the code at a specific point in time
- Sharing with colleagues
- PyPI or other package management index
- Published on a web page
- ...

- Access / licensing
- Installation
- Documentation
- Testing

## How should you release your code?
