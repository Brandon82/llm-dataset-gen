import pandas as pd

def initialize_empty_dataset(columns, filename):
    empty_dataset = pd.DataFrame(columns=columns)
    empty_dataset.to_csv(filename, index=False)