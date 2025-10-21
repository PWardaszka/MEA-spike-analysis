import pandas as pd
import os

def load_mea_data(filepath, save_cleaned=True):
    """
    Load and clean MEA spike data exported as ASCII from Multi Channel DataManager.
    
    Parameters:
        filepath (str): Path to the raw CSV file.
        save_cleaned (bool): Whether to save the cleaned DataFrame to 'data/processed/'.

    Returns:
        pd.DataFrame: Cleaned spike timestamps (µs), columns = electrodes
    """
    # skip 6 lines (metadata)
    df = pd.read_csv(filepath, skiprows=6)

    # delete empty columns
    df.dropna(axis=1, how='all', inplace=True)

    # save to data/processed
    if save_cleaned:
        filename = os.path.basename(filepath)
        processed_path = os.path.join("data", "processed", filename)
        df.to_csv(processed_path, index=False)
        print(f"[INFO] Cleaned data saved to: {processed_path}")

    return df
