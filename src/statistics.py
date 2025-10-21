import pandas as pd

def calculate_activity_per_electrode(df: pd.DataFrame) -> pd.Series:
    """
    Count the number of spikes (timestamps) for each electrode.
    """
    return df.count()


def calculate_activity_stats(df: pd.DataFrame, min_spikes: int = 10) -> dict:
    """
    Calculate summary statistics:
    - Number of active electrodes (with at least `min_spikes` events)
    - Total number of spikes across all electrodes
    """
    non_nan_counts = df.count()
    num_active_electrodes = (non_nan_counts >= min_spikes).sum()
    total_timestamps = non_nan_counts.sum()

    return {
        "num_active_electrodes": int(num_active_electrodes),
        "total_timestamps": int(total_timestamps),
    }


def calculate_firing_rates(df: pd.DataFrame, duration_seconds: float, min_spikes: int = 10) -> pd.Series:
    """
    Calculate firing rate (Hz) for each active electrode.
    """
    spike_counts = df.count()
    active_electrodes = spike_counts[spike_counts >= min_spikes]
    firing_rates = active_electrodes / duration_seconds
    return firing_rates


def calculate_average_firing_rate(df: pd.DataFrame, duration_seconds: float, min_spikes: int = 10) -> float:
    """
    Calculate average firing rate across all active electrodes.
    """
    firing_rates = calculate_firing_rates(df, duration_seconds, min_spikes)
    return firing_rates.mean()


# Optional test block
if __name__ == "__main__":
    # Wczytaj dane z przetworzonego pliku
    filepath = "data/processed/WT 41542 7DIV.csv"
    df = pd.read_csv(filepath)

    # Jeśli trzeba, popraw nagłówki
    df.columns = df.columns.astype(str)

    # Czas nagrania (np. 10 minut)
    duration_seconds = 10 * 60

    # Statystyki aktywności
    stats = calculate_activity_stats(df)
    print("Spike activity stats:", stats)

    # Firing rates
    firing_rates = calculate_firing_rates(df, duration_seconds)
    print("Firing rates (Hz):\n", firing_rates)

    # Średnia
    avg_rate = calculate_average_firing_rate(df, duration_seconds)
    print("Average firing rate across active electrodes (Hz):", avg_rate)
