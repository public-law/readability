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


## Why yet another Dale-Chall readability library?

It's 2022. There are probably a half-dozen implementations on PyPI.
So why create another one?

* They all seem to have issues.
  * For example, from my reading of the book, I realized that **reading level** is a set of
    ten "buckets" and and each one has a name. 
    E.g., there's "3" and "7-8". 
    The existing libraries I found treat these as floating point numbers. 
    But now I believe that an enumeration — or specifically,
    a [Literal](https://docs.python.org/3/library/typing.html#typing.Literal) — captures the formula better:
    `Literal["1", "2", "3", "4", "5-6", "7-8", "9-10", "11-12", "13-15", "16+"]`
* Use Test-Driven Development to squash bugs and prevent regressions.
* Turn examples from the book into test cases.
* Write with modern Python. I'm no expert, so I'm learning as I go along. E.g., 
  * It passes Pyright strict-mode type-checking.
  * It uses recent type enhancements like `Literal`.
* It should have a very easy API to use in any app or library.
  * No need to instantiate an object and learn its API.
  * Just import the needed function and call it.

And so I decided to re-think the library from the ground-up. I ordered a copy of Chall & Dale's _Readability Revisited_ and used it to write the library from scratch. It's been a great
experience: the book is well written with lots of details of the scientific validation
done by the authors. The bonus surprise was the sample texts
where are perfect as Pytest test cases.


## References

Chall, J., & Dale, E. (1995). _Readability revisited: The new Dale-Chall readability formula_.
Brookline Books.
