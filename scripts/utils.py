import pathlib
import pandas as pd



def load_data(data_splits, dataset = "GSEA_InContext"):
    data = {}
    for data_split in data_splits:
       file = pathlib.Path("../data", f"{dataset}_{data_split}.tsv.gz")
       data[data_split] = pd.read_csv(file, sep="\t")
        
    return data
