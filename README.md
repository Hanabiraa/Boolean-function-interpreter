 # Python - Boolean Function Interpreter

An interpreter written from scratch in python that can calculate basic boolean functions over the entire truth table or specific values


## Syntax

Operations are divided into 5 parts by priority, the author advises, for 100% reliability of the correctness of the result, to separate operations in one category (for example, either `and` or `nand` in the same category and are calculated from left to right) with parentheses

Priority of categories: 1 - first, 5 - last
1. `Bool number`, `negation`, `parentheses`
2. `and`, `nand`
3. `or`, `xor`, `nor`
4. `le`, `ge`
5. `eqv`

This interpreter supports operations such as:

|operation|equivalent for expression|
|----|-------|
|[Inverter / ¬](https://en.wikipedia.org/wiki/Inverter_(logic_gate))|negation|
|[logical conjunction / & / ∧](https://en.wikipedia.org/wiki/AND_gate)|and|
|[NAND / ↑ / Sheffer stroke](https://en.wikipedia.org/wiki/NAND_gate)|nand|
|[logical disjunction / ∨](https://en.wikipedia.org/wiki/OR_gate)|or|
|[exclusive OR / EOR / EXOR](https://en.wikipedia.org/wiki/XOR_gate)|xor|
|[NOR / ↓ / Peirce's arrow](https://en.wikipedia.org/wiki/Logical_NOR)|nor|
|le|le|
||ge|
|eqv|eqv|

## Dependencies

|package|version|
|----|-------|
|python|>= 3.9.6|
|pandas|>= 1.3.2|

***

chapters

***

## How to use it

```shell
python3 main.py
```

In the program itself, you will be prompted to the input line, where you must enter the expression, for example:

**(By default, the entire truth table will be saved to the ./output_data/table.csv file and is not shown, flag -v change this behavior)**

```python
prompt> x1 and x2
truth table saved in ./output_data/table.csv
```

in the ./output_data/table.csv

```csv
   x1  x2  expr: x1 and x2
0   0   0                0
1   0   1                0
2   1   0                0
3   1   1                1
```

## Flags

|flag|meaning|
|----|-------|
|-h|for reference|
|-v|print pd.DataFrame with answers to sys.stdout.write (default=False)|
|-d|outputs each change to the token array after the functions. Before the Abstract Syntax Tree (default=False)|

## Introduction


