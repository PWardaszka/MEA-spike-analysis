import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

def extract_electrode_ids(columns):
    """
    Extract electrode numbers from column names like '47 (ID=0) [µs]'.
    
    Parameters:
        columns (list): List of column names.
    
    Returns:
        list: List of electrode numbers as integers.
    """
    ids = []
    for col in columns:
        match = re.search(r'^(\d+)', col)
        if match:
            ids.append(int(match.group(1)))
        else:
            ids.append(col)  # fallback: keep original if no match
    return ids

def generate_raster_plot_from_df(df, title="Raster Plot", xlabel="Time (minutes)", ylabel="Electrode number"):
    """
    Generate a raster plot from a DataFrame containing spike timestamps (in µs).
    
    Parameters:
        df (DataFrame): Columns = electrodes, values = timestamps in µs
    """
    # Convert timestamps from µs to minutes
    df = df / (1e6 * 60)

    fig, ax = plt.subplots(figsize=(12, 10))

    for i, column in enumerate(df.columns):
        event_times = df[column].dropna().values
        for time in event_times:
            ax.plot([time, time], [i + 0.9, i + 1.1], color='blue', linewidth=2)

    ax.set_yticks(np.arange(len(df.columns)) + 1)
    ax.set_yticklabels(df.columns)

    ax.set_title(title, fontsize=16)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    ax.set_xlim([df.min().min(), df.max().max()])
    ax.set_ylim([0.5, len(df.columns) + 0.5])
    ax.tick_params(axis='both', labelsize=14)

    plt.tight_layout()
    plt.show()

def main():
    # Ścieżka do już przetworzonego pliku (bez metadanych)
    filepath = "data/processed/WT 41542 7DIV.csv"

    # Wczytaj przetworzony plik CSV
    df = pd.read_csv(filepath)

    # Zamień nagłówki na numer elektrodu (np. 47, 48, ...)
    df.columns = extract_electrode_ids(df.columns)

    # Raster plot
    generate_raster_plot_from_df(df, title="Example MEA Raster Plot")

if __name__ == "__main__":
    main()
