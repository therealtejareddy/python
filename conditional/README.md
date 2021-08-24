# Conditional Statements

Takes a decision & execute a set of statements based on that decision
> A python statement is an instruction which can be executed by interpreter
### Types of conditional statements
* conditional (`if`)
* Alternative (`if - else`)
* Chained Conditional (`if - elif - else`)

### conditional ( `if` )
The statements inside the `if` block executes when the condition is `True`

if the condition is `False` then the interpreter skips the `if` block code

```python
if condition:
    # True statement block

# example
is_rainy = True
if(is_rainy):
    print("Take Umbrella")
```

### Alternative ( if - else )
if the condition in `if` block is False then the code in `else` is executed
```python
if condition:
    # True Block Code
else:
    # False Block Code
```

> The walrus operator `:=` is used as an assignment expression

### Chained Conditional ( `if-elif-else` )
if the condition in `if` block is `False` then `elif` condition will be check if it is `True`, The code inside `elif` will be executed. if `elif` condtion is also `False` the code inside `else` block will be executed
```python
if condition1:
    # Block Code
elif condition1:
    # Block Code
else:
    # False Block Code
```
### Nested Conditional statements
writing conditional statements inside the condition
```python
if condition1:
    if condition2:
        # ststements
    else:
        # statements
else:
    if condition3:
        # ststements
    else:
        # statements
```