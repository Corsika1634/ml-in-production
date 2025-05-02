# ML-in-production

## Project Description
This project aims to provide a comprehensive guide and tools for deploying machine learning models in production environments.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Corsika1634/ML-in-production.git
   cd ML-in-production
   ```

---

## 🧪 Inference Benchmark (PR4)

This benchmark compares **sequential vs parallel inference performance** using a simulated `predict(x)` function  
(each call sleeps for 10ms to emulate latency).

The script is located at:
```
benchmark/benchmark_inference.py
```

### 🔍 Results (100 inference requests)

| Mode        | Time (s)    |
|-------------|-------------|
| Sequential  | 1.2059      |
| Parallel    | 0.5086      |

**Speedup:** ~2.37× faster with multiprocessing

