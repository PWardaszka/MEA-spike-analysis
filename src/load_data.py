import pandas as pd

def load_mea_data(filepath):
    """
    Load and clean MEA spike data exported as ASCII from Multi Channel DataManager.
    
    Parameters:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Raw spike timestamps, columns = electrodes, values = spike times (in µs)
    """
    # Pomijamy pierwsze 6 linii (metadane)
    df = pd.read_csv(filepath, skiprows=6)

    # Usuwamy ewentualne puste kolumny
    df.dropna(axis=1, how='all', inplace=True)

    return df
