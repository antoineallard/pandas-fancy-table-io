# -*- coding: utf-8 -*-
# @author: Antoine Allard <antoineallard.info>
#
# Script testing the functionalities of the pandas-fancy-table-io methods.

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


print(df1)
print(df2)
assert all(df1 == df2)

