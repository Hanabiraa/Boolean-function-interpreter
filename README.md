 # Python - Boolean Function Interpreter
 
***

An interpreter written from scratch in python that can calculate basic boolean functions over the entire truth table or specific values

### Dependencies


|package|version|
|----|-------|
|python|>= 3.9.6|
|pandas|>= 1.3.2|

## How to use

```shell
python3 main.py
```

In the program itself, you will be prompted to the input line, where you must enter the expression, for example:

**(By default, the entire truth table will be saved to the ./output_data/table.csv file and is not shown, flag -v or -s change this behavior (see below))**

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

|flag|extend flag|meaning|
|----|-----------|-------|
|-h|--help|for reference|
|-v|--visual| print pd.DataFrame with answers to sys.stdout.write and saves the file to the standard path (default: False)|
|-s|--simple|it just outputs the answer without storing it anywhere (default: False)|
|-e|--expr|You can enter an expression into this flag if you don't want to do it through the main.py|
|-d|--debug|outputs each change to the token array after the functions. Before the Abstract Syntax Tree (default=False)|

## Syntax

#### About priority
Operations are divided into 5 parts by priority, the author advises, for 100% reliability of the correctness of the result, to separate operations in one category _(for example, either `and` or `nand` in the same category and evaluating them without parentheses is **undefined behavior**)_ with parentheses.

Priority of categories: 1 - first, 5 - last
1. `Bool number`, `negation`, `parentheses`
2. `and`, `nand`
3. `or`, `xor`, `nor`
4. `le`, `ge`
5. `eqv`

#### Which boolean operations supports?

|operation|equivalent for expression|
|----|-------|
|[¬ / Inverter](https://en.wikipedia.org/wiki/Inverter_(logic_gate))|`negation`|
|[∧ / & / logical conjunction](https://en.wikipedia.org/wiki/AND_gate)|`and`|
|[↑ / NAND / Sheffer stroke](https://en.wikipedia.org/wiki/NAND_gate)|`nand`|
|[∨ / logical disjunction](https://en.wikipedia.org/wiki/OR_gate)|`or`|
|[⊕ / exclusive OR / EOR / NE](https://en.wikipedia.org/wiki/XOR_gate)|`xor`|
|[↓ / NOR / Peirce's arrow](https://en.wikipedia.org/wiki/Logical_NOR)|`nor`|
|[→ / implication](https://en.wikipedia.org/wiki/Material_conditional)|`le`|
|[← / reverse implication](https://en.wikipedia.org/wiki/Converse_(logic))|`ge`|
|[<->/ = / ~/ EQ / EQV](https://en.wikipedia.org/wiki/Logical_equality)|`eqv`|


### Introduction

***

This interpreter was created during my bachelor's degree in software engineering.
In this example, I studied one of the [top-down parsing algorithms](https://ru.wikipedia.org/wiki/%D0%9D%D0%B8%D1%81%D1%85%D0%BE%D0%B4%D1%8F%D1%89%D0%B8%D0%B9_%D1%81%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7).
In this case, I used [LL(1) parser](https://ru.wikipedia.org/wiki/LL-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80).

> Why is `LL(1)`?

Because only 1 lexeme is required to determine the parsing path (lexeme of one of the groups)

## How it works

