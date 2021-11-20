# -*- coding: utf-8 -*-
# @author: Antoine Allard <antoineallard.info>
#
# Custom functions to save pandas dataframes as nicely formatted tables into a text file, and vice versa.

import pandas
import tabulate


def to_table(df, fname, cols=None, comment='#', tabulateprops={}):
    """Custom function to save pandas dataframes as nicely formatted tables into a text file.

    Parameters
    ----------
    fname : str
        The path to the new file in which the hidden parameters will be written.
    cols : string, list or array of strings, optional
        A string, list or an array containing the name of the columns (as strings) to
        be written in the file (if None all columns will be written).
    comment : string, optional
        Symbol used to indicate commented lines. Default: '#'.
    tabulateprops : dict, optional
        Options to pass to the tabulate function (https://pypi.org/project/tabulate). Default: tablefmt='plain', stralign='right', colalign=('left',)
    """

    if cols is None:
        cols = df.columns
    else:
        if type(cols) is str:
            cols = [cols]
        assert all(col in df.columns for col in cols), 'Error: some columns are not in the dataframe.'
    header = list(cols)
    header[0] = comment + ' ' + header[0]

    # Options for the tabulate package.
    if 'tablefmt' not in tabulateprops:
        tabulateprops['tablefmt'] = 'plain'
    if 'stralign' not in tabulateprops:
        tabulateprops['stralign'] = 'right'
    if 'colalign' not in tabulateprops:
        tabulateprops['colalign'] = ('left',)

    with open(fname, 'w') as f:
        content = tabulate.tabulate(df[cols].values.tolist(), header, **tabulateprops)
        f.write(content)



def from_table(fname, comment='#'):
    """Custom function to read nicely formatted tables into pandas dataframes from a text file.

    Parameters
    ----------
    fname : str
        The path to the new file in which the hidden parameters will be written.
    comment : str, optional
        Ssymbol used to indicate commented lines. Default: '#'.

    Returns
    -------
    pandas.DataFrame
    """

    df = pandas.DataFrame()
    with open(fname, 'r') as f:
        header = f.readline().replace(comment, ' ').split()
        df = pandas.read_table(f, names=header, comment=comment, delimiter=r"\s+")
    return df


pandas.DataFrame.to_table = to_table
pandas.from_table = from_table



if __name__ == '__main__':

    details = {
        'Name' : ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
        'Age' : [23, 21, 22, 21],
        'University' : ['BHU', 'JNU', 'DU', 'BHU'],
     }

    df1 = pandas.DataFrame(details)
    df1.to_table('table_test.txt')
    df2 = pandas.from_table('table_test.txt')

    print(df1 == df2)

