# String cleaner
Module for clean string from special chars and replace it by html-entity.

#### In current version (0.3.1):
* Replace special chars from string by html-entity based on the json entity map
    * symbol - "
    * symbol - '
    * symbol - >
    * symbol - <
    * another quote symbols
* Support possibility work with context manager. `oprional`
* Additional users rule for replace. `oprional`

#### In next versions:
* 0.4 — validation scheme for users input values for additional replace rules
* 0.5 —
* 0.6 —
* 0.7 —
* 0.8 —
* 0.9 —
* 1.0 (`release`) —

#### How to use:
For first install module in your virtual environment:
```commandline
pip install string-cleaner
```
After this you can import this module and use it simple:
```python
from string_cleaner import cleaner
clean_string = cleaner.TakeString('<script>alert(123)</script>').make_clean_string()
```

Or use it with additional parameters:
```python
from string_cleaner import cleaner
clean_string = cleaner.TakeString(string='<script>alert(123)</script>', new_rule={"(": "|", ")": "|"}).make_clean_string()
```

Also, you can use it with context manager:
```python
from string_cleaner import cleaner

with cleaner.TakeString(string='<script>alert(123)</script>', new_rule={"(": "|", ")": "|"}) as clean_string:
    print(clean_string)
```
