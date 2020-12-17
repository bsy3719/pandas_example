import pandas as pd

class ReadFunction():
    # /Users/baek/git/datacentro/data-centro-python/sample/titanic_set.csv

    def load_file(path, sep, usecols, nrows, encoding):
        return pd.read_csv(path, sep=sep, usecols=usecols, nrows=nrows, encoding=encoding)