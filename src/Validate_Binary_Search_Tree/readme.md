# types
## tree
### binary search tree

# algorithms
## tree
### dfs

# caveats
## languages
### python
#### checking the existence of an integer
Avoid using:
```python
from typing import Optional

val: Optional[int] = 0
if not val:
    print("val doesn't exist")
```
Instead, prefer using:
```python
from typing import Optional

val: Optional[int] = 0
if val is not None:
    print("val doesn't exist")
```