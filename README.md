[![Tests and type-checks](https://github.com/public-law/new-dale-chall-readability/actions/workflows/python-app.yml/badge.svg)](https://github.com/public-law/new-dale-chall-readability/actions/workflows/python-app.yml)


# The new Dale-Chall readability formula

In a nutshell:

```python
In [1]: from new_dale_chall_readability import cloze_score, reading_level

In [2]: text = (
   ...:     'Latin for "friend of the court." It is advice formally offered '
   ...:     'to the court in a brief filed by an entity interested in, but not '
   ...:     'a party to, the case.'
   ...:     )

In [3]: cloze_score(text)
Out[3]: 42.46652

In [4]: reading_level(text)
Out[4]: '5-6'
```


An implementation that follows the specification as closely as
possible. Created by referring to a paper copy of
their most recent publication (Chall & Dale, 1995).


## References

Chall, J., & Dale, E. (1995). _Readability revisited: The new Dale-Chall readability formula_.
Brookline Books.
