import pandas as pd
def benchmark(csv_path):
    df = pd.read_csv(csv_path)
    n = len(df)
    print(f"Average time to complete {n} texts: {df.time.mean(): .3f}")
    print(f"Average output tokens: {df.tokens_generated.mean(): .3f}")
    df["tokens_per_sec"] = df.tokens_generated / df.time
    print(f"Average tokens/sec: {df.tokens_per_sec.mean(): .3f}")
    return df

benchmark("C:/Users/shiva/OneDrive/Desktop/simp/vllm-benchmark-1-GPUs.csv")