# frdate
[![](https://img.shields.io/badge/pypi-v0.1-blue)](https://pypi.org/project/frdate/)

This python functions discovers a date object underneath the input, and returns it in french.

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

The input can be a datetime.date or datetime.datetime object, or any string written in the following formats:
- YYYYMMDD
- DDMMYYYY
- YYYY-MM-DD
- YYYY/MM/DD
- YYYY MM DD
- DD MM YYYY
- DD/MM/YYYY
- DD-MM-YYYY
- ...
