## Fancy table input/output with Pandas

Custom functions to save pandas dataframes as nicely formatted tables into a text file, and vice versa.

### Usage

```python
import pandas
from pandas_fancy_table_io import to_fancy_table, from_fancy_table

# Adds the custom functions to the pandas module.
pandas.DataFrame.to_fancy_table = to_fancy_table
pandas.from_fancy_table = from_fancy_table

# Creates a dataframe.
details = {
    'Name' : ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
    'Age' : [23, 21, 22, 21],
    'University' : ['BHU', 'JNU', 'DU', 'BHU']
}
df1 = pandas.DataFrame(details)

# Writes the dataframe into a text file.
df1.to_fancy_table('table_test.txt')

# Reads the dataframe from the texte file.
df2 = pandas.from_fancy_table('table_test.txt')
```

See `pandas_fancy_table_io.py` and `example.py` for further details.
