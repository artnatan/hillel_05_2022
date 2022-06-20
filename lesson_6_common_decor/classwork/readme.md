## <span style="color:green">Materials</span>

- [Python built-in functions](https://docs.python.org/3/library/functions.html)
- [Python Magic/Dunder methods](https://www.tutorialsteacher.com/python/magic-methods-in-python)


## Useful decorators

1. wraps
2. property
3. classmethod
4. staticmethod

5. lru_cache

```python
from functools import lru_cache
import time

def fib_without_cache(n):
   if n < 2:
       return n
   return fib_without_cache(n - 1) + fib_without_cache(n - 2)

begin = time.time()
fib_without_cache(30)
end = time.time()

@lru_cache(maxsize=None)
def fib_with_cache(n):
   if n < 2:
       return n
   return fib_with_cache(n - 1) + fib_with_cache(n - 2)

begin = time.time()
fib_without_cache(30)
end = time.time()
```