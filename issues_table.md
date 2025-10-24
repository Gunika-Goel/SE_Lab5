# Static Analysis Issues - inventory_system.py

| Issue Type               | Line(s)       | Description                                        | Fix Approach |
|---------------------------|--------------|---------------------------------------------------|--------------|
| Mutable default argument  | 9            | `logs=[]` shared across calls, can accumulate across function calls | Changed default to `None` and initialized inside function (`if logs is None: logs = []`) |
| Bare except               | 14-17        | Catches all exceptions silently, hides bugs      | Replaced with `except KeyError` and added a print message |
| Dangerous `eval()`        | 63           | Using `eval()` is unsafe, can execute arbitrary code | Removed `eval()` and replaced with safe print statement |
| Invalid type input        | 55-57        | `addItem(123, "ten")` can crash due to type mismatch | Added type checking (`item` must be str, `qty` must be int) and raised `ValueError` |
| File handling             | 25-31        | `open()` without `with` may leak files           | Used `with open(...) as f:` syntax and added `FileNotFoundError` handling |
