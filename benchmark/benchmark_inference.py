import time
import multiprocessing as mp

# Fake inference function
def predict(x):
    time.sleep(0.01)  # Simulate prediction time
    return x * x

# Sequential run
def run_sequential(inputs):
    results = []
    for x in inputs:
        results.append(predict(x))
    return results

# Parallel run
def run_parallel(inputs):
    with mp.Pool(mp.cpu_count()) as pool:
        results = pool.map(predict, inputs)
    return results

def main():
    inputs = list(range(100))  # 100 "requests" for inference

    print("\nSequential inference...")
    start = time.time()
    run_sequential(inputs)
    duration_seq = time.time() - start
    print(f"Sequential execution time: {duration_seq:.4f} seconds")

    print("\nParallel inference...")
    start = time.time()
    run_parallel(inputs)
    duration_par = time.time() - start
    print(f"Parallel execution time: {duration_par:.4f} seconds")

    print("\nSummary:")
    print(f"- Sequential: {duration_seq:.4f}s")
    print(f"- Parallel: {duration_par:.4f}s")
    print(f"- Speedup: {duration_seq / duration_par:.2f}x faster")

if __name__ == "__main__":
    main()
