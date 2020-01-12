def rec_fib(n):
 if n < 2:
    return n
 else:
    return rec_fib(n-1)+rec_fib(n-2)

 def measure(n):
     start = time.time()
     for _ in range(50):
         x = rec_fib(n)
     end = time.time()
     return (end - start) / 50

 