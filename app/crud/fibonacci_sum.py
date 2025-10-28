from fastapi import HTTPException

async def sum_fib():
    try:
        N = 50
        # Initialize the first two numbers and the total sum
        a, b = 0, 1
        total_sum = 0
    
        # The Fibonacci sequence starts 0, 1, 1, 2, 3, 5, ...
        for _ in range(N):
            total_sum += a
            a, b = b, a + b # Update a to b, and b to the next number (a+b)
        return {
           "sum": total_sum
        }
    except HTTPException as Httpexc:
        raise Httpexc

