Profiling 5 ways to call functions with an integer index.

Each round, a large number of random indexes are generated, calling all the
functions (including the default). The functions are shuffled each round and
called once for each of the indexes.

Saves profiling data to `stats.prof`. Use `snakeviz` to view.

Each function is run 16,000,000 times. This took about 45s total on my computer.

| function | description | num calls | total time | per call |
---|---|---|---|---
dict_var| assign dict within the function |16000000 | 6.814 | 4.259e-07
list_prop| assign dict once, as a property of the function (with bounds check) |16000000 | 6.471 | 4.045e-07
dict_prop| assign list once, as a property of the function |16000000 | 6.032 | 3.770e-07
if_else| if-elif-else ladder |16000000 | 3.999 | 2.500e-07
match_stmt| use match statement like switch |16000000 | 3.926 | 2.453e-07