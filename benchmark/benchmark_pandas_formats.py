import time
import pandas as pd
import os

# Gene
def generate_dataframe(n_rows=100_000):
    return pd.DataFrame({
        "col1": range(n_rows),
        "col2": [f"text_{i}" for i in range(n_rows)],
        "col3": [i * 0.5 for i in range(n_rows)],
    })

# Fun
def benchmark_format(df, save_func, load_func, format_name):
    print(f"\nBenchmarking {format_name}...")

    # Save
    start_time = time.time()
    save_func(df)
    save_duration = time.time() - start_time

    # Load
    start_time = time.time()
    _ = load_func()
    load_duration = time.time() - start_time

    print(f"Save time: {save_duration:.4f} seconds")
    print(f"Load time: {load_duration:.4f} seconds")

def main():
    df = generate_dataframe()
    os.makedirs("benchmark_outputs", exist_ok=True)

    benchmark_format(
        df,
        save_func=lambda d: d.to_csv("benchmark_outputs/test.csv", index=False),
        load_func=lambda: pd.read_csv("benchmark_outputs/test.csv"),
        format_name="CSV"
    )

    benchmark_format(
        df,
        save_func=lambda d: d.to_parquet("benchmark_outputs/test.parquet"),
        load_func=lambda: pd.read_parquet("benchmark_outputs/test.parquet"),
        format_name="Parquet"
    )

    benchmark_format(
        df,
        save_func=lambda d: d.to_feather("benchmark_outputs/test.feather"),
        load_func=lambda: pd.read_feather("benchmark_outputs/test.feather"),
        format_name="Feather"
    )

    benchmark_format(
        df,
        save_func=lambda d: d.to_pickle("benchmark_outputs/test.pkl"),
        load_func=lambda: pd.read_pickle("benchmark_outputs/test.pkl"),
        format_name="Pickle"
    )

if __name__ == "__main__":
    main()
