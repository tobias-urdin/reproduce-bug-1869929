# Reproduce bug 1869929

This is a reproduce for bug 1869929

Link: https://bugs.launchpad.net/oslo.config/+bug/1869929

# Usage

Clone the repo and run `tox`.

```
$ git clone https://github.com/tobias-urdin/reproduce-bug-1869929
$ tox
..snip output..
RuntimeError: maximum recursion depth exceeded
```
