from src.load_data import load_mea_data

df = load_mea_data("data/raw/WT 41542 7DIV.csv")
print(df.head())
