from fastapi import APIRouter, HTTPException, status
from ..schema.fibonacci_sum import FibRes
from ..crud.fibonacci_sum import sum_fib

router = APIRouter(tags=["Fibonacci Sum"])


@router.get("/fibonacci-sum", response_model=FibRes, status_code=status.HTTP_200_OK)
async def sum_fibonacci_sequence():
    """
    Q9: Sums the first 50 fibonacci sequence.
    """
    try:
        return await sum_fib()
    except HTTPException as Httpexc:
        raise Httpexc
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = str(e)
        )
