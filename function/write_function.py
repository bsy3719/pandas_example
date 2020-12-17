import pandas as pd

class WriteFunction():

    def wirte_file(self, path):
        return pd.to_csv(path)