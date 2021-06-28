# frdate
[![](https://img.shields.io/badge/pypi-v0.3-blue)](https://pypi.org/project/frdate/)

Finds a date object in a string input, and returns it in french.

**Installation :**
```python
pip install frdate
```

**Examples:**

```python
>>> from frdate import conv

>>> conv('14071789')
"14 juillet 1789"

>>> conv('17890714',to_date=True)
"datetime.date(1789, 7, 14)"

>>> conv('1789-07-14',litteral=True)
"quatorze juillet mille sept cent quatre-vingt-neuf"
```

**Supported formats :**

The input can be a datetime.date or datetime.datetime object, or any string representing a date, or a list or dict of strings
