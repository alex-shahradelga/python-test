# Last updated: 2026-01-23 04:11:44

def fibonacci(n):    if n <= 1:        return n    return fibonacci(n-1) + fibonacci(n-2)if __name__ == "__main__":    for i in range(10):        print(f"F({i}) = {fibonacci(i)}")
