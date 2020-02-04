### Software developer AI & ML test

#### Project structure

```
juan_argaez_test
│   lines.py
│   version.py
│   search.py
│   requirements.txt
└───tests
    │   lines_test.py
    │   version_test.py
    │   search_test.py
```

#### Design and missing features

##### Question A
The solution is a function which receives numeric `x1`, `x2`, `x3` and `x4` and outputs a boolean, depending if the lines overlap.

The function is flexible enough in receiving the input points in different order. This means that passing `x1 = 1` and `x2 = 3` is the same as passing `x1 = 3` and `x2 = 1`.

Only lines are expected, cases when `x1 = x2` or `x3 = x4` will return `False`.

##### Question B
The solution is divided into two functions:
1. One function for receiving both version values to compare. It returns `-1`, `0` or `1` if the first version is lower, equal or greater than the second, respectively.
1. Another function for splitting the version parts, _i.e._ alnum sequences separated by any non-alnum character.
For example version `1a.f4-1` is composed of three parts `['1a', 'f4', 1]`.

##### Question C
The solutions sends a request to Google by using `urllib` library. The response is then processed with Beautiful Soup package.

A REST API server was not implemented, though it can be easily built with Flask, Django or other framework.
