from sys import argv, stdout
from pathlib import Path
import re
"""
The whole point of writing this script is to concat a bunch of data files without 
worrying about the repeating headers
"""



def glob_years(datadir, start_year, end_year):
    """
    this method expects the datadir to be a certain Path containing files in this format:
    datadir/
        |_2005.csv
        |_2006.csv
        Yields: string, line of text
        """
        tx = str(start_year)
        ty = str(end_year)
