import pandas as pd

class StreamingDataset:
    def __init__(self, filepath, batch_size=32):
        """
        Initializes the StreamingDataset.

        Args:
            filepath (str): Path to the CSV file.
            batch_size (int): Number of rows per batch.
        """
        self.filepath = filepath
        self.batch_size = batch_size

    def __iter__(self):
        """
        Yields batches of data from the file.
        """
        for chunk in pd.read_csv(self.filepath, chunksize=self.batch_size):
            yield chunk

def main():
    # Example usage
    dataset = StreamingDataset("benchmark_outputs/test.csv", batch_size=10)

    for i, batch in enumerate(dataset):
        print(f"\nBatch {i+1}")
        print(batch)

if __name__ == "__main__":
    main()
