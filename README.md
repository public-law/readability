[![Tests and type-checks](https://github.com/public-law/new-dale-chall-readability/actions/workflows/python-app.yml/badge.svg)](https://github.com/public-law/new-dale-chall-readability/actions/workflows/python-app.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/ef1198fa2d9246aa3c7d/maintainability)](https://codeclimate.com/github/public-law/new-dale-chall-readability/maintainability)



# The new Dale-Chall readability formula

Installation:

```bash
$ pip install new-dale-chall-readability
```

Let's try it out:
```bash
$ ipython
```

```python
In [1]: from new_dale_chall_readability import cloze_score, reading_level

In [2]: text = (
   ...:     'Latin for "friend of the court." It is advice formally offered '
   ...:     'to the court in a brief filed by an entity interested in, but not '
   ...:     'a party to, the case.'
   ...:     )

In [3]: reading_level(text)
Out[3]: '7-8'

In [4]: cloze_score(text)
Out[4]: 36.91
```


## Why yet another readability library?

It's 2022. There are probably a half-dozen Dale-Chall implementations in Python on PyPI.
Why create another one?

* Dale-Chall.
* They all seem to have issues.
* Test-driven development.
* Use examples from the book as test cases.
* Modern Python.
* Maintainable coding practices.
* Very easy API to use in any app or library.
* Purchase a copy of Chall & Dale's _Readability Revisited_ and use it to implement the library from scratch.


## References

Chall, J., & Dale, E. (1995). _Readability revisited: The new Dale-Chall readability formula_.
Brookline Books.
