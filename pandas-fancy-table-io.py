# -*- coding: utf-8 -*-
# @author: Antoine Allard <antoineallard.info>
#
# Custom functions to save pandas dataframes as nicely formatted tables into a text file, and vice versa.

import pandas
import tabulate


def to_fancy_table(df, filename, cols=None, comment='#', tabulateprops={}):
    """Custom function to save pandas dataframes as nicely formatted tables into a text file.

    Parameters
    ----------
    filename : str
        The path to the new file in which the hidden parameters will be written.
    cols : str, list or array of str, optional
        A string, or a list or an array containing the name of the columns (as strings) to
        be written in the file. Default is to write the full dataframe into the text file.
    comment : str, optional
        Symbol used to indicate commented lines. Default is `#`.
    tabulateprops : dict, optional
        Options to pass to the [tabulate](https://pypi.org/project/tabulate) package. Default
        keywords are `tablefmt='plain', stralign='right', colalign=('left',)`.
    """

    if cols is None:
        cols = df.columns
    else:
        if type(cols) is str:
            cols = [cols]
        assert all(col in df.columns for col in cols), 'Error: some columns are not in the dataframe.'
    header = list(cols)
    header[0] = comment + ' ' + header[0]

    # Default options for the tabulate package if none provided.
    if not tabulateprops:
        tabulateprops = {'tablefmt': 'plain',
                         'stralign': 'right',
                         'colalign': ('left',)}

    with open(filename, 'w') as f:
        content = tabulate.tabulate(df[cols].values.tolist(), header, **tabulateprops)
        f.write(content)



def from_fancy_table(filename, comment='#'):
    """Custom function to read nicely formatted tables into pandas dataframes from a text file.

    Parameters
    ----------
    filename : str
        The path to the file containing the fancy table.
    comment : str, optional
        Symbol used to indicate commented lines. Default is `#`.

    Returns
    -------
    pandas.DataFrame
    """

    df = pandas.DataFrame()
    with open(filename, 'r') as f:
        header = f.readline().replace(comment, ' ').split()
        df = pandas.read_table(f, names=header, comment=comment, delimiter=r"\s+")
    return df



if __name__ == '__main__':

    pandas.DataFrame.to_fancy_table = to_fancy_table
    pandas.from_fancy_table = from_fancy_table

    details = {
        'Name' : ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
        'Age' : [23, 21, 22, 21],
        'University' : ['BHU', 'JNU', 'DU', 'BHU'],
     }

    df1 = pandas.DataFrame(details)
    print(df1)
    df1.to_fancy_table('table_test.txt')
    df2 = pandas.from_fancy_table('table_test.txt')

    print(df1 == df2)

