# frdate
[![](https://img.shields.io/badge/pypi-v0.6-blue)](https://pypi.org/project/frdate/)

Date conversion (from numbers to letters or from letters to date object), in french.

**Installation :**
```bash
pip install frdate
```

**Usage :**

The main method of this package is `conv()`

It takes one mandatory argument (the input to convert) and two optional boolean args :
- to_date (default = False) : set to True if you need to convert the input into a `datetime.date()` object
- litteral (default = False) : set to True if you need to convert the input into a string object only using letters

**Supported formats :**

The input can be :
- a datetime.date object
- a datetime.datetime object
- a string representing a date, in any format,
- a list of the above elements

**Examples:**

```python
from frdate import conv

conv('14071789')
#'14 juillet 1789'

conv('17890714',to_date=True)
#datetime.date(1789, 7, 14)

conv('1789-07-14',litteral=True)
#'quatorze juillet mille sept cent quatre-vingt-neuf'

conv(['01/01/2000','2000-01-01',date(2000,1,1)])
#['1er janvier 2000','1er janvier 2000','1er janvier 2000']
```
