## <span style="color:green">Homework</span>

- Reailze reverse string decorator
```python
# MODIFY THIS DECORATOR
def reverse_string(func):
    """If output is a string, reverse it. Otherwise, return None."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# TARGET FUNCTIONS
@reverse_string
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"

@reverse_string
def get_university_founding_year() -> int:
    return 1957

# TEST OUPUT
print(
    get_university_name(),
    get_university_founding_year(),
    sep="\n"
)
```

- Replace dict value decorator
```python
# MODIFY THIS DECORATOR
def mask_data(target_key: str, replace_with: str = "*"):
    """Replace the value of a dictionary with a 'masked' version."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {
        "name": name,
        "age": age
    }

# TEST OUPUT
print(
    get_user(name="Alice", age=30),
    get_user(name="Bob", age=25),
    sep="\n"
)
```
